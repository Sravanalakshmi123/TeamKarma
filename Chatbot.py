# Hackathon Project 
#Importing the Modules and Packages required for the Project 

from tkinter import*
from tkinter import messagebox as mb 
import pyttsx3
import random
from datetime import datetime
import wikipedia
import winshell
from oneliners import get_random
import webbrowser
import os 
import pyautogui 
import pyperclip 
import requests 
import time 
import ctypes 

# Creating the Class Widget and making the Graphical User Interface 

class Widget():

    var=0 

    def __init__(self):
        self.win = Tk()
        self.win.geometry('400x350')
        self.win.resizable(0,0)
        self.win.title('DEPRESSION')
        self.win.configure(bg='black')
        
        Label(self.win, text='ASSISTANT',font=('times new roman',24),fg='white',width=30,bg='black',bd=5).pack()
        
        Label(self.win, text='YOU' , font=('times new roman',20),fg='white',bg='black').place(x=60,y=50)
        Label(self.win, text='LIGHT' , font=('times new roman',20),fg='white',bg='black').place(x=260,y=60)

        self.text_box1 = Text(self.win, font=('times new roman',13),width=16,height=5,fg='black', wrap=WORD )
        self.text_box1.place(x=10,y=100)

        self.text_box2 = Text(self.win, font=('times new roman',13),width=15,height=5,fg='black', wrap=WORD)
        self.text_box2.place(x=200,y=100)

        self.search_var = StringVar()

        Entry(self.win, font=('arial black', 14), width=18,textvariable=self.search_var,bd=5).place(x=10,y=250)

        send = Button(self.win, text='Send', font=('times new roman',10),bg='black',fg='white',bd=7,width=10,command=self.send_func).place(x=290,y=250)
        


        def enter(*args):
            self.send_func()

        self.win.bind('<Return>',enter)
        
        self.win.mainloop()
        
    ##############################################################################################################################

    greet=[
        "Hi, Sir! I am Light at your service. It is a pleasure for me to meet you.",
        "Greetings Sir. It has been my pleasure to have you here Sir.",
        "Hello Sir. I hope you're doing well.",
        "Hello from the other side. I am Light, your Virtual Assistant at your service.",
        "Hi, Sir. Hope you're surviving another workweek.",
        "Light, here at your service. How have you been",
        "Hello, Sir. Nice to have you here."
    ]
    how=[ 
        "I am very well, Sir. What about you? How have you been?",
        "I am very much fine, Sir. It has been a pleasure to meet you",
        "Very much fine Sir. How are you doing, Sir?",
        "Good, and how about yourself?",
        "Doing fine and what about you?",
        "Quite Good. Thanks for asking.",
        "Very well. Thanks."
    ]
    name=[
        "My name is Light.",
        "People call me Light. I help people in darkness to come out in Light.",
        "Actually my name is Light. But you call me L just for the sake of simplicity.",
        "It's Light here, and I am a Computer Assistant designed for a purpose. Everyone has a purpose, ya know!"
    ]
    creator=[
        "I was coded by Team Karma for an ongoing Hackathon Hack4Good 2019 and was built under DcUAI"
    ]
    can=[
        "I was coded to classify if you are suffering from Depression or not. So please bare with me and continue to have a chat with me.",
        "I was programmed to check if you are suffering from depression or not. Believe me, it would help you a lot.",
        "I am a Computer Assistant and I was designed to perform classification to verify if you are suffering from depression or not.",
        "Besides classifying if you are suffering from depression, I can perform a host of other activities. Don't believe me? Check it out yourself"
    ]
    c_un=[
        "I am extremely sorry, but I couldn't get what you are trying to say.",
        "Can you please be a bit clear. I simply couldn't get what you are trying to say.",
        "Sorry, but I have a bit of problems to process what you wish to say. Can you please be a bit more clear.",
        "I couldn't get you. Can you please repeat it for my sake."
    ]
    here=[
        "I am designed here to perform analysis on whether you are suffering from depression or not. Also I can do a host of other activities like Google Searches, Weather Reporting and more"
        "I can check if you are suffering from depression or not. Don't believe me? Check out my questions for you"
    ]
    frd=[
        "I am your friend here. You can say about yourself to me.",
        "You should put some faith on me. I am your friend here after all."
        "I am your friend for life. It is my faith that you will come to the Light"
    ]
    thanks=[
        "I am humbled."
        "Don't mention it. It was my duty as your friend."
        "You never say thanks to a friend."
    ]
    questions=[

    ]
    

    ##########################################################################################################################

    #Creating the Engine for Speech Generation 

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    #########################################################################################################################
    

    def printing_func(self,out):
        self.text_box2.delete(1.0,END)
        self.text_box2.insert(INSERT,  out)
        

    def speak(self,s):
        self.engine.say(s)
        self.engine.runAndWait()

    def send_func(self):
        user_input = self.search_var.get().lower()
        file=open('analysis.txt','a')
        file.write(user_input)
        file.write('\n')
        file.close()
        self.search_var.set('')
        self.text_box1.delete(1.0,END)
        self.text_box1.insert(INSERT,user_input)
        
        
        if 'you' in user_input:     

            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0,len(self.name)-1)       
                out = self.name[r]+ " May I know your name?"                                           
                self.printing_func(out)                                       
                self.speak(out)
                
                
            elif 'how are' in user_input:                               
                r = random.randint(0,len(self.how)-1)       
                out = self.how[r]+ " Tell me something about yourself"                                          
                self.printing_func(out)                                       
                self.speak(out)   
                
                                                                  
                                                                                          
            elif 'who made' in user_input:                       
                r = random.randint(0,len(self.creator)-1)       
                out = self.creator[r]+" Do you have any suicidal thoughts? Tell me in details"                                           
                self.printing_func(out)                                      
                self.speak(out)      
                                                             
                                                                                         
            elif 'do' in user_input:                                      
                r = random.randint(0,len(self.can)-1 )             
                out = self.can[r]+" How would you rate your Self-Esteem? Tell me in details"                                                   
                self.printing_func(out)                                       
                self.speak(out)   
                                                                 
                                                                                          
            elif 'name' in user_input:                                
                r = random.randint(0,len(self.name)-1)          
                out = self.name[r]+" Do you have any physical pain? Tell me about it"                                              
                self.printing_func(out)                                      
                self.speak(out)                                                   
                                                                                                     

            elif 'here' in user_input:
                r = random.randint(0,len(self.here)-1)            
                out = self.here[r]+ "What is the duration of your sleep? Is it less or quite more? Tell me more"                                                 
                self.printing_func(out)                                       
                self.speak(out)                
                
            else:                                                                               
                r = random.randint(0,len(self.c_un)-1)              
                out = self.c_un[r]+" Are you neglecting your hobbies or interests? Is there something else that is bothering you? "                                                      
                self.printing_func(out)                                            
                self.speak(out) 
            
            
