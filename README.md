# Weather App

A simple Flask weather application that fetches current weather details from OpenWeatherMap.

## Setup

1. Install Python.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Open the `.env` file and replace `PASTE_YOUR_NEW_API_KEY_HERE` with your OpenWeatherMap API key:

   ```env
   OPENWEATHER_API_KEY=your_actual_api_key
   ```

6. Run the application:

   ```bash
   python app.py
   ```

7. Open the local URL shown in the terminal (usually http://127.0.0.1:5000).

## GitHub security

- `.env` contains your private API key and is excluded by `.gitignore`.
- Commit `.env.example` so others know which environment variable to configure.
- Never upload your real `.env` file or share your API key publicly.
- If an API key was already committed or exposed, revoke/regenerate it in your OpenWeatherMap account. Removing it from the latest code does not make an exposed key private again.
