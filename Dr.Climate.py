''' Python Weather Forcasting Program using Python
    it take voice command as input it will ask you city
    name for which you want to know the weather.
    we have to tell city name in device microphone
    after programs record city name it will display and
    tell all weather report of the day.
    We can extend this program by showing weather of whole
    week or even month as well. it will help farmers '''  
     

# Created by : Abhijeet Khatri
# Email : abhijeetkhatri3969@gmail.com



import pyowm
import speech_recognition as sr
import pyttsx3
import datetime
Ip = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greetMe():
    hour=datetime.datetime.now().hour
   # Username = input(speak("Hello User, what is your name?"))
    #print(hour)
    if hour>0 and hour<12:
        speak("HelloGood Morning")
        print("Hello Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Hello Good Afternoon")
        print("Hello Good Afternoon")
    else:
        speak("Hello Good Evening")
        print("Hello Good Evening")
def takeCommand():
    statement = " "
    try:
         with sr.Microphone() as source:
            print("Dr.Climate Listening....")
            Ip.adjust_for_ambient_noise(source)
            audio = Ip.listen(source)
            statement = Ip.recognize_google(audio, language='en-in')
            print(statement)
    except Exception as e:
            speak("I can't heard you proparly,please say that again")
            return None
    return statement
print("Welcome to Docter Climate")
speak("Welcome to Docter Climate")
greetMe()
if __name__ =='__main__':
    speak("Please Tell me your city name?")
    CityName = takeCommand()
    print(CityName)

try:
    Own = pyowm.OWM('0e1cceaa20984b7f9a7c2844bbff459e')
    location = Own.weather_at_place(CityName)
    weather = location.get_weather()
    temp = weather.get_temperature('celsius')
    humidity = weather.get_humidity()
    wind = weather.get_wind()
    pressure = weather.get_pressure()
#Report = weather.get_weather()
#print("City:" +Own.get_location())
    speak(CityName)
    print(temp)
    speak("Todays Temperature in:" + CityName)
    speak(temp)
    for key,value in temp.items():
        print(key , value)
    print("Humidity:"+str(humidity))
    speak("Humidity:in"+CityName+"is"+str(humidity))
    print("Wind:-"+str(wind))
    speak("Wind in Kilometer per hour in :-"+CityName+"is"+str(wind))
    print("pressure:-"+str(pressure))
    speak("Atmosphare pressure in :-"+CityName+"is"+str(pressure))
    print(weather)
    print("Today weather report:")
    speak("Today weather report:")
    forecast = Own.three_hours_forecast(CityName)
#print("3 hours forecast"+str(forecast))
#speak("3 hours forecast in"+CityName+"is")
    Rainreport = forecast.will_have_rain()
    Rainstatus = ""
    if Rainreport is True:
        Rainstatus = "Yes"
    else:
        Rainstatus = "No"
    print("Will have Rain Today in?")
    speak("Will have Rain Today in?"+CityName)
    print(Rainstatus)
    speak(Rainstatus)
    Sunreport = forecast.will_have_sun()
    Sunstatus = ""
    if Sunreport is True:
        Sunstatus = "Yes"
    else:
        Sunstatus = "No"
    print("Will have Sunny day Today in ?")
    speak("Will have Sunny day Today in?"+CityName)
    print(Sunstatus)
    speak(Sunstatus)
    Cloudreport = forecast.will_have_clouds()
    Cloudstatus = ""
    if Cloudreport is True:
        Cloudstatus = "Yes"
    else:
        Cloudstatus = "No"
    print("Will have Cloud Today in ?")
    speak("Will have Cloud Today in ?"+CityName)
    print(Sunstatus)
    speak(Sunstatus)
    TodayStatus = weather.get_status()
    DetailStatus = weather.get_detailed_status()
    print("Weather Status :" +TodayStatus)
    speak("Todays Weather Status of:"+CityName+ "is"+TodayStatus)
    print("Detail Weather Status:" +DetailStatus)
    speak("Todays Detail Weather Status of:"+CityName+ "is" +DetailStatus)
    print("Now listen advise from Dr.Climate: based on todays weather in" +CityName)
    speak("Now listen advise from Dr.Climate: based on todays weather in"+CityName)
    if TodayStatus == "Haze" or TodayStatus == "haze":
        print("Advise to vehical driver Please drive your vehical slowly and carefully beacuase there is Haze in your city" +CityName)
        speak("Advise to vehical driver Please drive your vehical slowly and carefully beacuase there is Haze in your city"+CityName)
    elif TodayStatus == "clear" or TodayStatus == "clear sky" or TodayStatus == "Clear":
        speak("Todays is lovely weather for travelling and trip enjoy your day")
    elif TodayStatus == "Clouds" or TodayStatus == "clouds":
        print("There could be drizzle in your city please keep umbrella with you")
        speak("There could be rain in your city please keep umbrella with you")
    elif TodayStatus == "Smoke" or TodayStatus == "smoke":
        print("There is smoke in your city and which is harmfull for your lunks please wear mask on your mouth")
        speak("There is smoke in your city  and which is harmfull for your lunks please wear mask on your mouth")
    else:
        speak("Status not found")
    print("Thank you To Visit Docter Climate ")
    speak("----Thank you To Visit Docter Climate----")
except timeout as e:
    print("Socket Timeout")



#print("Report:"+str(Report))

