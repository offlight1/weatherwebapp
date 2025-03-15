from flask import Flask, request, jsonify   
import requests
from flask_cors import CORS


app = Flask(__name__ )

API_KEY = "a799bb915333eb3713547d3e161dc606"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"   

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city') 
    
    if not city:
        return jsonify({
            "error": "Please provide city name"
        }), 400
        
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)    
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "city": data["name"],
        })
    else:
        return jsonify({
            "error": "City not found"
        }), 404
    
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)