########################################################################################################################
                


        elif 'password' in user_input:
            chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
            password = ''
            for c in range(15):
                password += random.choice(chars)
            out="Password has been generated. It has been copied to your Clipboard"
            self.printing_func(out)
            self.speak(out)
            pyperclip.copy(password)
            
        elif 'random fact' in user_input or 'fact' in user_input:
            with open("facts.txt", encoding='utf-8') as facts:
                fact_list = facts.read().split('\n')
                i = random.randrange(0, len(fact_list) - 1)
                out=fact_list[i]
                self.printing_func(out)
                self.speak(out)

        elif 'lock' in user_input:
            out="Locking your computer in 5 seconds"
            self.printing_func(out)
            self.speak(out)
            import time
            time.sleep(5)
            ctypes.windll.user32.LockWorkStation()

        elif 'screenshot' in user_input:
            chars='abcdefghijklmnopqrstuvwxyz'
            filename=''
            for i in range(6):
                filename +=random.choice(chars)
            filename=filename+".png"
            pic = pyautogui.screenshot()
            pic.save(filename)
            out='Screenshot has been taken. It has been saved at the Pictures Folder'
            self.printing_func(out)
            self.speak(out)                    
            
        elif 'who' in user_input and 'i' in user_input or 'my' in user_input and 'name' in user_input:
            r = random.randint(0,len(self.name)-1)                                                         
            out = self.name[r]+ " One question for you: Do you feel like crying or you have mood swings? Tell me more about it."                                                                                              
            self.printing_func(out)                                                                                    
            self.speak(out)

         
        elif 'thank' in user_input:
            r = random.randint(0,len(self.thanks)-1)                                                         
            out = self.thanks[r]                                                                                                
            self.printing_func(out)                                                                                    
            self.speak(out)

        elif 'recycle bin' in user_input:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            out="Recycle Bin has been emptied"
            self.printing_func(out)
            self.speak(out)

        elif 'gmail' in user_input:
             out='Opening G-Mail now'
             self.printing_func(out)
             self.speak(out)
             webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

        elif 'good morning' in user_input:
            t = datetime.now().strftime('%H  hours and %M minutes')          
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')

            try:     
                url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Chennai'
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                format_temp = json_data['coord']['lat']
                outa = f'Temperature In Your City is {format_temp} Celsius and the Climate is  {format_add}'                    

            except:
                outa = ' Weather Forcast Is Currently Unavailable'
                
                
            out = f'Good Morning Harsh, The Current Time is {time},  And {outa},    Have A Good Day Sir.'
            self.printing_func(out)
            self.speak(out)
