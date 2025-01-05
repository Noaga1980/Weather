

import requests
#Import API KEY from secret
#from secrets import api_key
import streamlit as st
api_key = st.secrets["api_key"]

# Ask city Name From the User
city = st.text_input("Enter the city name: ")

# The URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Sent the request to API
response = requests.get(url)

# Check if the request success
if response.status_code == 200:
    # Converting the response to JSON format
    data = response.json()

    # Import the relevant data
    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    # print the results
    st.write(f"Weather in {city_name}:")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Description: {weather_description}")
    st.write(f"Humidity: {humidity}%")
else:
    # Error handling
    st.write(f"Failed to retrieve data: {response.status_code}")
