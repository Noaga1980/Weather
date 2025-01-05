Weather App

This project is a simple weather application built using Python and the Streamlit framework. The app retrieves weather information for a given city using the OpenWeatherMap API and displays it interactively.

Features

Fetches current weather data, including:

Temperature (in Celsius)

Weather description

Humidity level

Interactive user input for city name

Error handling for invalid requests

Prerequisites

Python Dependencies

Ensure you have Python installed (version 3.7 or later recommended). The required Python packages are listed below:

requests

streamlit

You can install them using:

pip install requests streamlit

OpenWeatherMap API Key

You need an API key from OpenWeatherMap to use this application. You can get one by creating a free account on their website.

How to Run the App

Clone or download this repository to your local machine.

Save your OpenWeatherMap API key in Streamlit's secrets file. To do this:

Create a .streamlit folder in the root directory of your project.

Inside the .streamlit folder, create a file named secrets.toml.

Add your API key to the file in the following format:

[secrets]
api_key = "your_api_key_here"

Open a terminal or command prompt and navigate to the project directory.

Run the Streamlit app with the command:

streamlit run main.py

The app will open in your default web browser. If it does not, copy the URL displayed in the terminal (e.g., http://localhost:8501) and paste it into your browser.

File Structure

project/
├── main.py            # The main Python script for the app
├── .streamlit/        # Folder for Streamlit configuration
│   └── secrets.toml   # File containing the API key
└── README.md          # Documentation for the project

Usage

Enter the name of the city for which you want weather data.

The app will display the following information if the city is found:

Temperature

Weather description

Humidity

If the city is not found or there is an error, the app will show an appropriate message.

Troubleshooting

Error: Failed to retrieve data

Ensure your API key is correct and has not expired.

Check your internet connection.

Verify that the city name is spelled correctly.

Streamlit app does not open

Ensure you ran the app using streamlit run main.py.

Check that the required packages are installed.

License

This project is open-source and available under the MIT License.