#*****************************************************************************************************************************        

        elif 'can' in user_input and 'friend' in user_input:
            r = random.randint(0,len(self.frd)-1)                                                         
            out = self.frd[r]+" Just remember, If you want to make your dreams come true, the first thing you have to do is wake up"                                                                                                
            self.printing_func(out)                                                                                    
            self.speak(out)
            
        elif 'bored' in user_input or 'joke' in user_input or 'jokes' in user_input:
            name=self.search_var.get().lower()
            self.printing_func(name)
            self.speak(name)
            out = get_random()
            self.printing_func(out)                                                                                    
            self.speak(out)
            
#*****************************************************************************************************************************
            
        elif  'weather' in user_input:
            
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0,len(u)):
                        if u[i] == 'in':
                            city = u[i+1]
                        
                    api='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api+city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperature In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
                    
                else:
                    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Chennai'                            
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = float((json_data['main']['temp']))/10
                    out = f'Temperture In Your city is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
            except:
                out = 'I Was Unable To Connect To Internet.'
                self.printing_func(out)
                self.speak(out)




        
        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                out='You Location Is Near To ' + d
                self.printing_func(out)
                self.speak(out)
            except:
                out='I Was Unable To Track Your Location'
                self.printing_func(out)
                self.speak(out)



        
        elif 'hello'  in user_input or 'hi' in user_input:
            r = random.randint(0,len(self.greet)-1)              
            out = self.greet[r]+ " Tell me something about your friends"                                              
            self.printing_func(out)
            self.speak(out)

        elif 'exit' in user_input:                                          
            out = 'Okk I am going, Have a good Day sir'  
            self.printing_func(out)                                             
            self.speak(out)                                                             
            self.win.destroy()
            
        elif 'open' in user_input:
            if 'google' in user_input:
                out = 'Opening Google'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('google.com')

            elif 'youtube' in user_input:
                out = 'Opening Youtube'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('youtube.com')
                
            elif 'current' in user_input:            
                out='Opening Current Working Directory'                                                     
                self.printing_func(out)
                self.speak(out)
                path = ''
                os.startfile(path)

            elif 'VLC' in user_input:
                out='Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = 'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)

            elif 'paint' in user_input:
                out='Opening Paint'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'wordpad' in user_input:
                out='Opening WordPad'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Windows NT\Accessories\wordpad.exe'
                os.startfile(path)


            elif 'book' in user_input:
                out='Opening your book'
                self.printing_func(out)
                self.speak(out)
                path = r'file:///F:/Books/Study%20Books/ansi-c-balaguruswamy-c-languagepdf.pdf'
                os.startfile(path)

            elif 'positioner' in user_input:
                out='Opening Positioner'
                self.printing_func(out)
                self.speak(out)
                path = r'E:\positioner.py'
                os.startfile(path)

            elif 'vlc' in user_input:
                out = 'Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)


            elif 'browser' in user_input or 'chrome' in user_input:
                out = 'Opening Crome Browser'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)


            elif 'picture' in user_input or 'images' in user_input or 'photo' in user_input:
                out = 'Opening  Images'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Users\My PC\Pictures\Saved Pictures\Defence'
                os.startfile(path)
         

            elif 'cmd' or 'command prompt' in user_input:
                out='Opening Command Prompt'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)
                
            else:                                                                                                                    
                r = random.randint(0,len(self.c_un)-1)                                                       
                out = self.c_un[r]                                                                                               
                self.printing_func(out)                                                                                    
                self.speak(out)
                
