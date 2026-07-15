# Weather Application

A simple desktop Weather Application built with **Python**, **Tkinter**, and the **OpenWeatherMap API**. The application allows users to search for any city and instantly view current weather details in a clean graphical interface.

## Features

- Search weather by city name
- Displays:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Atmospheric Pressure
  - Wind Speed
  - Weather Condition
- User-friendly Tkinter GUI
- Real-time weather data using OpenWeatherMap API

## Project Structure

```text
Weather Application/
│
├── Weather_backend.py      # Handles API requests and weather data processing
├── weather_frontend.py     # Tkinter GUI for user interaction
├── README.md
└── requirements.txt
```

## Technologies Used

- Python 3
- Tkinter
- Requests
- OpenWeatherMap API

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-application.git
cd weather-application
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python weather_frontend.py
```

## API Key Setup

This project uses the OpenWeatherMap API.

1. Create a free account on OpenWeatherMap.
2. Generate an API key.
3. Replace the value of `API_KEY` in `Weather_backend.py`:

```python
API_KEY = "YOUR_API_KEY"
```

## Example Output

```text
City: Delhi, IN
Temperature: 32°C
Feels Like: 35°C
Humidity: 68%
Pressure: 1008 hPa
Wind Speed: 3.2 m/s
Condition: Clear Sky
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Rudra Chaudhary