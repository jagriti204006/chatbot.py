
import wikipedia
import winsound
from playsound import playsound
import os 
import pywhatkit as kit
from datetime import datetime
from string import printable as chars
from random import choice, sample as ls
from subprocess import call
import webbrowser
import time
import pyttsx3
import speech_recognition as sr
import pyaudio

bot = pyttsx3.init()
bot.setProperty('rate',140)
bot.setProperty('volume',1000)
voices = bot.getProperty('voices')
print('''Whats your gender:             #asking for gender of user and assigning the assistant of opposite gender
1. Male 
2. Female ''')
gender = int(input("Enter your gender: "))
if gender == 2:
    voiceId = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
elif gender == 1:
    voiceId = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

bot.setProperty('voice',voiceId)  #setting property of voice
bot.say("Heyy! I am your assistant!")
print("\a")
bot.runAndWait()

  
# # Initialize the recognizer 
listener = sr.Recognizer() 
bot = pyttsx3.init()



# print("Going to while True")
# below are the intents : read aloud anyone of these when the terminal shows "Speak now"

whatsappIntent = ["send a message on whatsapp", "send a text on Whatsapp", "whatsapp"]
helloIntent = ["hi", "hello", "bonjour", "hey", "hola amigo", "hola", "heyya", "namaste", "namaskar"] 
greetingIntent = ["how are you", "wassup", "whats up", "wbu", "how you doing", "how you doin", "how have you been", "kaise ho", "kya haal hai"] 
greetAnsIntent = ["i am fine", "i am good", "i am okay", "i am all good", "all good"] 
songsIntent = ["play a song", "play something for me", "play a random song"]
wikiIntent = ["open wikipedia", "get info from wikipedia", "get me information"] 
siteIntent = ["open google", "open the site"] 
youtubeIntent = ["play a song on youtube", "play something for me on youtube", "play a random song on youtube", "play a video on youtube"]
whistleIntent = ["whistle for me", "blow whistle", "blow a whistle", "blow a whistle for me"]
datetimeIntent = ["tell me the date and time", "date and time", "today's date and time", "current date and time"]
passwordIntent = ["generate a strong password", "generate a password", "give a strong password"]
byeIntent = ["bye", "talk to you later", "see you later", "later"] 

while True:
    print("In while true")
    with sr.Microphone() as source:   # declaring microphone as the source of voice
        print("Speak now..")
        
        voice = listener.listen(source) 
        print("goin to try")
        try:                            # try-except for mature termination of the code if the assistant does not understand the user voice
            print("in try block")
            command = listener.recognize_google(voice)       #getting the command of the user
            
            print("Converting..")                           
            print(command)
        except:
                                                    
            bot.say("Try Again")
            bot.runAndWait()
            print("Speech unclear!!")
            print("Try again")
            break

    

    if command.lower() in helloIntent:
        bot.say("Hello")
        print("Hello")

    elif command.lower() in whatsappIntent:
        bot.say("Enter the mobile number ")
        mob = input("Enter the mobile number: ")
        bot.say("Enter the message")
        msg = input("Enter the message: ")
        bot.say("Enter the time ")
        hr = int(input("Hours: "))
        mn = int(input("Minutes: "))
        kit.sendwhatmsg(mob, msg, hr, mn)
        print("sent")
        
    elif command.lower() in greetingIntent:
        bot.say("I am fine... Thank you")
        print("I am fine... Thank you")

    elif command.lower() in greetAnsIntent:
        print("Thats good to hear. Tell me more")
        bot.say("Thats good to hear. Tell me more")

    elif command.lower() in songsIntent:
        print("PLease wait")
        bot.say("Please wait")
        songs = os.listdir()
        print('''1. Play a random song
                 2. Select a song
              ''')
        ch = int(input("Enter your choice: "))
        if ch==1:
            currentSong = choice(songs)
            os.startfile(currentSong)
        elif ch==2:
            for i, song in enumerate(songs):
                print(f"{i+1}. {song}")
            print("Press 0 to exit music player...")
            while True:
                userMessage = int(input("Which one do you want to play: "))
                if userMessage == 0:
                    break
                songIndex = userMessage - 1
                os.startfile(songs[songIndex])
                break

    elif command.lower() in passwordIntent:
        print("How many digits you want in your password: ")
        PASS = ''.join(ls(chars[:94],int(input(""))))
        print(PASS)

    elif command.lower() in wikiIntent:
        print("Enter the topic: ")
        bot.say("Enter the topic: ")
        topic = input()
        data = wikipedia.summary(topic)
        print(data)
        bot.say(data)
    
    elif command.lower() in datetimeIntent:
        bot.say(f"Today's date and time : {datetime.now()}")
        print(f"Today's date and time : {datetime.now()}")
   
    elif (command.lower().find("open")!=-1):
        bot.say("Enter the website name again")
        website = input("Enter the website name again: ")
        print("Please wait ")
        bot.say("Please wait")
        webbrowser.open(f"https://www.{website}.com")

    elif command.lower() in whistleIntent:
        playsound('{location of your audio file of whistle}')

    elif command.lower() in youtubeIntent:
        bot.say("What do you want to play on youtube: ")
        bot.runAndWait()
        whatToFind = input("Enter the topic of video to find : ")
        kit.playonyt(whatToFind)

    elif command.lower() in byeIntent:
        bot.say("Okay, will see you later... Have a good day")
        bot.runAndWait()
        exit()
    else :
        bot.say("I didn't understand.")
 
    bot.runAndWait()
