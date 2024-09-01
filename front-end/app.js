function getWeather() {
    const city = document.getElementById('city').value;
    if (!city) {
        alert('Please enter a city');
        return;
    }

    fetch(`http://127.0.0.1:5000/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('weather-result').innerText = data.error;
            } else {
                document.getElementById('weather-result').innerHTML = `
                    <p><strong>Weather in ${data.name}:</strong></p>
                    <p>Temperature: ${data.main.temp}°C</p>
                    <p>Humidity: ${data.main.humidity}%</p>
                    <p>Weather: ${data.weather[0].description}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('weather-result').innerText = 'An error occurred while fetching weather data.';
        });
}
