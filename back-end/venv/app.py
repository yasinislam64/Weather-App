from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) #Enable CORS to connect to the front-end

# Replace with your actual API key from OpenWeatherMap
API_KEY = '5c55dd910cfa7df5d61ecc9cbd8f5f33'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    # Build the URL for the API request
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        # Send a GET request to the weather API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant data from the API response
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return jsonify(weather_info)
        else:
            return jsonify({'error': data.get('message', 'Unable to fetch weather data')}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

