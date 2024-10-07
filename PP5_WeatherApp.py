import tkinter as tk
import requests
#define fxn with city as parameter, for info to be fetched about
def get_weather(city):
    #variables to hold 
    api_key = ''
    base_url = ''
    #dictionary for parameters for api req.
    params = {
        'q':city,
        'appid': api_key,
        #unit parameter set to farenheit
        'units': 'imperial'
    }
    #hold the response from the api
    response = requests.get(base_url, params=params)
    #return json response as dictionary
    return response.json()

def show_weather():
    #retrieves city name from entry
    city = city_entry.get()
    #sends req. to api using city (parameter) and returns weather data in json format

    weather_data = get_weather(city)
    #if status code isnt 200 print error message
    if weather_data.get('cod') != 200:
        weather_info.set(f'Error: {weather_data.get('message')}')
        return
    
    city_name = weather_data.get('name')
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    #set info into tkinter variable
    weather_info.set(
        f'City: {city_name}\n'
        f'temperature: {temp}F\n'
        f'Humidity: {humidity}%\n'
        f'description:  {description}\n'
        f'wind speed: {wind_speed} m/s'
        
    )
#create main window and set title
root = tk.Tk()
root.title('Weather App')
#create label widget
city_label = tk.Label(root, text= 'Enter city name:')
city_label.pack(pady=10)
#entry widget where user enters city
city_entry = tk.Entry(root)
city_entry.pack(pady=5)
#create a button to show weather when clicked
get_weather_button = tk.Button(root, text='Get Weather',command=show_weather)
get_weather_button.pack(pady=10)

weather_info = tk.StringVar()
weather_info_label = tk.Label(root, textvariable=weather_info, font=('Helvetica',14),justify='left')
weather_info_label.pack(pady=20)

root.mainloop()