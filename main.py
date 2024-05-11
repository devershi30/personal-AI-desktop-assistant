import pyttsx3 # for text to speech conversion, a python library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib
import os


engine = pyttsx3.init('sapi5') #Microsoft API
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Devershi")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Devershi")
    else:
        speak("Good Evening, Devershi")

    speak("Hello, I am Jarvis. How can I help you today, sir?")

def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1 # pause_threshold: Seconds of non-speaking audio before a phrase is considered complete
        # For eg, it does not get complete to record if there is a gap while speaking to microphone

        audio = r.listen(source)

    try:
        print ("Recognizing...") # recognizing the command
        query = r.recognize_google(audio, language = 'en-in')
        print (f"User said: {query}\n")

    except Exception as e:
       # print (e) # Just to see the exception
        print ("Say that again please .....")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enter-you-email', 'password-of-email') # Just for example
    server.sendmail('devershi40@gmail.com', to, content) # receivers email
    server.close()



if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
    
        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
    
        elif 'play music videos' in query:
            music_dir = 'C:\\Users\\dever\\Pictures\\Wedding Pictures (R & K)\\Rushabh_Ring_Ceremony\\RUSHABH & KEYURI'
            songs = os.listdir(music_dir)
            print (songs)
            n = random.randint(0,4) # generating a random number to play different videos everytime you ask
            os.startfile(os.path.join(music_dir, songs[n]))
        
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'open vs code' in query:
            code_path = "C:\\Users\\dever\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                speak("What to write in the email, sir?")
                content = takeCommand()
                to = "devershi40@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print (e)
                speak("Sorry, Sir Devershi, I am not able to send the email. Can you please check what is wrong?")



                


        
