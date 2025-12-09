import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import re 

from services.weather_handler import get_current_weather
from services.email_handler import send_simple_email, set_calendar_reminder
from services.smart_home import control_device


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    """Converts text to speech."""
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

def listen_command():
    """Captures audio from microphone and returns transcribed text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1.2
        r.energy_threshold = 400
        
        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            return "none"
        
    try:
        query = r.recognize_google(audio, language='en-in').lower() 
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        return "none"
    except sr.RequestError:
        return "service_error"




def execute_email_task(query):
    """Uses basic RegEx/Keyword matching to simulate NLU for email."""
    
        match = re.search(r"to (.*?) subject (.*?) body (.*)", query)
    if not match:
        speak("I need the recipient, subject, and body. Please try: 'send email to [recipient] subject [subject] body [message]'")
        return
        
    recipient, subject, body = match.groups()
    
   
    recipient_email = f"{recipient.strip().replace(' ', '.')}@example.com" 
    
    speak(f"Composing email to {recipient} with subject {subject}...")
    success, message = send_simple_email(recipient_email, subject, body)
    
    if success:
        speak(f"Email successfully sent to {recipient}!")
    else:
        speak(f"Failed to send email. {message}")


def execute_weather_task(query):
    """Uses basic keyword matching to find location."""
    
    match = re.search(r"weather in (.*?)$", query)
    city_name = match.group(1).strip() if match else "indore"
    
    speak(f"Checking the forecast for {city_name}.")
    weather_report = get_current_weather(city_name)
    speak(weather_report)
    

def execute_smart_home_task(query):
    """Uses basic keyword matching for smart home control."""
    
    if "turn on" in query and "living room lights" in query:
        topic = "homeassistant/light/living_room/command"
        payload = "ON"
        success, message = control_device(topic, payload)
        if success:
            speak("Living room lights are now on.")
        else:
            speak(f"Could not reach the smart hub. {message}")
            
   
    else:
        speak("I don't recognize that specific smart home command.")



def run_assistant():
    """Main loop to listen and execute commands."""
    
    speak("System Ready. How may I help you?")
    
    while True:
        query = listen_command()
        
        if query == "none":
            continue
        elif query == "service_error":
            speak("I cannot reach the speech recognition service. Please check your network.")
            continue
            
       

        if 'wikipedia' in query:
           
            try:
                search_term = query.replace("wikipedia", "").strip()
                if not search_term:
                    speak("What would you like to search for on Wikipedia?")
                    continue
                speak(f'Searching Wikipedia for {search_term}...')
                results = wikipedia.summary(search_term, sentences=2)
                speak(results)
            except:
                speak("Sorry, I could not find that information.")

        elif 'open youtube' in query or 'open browser' in query:
            
            speak("Opening browser to YouTube.")
            webbrowser.open("http://youtube.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {strTime}")

        elif 'weather in' in query or 'forecast' in query:
            
            execute_weather_task(query)
            
        elif 'send email' in query or 'compose email' in query:
            
            execute_email_task(query)
            
        elif 'set reminder' in query:
        
            speak(set_calendar_reminder("Call doctor", "3 PM tomorrow"))
            
        elif 'turn on' in query or 'turn off' in query:
         
            execute_smart_home_task(query)

        elif 'stop' in query or 'exit' in query or 'goodbye' in query:
            speak("Goodbye! Shutting down the assistant.")
            break
            
        else:
            speak("I'm sorry, I don't recognize that command. Try 'What is the time?' or 'Check weather in London'.")

if __name__ == "__main__":
    run_assistant()
