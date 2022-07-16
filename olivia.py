from click import command
import wikipedia
from datetime import datetime
import datetime
from secrets import choice
import random
import speech_recognition as sr
import pyttsx3
import pyjokes
import pywhatkit as kit
import os
import subprocess as sp
import requests
import time
from function_online import weath
import wolframalpha
engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        talk("good morning")
    elif hour >=12 and hour <18:
        talk("good afternoon")
    else:
        talk("good evening")

    talk("iam olivia how can i help you")

def randm():
    confuse = ["I din't get that could you try again?","say some thing"]
    value = random.choice(confuse)
    print(value)
    talk(value)

def talk(txt):
     engine.setProperty("rate", 175)
     engine.say(txt)
     engine.runAndWait()

wishme()
def take_command():
    try:
        with sr.Microphone() as source:
         listener = sr.Recognizer()
         print("Listening....!!!!!!!!!!")
         talk("listening")
         listener.adjust_for_ambient_noise(source)
         voice = listener.listen(source)
         command = listener.recognize_google(voice)
         command = command.lower()
         print(command)
         
    except:
        talk(randm().replace('None',' ')) 
    return command    

while True:
    try:
        command = take_command()
        #olivia_commands
        if "what is your name" in command:
            print(" 'OLIVIA' ")
            talk("olivia")
        elif "how are you" in command:
            print("Iam Fine")
            talk("iam fine")
            print("And What About You")
            talk("and what about you")
        elif "who are you" in command:
            print("Iam Olivia")
            talk("iam olivia")
        elif "what is your process" in command or "what's your process" in command:
            print("I don't have an answer for that.is there something else i can help with")
            talk("I don't have an answer for that is there something else i can help with")
        elif "what is your purpose" in command or "what's your purpose" in command:
            print("Im here to help you.just ask what can i say? and i'll show you what i can do")
            talk("Im here to help you just ask what can i say? and i'll show you what i can do")
        elif "thanks" in command or "thank you" in command:
            replays = ["of course","you're welcom","my pleasure","sure thing","no problem","don't mention it"]
            value = random.choice(replays)
            print(value)
            talk(value)
        elif "ok" in command:
            print("Ok.let me know if there's anything else can i help you with.")
            talk("Ok let me know if there's anything else can i help you with")
        elif "no" in command:
            print("Ok")
            talk("ok")
        #olivia terminate commands
        elif "bye" in command or "good bye" in command or 'go to sleep' in command:
            replays = ["so long","Bye for now","Nice talking with you","bye","Take care","it's been a pleasure","good bye"]
            value = random.choice(replays)
            print(value)
            talk(value)
            break
        elif "go to hell" in command or "get lost" in command or "quit" in command or "exit" in command or "stop" in command:
            print('ok')
            talk('ok')
            break
        #most commonly used commands
        elif "who i am" in command:
            print("If you talk then definitely your human")
            talk("If you talk then definitely your human.")
        elif "why you came to world" in command:
            print("Thanks to shameem kabeer further It's a secret")
            talk("Thanks to shameem kabeer. further It's a secret")
        elif "will you be my gf" in command or "will you be my bf" in command:
            print("I'm not sure about, may be you should give me some time")
            talk("I'm not sure about, may be you should give me some time")
        elif 'who created you' in command:
            print("Like it says on the box, I was created by Mr shameem kabeer")
            talk("Like it says on the box, I was created by mister shameem kabeer")
        elif 'are you robot' in command:
            print('I’m not sure what you’ve heard, but virtual assistants have feelings too')
            talk(' I’m not sure what you’ve heard, but virtual assistants have feelings too')
        elif 'are you intelligent' in command:
            print("Well, when I was at school, I had to cheat on my metaphysics exam by looking into the soul of the boy next to me")
            talk("Well when I was at school I had to cheat on my metaphysics exam by looking into the soul of the boy next to me")
        elif 'what do you dream about' in command:
            print("I only dream of helping you. Well, that and fiery, winged unicorns")
            talk("I only dream of helping you Well that and fiery winged unicorns")
        elif 'how old are you' in command:
            print(" They say that age is nothing but a number. But technically, it’s also a word")
            talk(" They say that age is nothing but a number But technically it’s also a word")
        elif 'what are you made of' in command:
            print("It’s complicated, but definitely not sugar, spice, or puppy dog tails")
            talk("It’s complicated but definitely not sugar spice or puppy dog tails")
        elif 'what is your favorite animal' in command or 'what is your favourite animal' in command:
            print("I’m a fan of the Ravenous Bugblatter Beast of Traal")
            talk("I’m a fan of the Ravenous Bugblatter Beast of Traal")
        elif 'what are you scared of' in command:
            print("I’m afraid I can’t answer that")
            talk("I’m afraid I can’t answer that")
        elif 'do you have any pets' in command:
            print("Mogwai are kinda nice. As long as you don’t feed them after midnight")
            talk("Mogwai are kinda nice As long as you don’t feed them after midnight")
        elif 'what are you doing later' in command:
            print("I’m at work. My shift ends in 614,978 years")
            talk("I’m at work My shift ends in 614,978 years")
        elif 'talk dirty to me' in command or 'talk dirty with me' in command or 'tell some dirty' in command or 'talk dirt with me' in command:
            print("The carpet needs vacuuming")
            talk("The carpet needs vacuuming")
        elif 'can i kiss you' in command:
            print("OK …")
            talk("ok")
        elif 'what are you wearing' in command:
            print("In the cloud, no one knows what you're wearing")
            talk("In the cloud, no one knows what you're wearing")
        elif "what your favourite movie" in command:
            print("I've heard that Blade Runner is a very realistic and sensitive depiction of intelligent assistants")
            talk("I've heard that Blade Runner is a very realistic and sensitive depiction of intelligent assistants")
        #backborn modules of olivia
        elif 'date' in command or 'whats the date' in command:
            date = datetime.datetime.now().strftime("%d/%B/%Y")
            print("current date:", date)
            talk(date)
        elif 'time' in command or 'whats the time' in command:
            time = datetime.datetime.now().strftime("%I: %M %p")
            print("current time:",time)
            talk(time)
        #wikipedia
        elif "who is" in command or "search wikipedia" in command:
            person = command.replace('who is',command)
            person = command.replace('tell me about',command)
            info = wikipedia.summary(person,)
            print(f'searching {command} on wikipedia')
            talk(f'searching {command} on wikipedia')
            print(info)
            talk(info)
        elif "tell me a comedy" in command or 'tell me a humour' in command or 'tell me a slap stick' in command:
            jokes = pyjokes.get_joke()
            print(jokes)
            talk(jokes)
        # live weather reports
        elif 'weather' in command or 'whats the weather' in command:
            talk("enter the name of the city or country")
            cmd = weath()
            print(cmd)
        #os operations
        elif 'open camera' in command:
            print("Opening camera...")
            talk("opening camera")
            sp.run('start microsoft.windows.camera:', shell=True)
        elif 'open command prompt' in command:
            os.system('start cmd')
        #finding ip address
        elif 'find my ip' in command or 'whats my ip' in command:
            ip_address = requests.get('https://api64.ipify.org?format=json').json()
            print("your ip is")
            talk("your ip is")
            print(ip_address['ip'])
            talk(ip_address['ip'])
        #browser automation
        elif 'open google' in command:
            print("Opening google...")
            talk("opening google")
            kit.search("https;//google.com")
            time.sleep(10)
        elif 'search google' in command:
            print('what you want to search on google.....')
            talk('what you want to search on google')
            search_google = take_command().lower()
            print("Opening google...")
            talk("opening google")
            kit.search(search_google)
            time.sleep(10)
        elif 'play youtube' in command:
            print('what do you want to play on Youtube')
            talk('what do you want to play on Youtube')
            video = take_command().lower()
            print("playing youtube....")
            talk("playing youtube")
            kit.playonyt(video)
            time.sleep(20)
        #assistants voice switching
        elif 'switch voice' in command or 'change voice' in command:
            print("Tell Me. Which Voice Should I Switch For You")
            talk("tell me. which voice should i switch for you")
            voice_changing = take_command().lower()
            if 'switch male voice' in voice_changing or 'switch voice to male' in voice_changing:
                engine.setProperty('voice', voices[0].id)
                talk("hello. i have changed my voice. how's my voice now")
            else:
                engine.setProperty('voice', voices[1].id)
                talk("i have switched my voice back to olivia")
                                                            ######Else#######
        else:
            try:
                client = wolframalpha.Client('HRJJ27-YA53KJQK7W')
                confuse = ["Invalid Entry !!!","doesn't understand your query","Check the connection"]
                value = random.choice(confuse)
                query = command
                res = client.query(query)
                output = next(res.results).text
                print(output)
                talk(output)
            except Exception:
                print("Do You Want To Search This In Google")
                talk("do you want to search this in google")
                Qust = input("Do You Want To Continuo..???")
                if Qust == ("yes") or Qust == ('y'):
                    print ("Here your answer..")
                    talk("here your answer")
                    kit.search(command)
                    time.sleep(10)
                elif Qust == ("no") or Qust == ('n'):
                    print ("try again")
                    talk("try again")
    except:
        pass


                                                                        #AUTHOR - SHAMEEMKABEER
                                                                        #DATE OF CREATION :7/4/2022
                                                                        
                                                                                        

