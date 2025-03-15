document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("getWeather");
    const cityInput = document.getElementById("city");
    const weatherResult = document.getElementById("weatherResult");

    button.addEventListener("click", function () {
        const city = cityInput.value.trim();

        if (city === "") {
            weatherResult.textContent = "Please enter a city name.";
            return;
        }

        // Call our Flask backend
        fetch(`http://127.0.0.1:5000/weather?city=${city}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    weatherResult.textContent = "City not found. Please try again.";
                } else {
                    weatherResult.textContent = `Temperature: ${data.temperature}°C, Condition: ${data.condition}`;
                }
            })
            .catch(error => {
                weatherResult.textContent = "Error fetching weather data.";
                console.error("Error:", error);
            });
    });
});
