# 🌦️ Weather App

A modern and responsive Weather Forecast Web Application built using Python Flask, HTML, and CSS. This application uses the OpenWeatherMap API to fetch and display real-time weather information for different cities around the world.

## ✨ Features

- 🌍 Search weather information by city name.
- 🌡️ Display real-time temperature in Celsius.
- 💧 Show humidity details.
- ☁️ Display current weather conditions.
- 🎨 Modern and professional user interface.
- 📱 Responsive design for different screen sizes.
- 🔐 Secure API key management using environment variables.
- ⚡ Real-time weather data through OpenWeatherMap API.

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3
- **Backend:** Python, Flask
- **API:** OpenWeatherMap API
- **Environment Management:** Python Dotenv
- **HTTP Requests:** Requests Library

## 📂 Project Structure

```text
Weather-App/
│
├── app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Weather-App
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file in the project root directory.

Add your OpenWeatherMap API key:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Get your API key from:

https://openweathermap.org/api

### 7. Run the Application

```bash
python app.py
```

### 8. Open in Browser

```text
http://127.0.0.1:5000
```

## 🔐 API Key Security

- API keys are stored in the `.env` file.
- Python Dotenv loads environment variables securely.
- The `.gitignore` file prevents the `.env` file from being uploaded to GitHub.
- The `.env.example` file provides a sample configuration.

**Important:** Never upload your actual API key to a public GitHub repository.

## 🌐 API Integration

This project uses the OpenWeatherMap Current Weather API to retrieve:

- City Name
- Temperature
- Humidity
- Weather Description

## 🚀 Future Enhancements

- Weather icons based on weather conditions.
- Five-day weather forecast.
- Current location weather detection.
- Wind speed and pressure information.
- Search history.

## 👩‍💻 Author

**Your Name**

GitHub: YOUR_GITHUB_PROFILE_URL

## 📄 License

This project is created for educational and learning purposes.