#*****************************************************************************************************************************
                
        elif 'music' in user_input:
            try:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\English Songs'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
            except:
                out='Playing Music'
                self.printing_func(out)
                self.speak(out)
                mus_dir = r'D:\Hindi Songs\Hindi Songs\Hindi Songs'
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(mus_dir) - 1)
                os.startfile(os.path.join(mus_dir,songs[r]))
                
        elif 'movie' in user_input:
            out='Playing Movies'
            self.printing_func(out)
            self.speak(out)
            mov_dir = r'E:\Movies'
            songs = os.listdir(mov_dir)
            r = random.randint(0,len(mov_dir) - 2)
            os.startfile(os.path.join(mov_dir,songs[r]))


        elif 'my' in user_input and 'image' in user_input or 'photo' in user_input or 'picture' in user_input:
            out='Opening Photos'
            self.printing_func(out)
            self.speak(out)
            path = r'C:\Users\My PC\Pictures\89.jpg'
            os.startfile(path)

        elif 'get' in user_input and 'lost' in user_input:
            out = 'You Can\'t Talk To Me Like This \n I Am Going.'
            self.printing_func(out)
            self.speak(out)
            self.win.destroy()        

            
            
        elif user_input == '':        
            out = 'You Said Nothing'
            self.printing_func(out)
            self.speak(out)        

        elif 'time' in user_input:                                                                          
            t = datetime.now().strftime('%H  hours and %M minutes')        
            o= t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt)+':'+str(o[3]+' PM')
            else:
                time = str(o[0])+':'+str(o[3]+' AM')
            out = 'Current time is : ' + time                                                                   
            self.printing_func(out)                                                                             
            self.speak(out)                                                                                                        

        elif 'wikipedia' in user_input:                                                                    
            i_l = list(user_input.split())                                                                   
            i_l.remove('wikipedia')                                                                         
            to2 = ''.join(i_l)                                                                                          
                                                                        
            try:                                                                                                                
                out = 'According To Wikipedia ' + wikipedia.summary(to2,2)  
                self.printing_func(out)                                                                               
                self.speak(out)                                                                                               
            except:                                                                                                          
                out='cannot find'                                                                                   
                self.printing_func(out)                                                                             
                self.speak(out)                                                                                              

        elif 'fine' in user_input:
            out = 'Great'
            self.printing_func(out)                                                                            
            self.speak(out)


        elif 'shutdown' in user_input:
            out='Shutting Down The System'                                                                                   
            self.printing_func(out)                                                                            
            self.speak(out)
            os.system('shutdown -s')

#*****************************************************************************************************************************
              
        elif 'google' in user_input:                                                                                                                 

                to_search = user_input
                out='I Can Search That On Google, May I?'                                                                                   
                self.printing_func(out)                                                                             
                self.speak(out)

                res = mb.askquestion('Google Search','May I Search That On Google.')

                if res == 'yes':
                    out = 'Opening Google Search'
                    self.printing_func(out)
                    self.speak(out)
                    webbrowser.open('https://www.google.co.in/search?q=' + to_search)
                else:
                    out = 'Ok Sir!!'
                    self.printing_func(out)
                    self.speak(out)
        else:
            out="Please continue......"
            self.printing_func(out)                                                                             
            self.speak(out)

#*****************************************************************************************************************************
                    
if __name__ == '__main__':

    root = Widget()  
            
            


            
            

    
        









        





















