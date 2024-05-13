from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        # creating database object
        self.dbo=Database()
        self.apio=API()

        # loading GUI login

        self.root=Tk()                                  # tk() is the main class inside tkinter,self.root ek variable jis main hum tk() class k object ko store karte hai.
        self.root.title("T App")                       # title of the GUI
        self.root.iconbitmap('resources/favicon.ico')   # image of the GUI
        self.root.geometry('350x600')                   # weidth and height of the GUI
        self.root.config(bg='#273746')                  # background colour or can be used hexcode for color
        self.login_gui()
        self.root.mainloop()                            # hold the GUI on the screen orelse it stay for a fraction of time and disapear

    def login_gui(self):

        self.clear()

        heading=Label(self.root,text='T App',bg='#273746',fg='white')  # self.root-->  you have to tell ye label->konse object k through GUI pe place ho raha hai


        heading.pack(pady=(30,30))                                      # GUI has geometric manager that allow to write/display/place these thing on the GUI/on the interface
                                                                        # two type of geometric manager-->pack(we use this coz inteligent ),grid
                                                                        # pady--->(upar,niche)upar se kitna aur niche se kitna gap chaiea

        heading.config(font=('verdana',24,'bold',))                     # font styleing

        label1=Label(self.root,text='Enter Email',bg='#273746',fg='white')
        label1.pack(pady=(10,10))

        # entry is a class
        # we use self--> coz is variable ko hamare class k dusre method use karenge
        # aur dusro ko jismain nahi hai usko srif es method main use kara jaega
        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)  # ipady for height of the input





        label2=Label(self.root,text='Enter Password',bg='#273746',fg='white')
        label2.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=30,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)






        # we use button class
              # in buttn class we can provide height
        login_btn=Button(self.root,text='Login',bg='#707B7C',fg='white',width=10,height=1,command=self.perform_login)
        login_btn.pack(pady=(10,10))




        label3=Label(self.root,text="Not a member ?",bg='#273746',fg='white')
        label3.pack(pady=(20,7))


        redirect_btm=Button(self.root,text="Register",bg='#707B7C',fg='white',width=11,height=1,command=self.register_gui)
        redirect_btm.pack(pady=(7,10))                                                              # here when the register buttom get clicked,
                                                                                                    # its command transfer/call the to register function below
    def register_gui(self):
        self.clear()

        # now we will create a interface of register
        heading = Label(self.root, text='T App', bg='#273746', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold',))
# for name
        label0 = Label(self.root, text='Enter Name', bg='#273746', fg='white')
        label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=4)

# for email
        label1 = Label(self.root, text='Enter Email', bg='#273746', fg='white')
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=4)

# for passward
        label2 = Label(self.root, text='Enter Password', bg='#273746', fg='white')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

# for register buttom
        register_btn = Button(self.root, text='Register', bg='#707B7C', fg='white', width=10, height=1,command=self.perform_registration) # when i hit register open this function
        register_btn.pack(pady=(10, 10))

# for already member
        label3 = Label(self.root, text="Already a member !", bg='#273746', fg='white')
        label3.pack(pady=(20, 7))

        redirect_btm = Button(self.root, text="Login now", bg='#707B7C', fg='white', width=11, height=1,command=self.login_gui)
        redirect_btm.pack(pady=(7, 10))





    def clear(self):      # as we need to clear every time so we put it into a separate function so that can be used anytime
        # now our work is to clear our old gui means log in gui
        for i in self.root.pack_slaves():  # pack slaves means it gather all the elemets of that method(all the button and lebel)
            i.destroy()

    def perform_registration(self):
        # fetch data from gui

        name=self.name_input.get()
        email=self.email_input.get()
        passward=self.password_input.get()

        response=self.dbo.add_data(name,email,passward)
        if response:
            messagebox.showinfo('Sucsess',"Registration Successful . you can login now ")
        else:
            messagebox.showerror("Error","Email already exist")



    def perform_login(self):
        email=self.email_input.get()
        passward=self.password_input.get()

        response=self.dbo.search(email,passward)
        if response:
            messagebox.showinfo('Sucess','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Email/Passward')



    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='T App', bg='#273746', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold',))

        sentiment_btn=Button(self.root,text='Sentiment Analysis',bg='#EAECEE',fg='black',width=30,height=3,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(40,10))

        ner_btn = Button(self.root, text='Named Entity Recognition', bg='#EAECEE', fg='black', width=30, height=3,command=self.Named_Entity_Recognition)
        ner_btn.pack(pady=(20, 10))

        emotion_btn = Button(self.root, text='Syntax Analysis', bg='#EAECEE', fg='black', width=30, height=3,command=self.Syntax_Analysis)
        emotion_btn.pack(pady=(20, 10))

        logout_btm = Button(self.root, text="Logout now", bg='#707B7C', fg='white', width=11, height=1,command=self.login_gui)
        logout_btm.pack(pady=(30, 10))


    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='T App', bg='#273746', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold',))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#273746', fg='white')
        heading2.pack(pady=(20, 20))
        heading2.config(font=('verdana', 20, ))

        label1 = Label(self.root, text='Enter The Text', bg='#273746', fg='white')
        label1.pack(pady=(10, 10))
        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=13)

        sentiment_btn = Button(self.root, text='Analyze sentiment', bg='#707B7C', fg='white', width=14, height=2,command=self.do_sentiment_analyis)
        sentiment_btn.pack(pady=(17, 10))

        self.sentiment_result = Label(self.root, text='', bg='#273746', fg='white')
        self.sentiment_result.pack(pady=(30, 30))




        goback_btn = Button(self.root, text='Go Back', bg='#707B7C', fg='white', width=14, height=2,command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analyis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentimental_analyis(text)
        txt=''
        for i in result:
            txt=txt+i + ' --> ' + str(result[i]) +'\n'
        self.sentiment_result['text'] =txt


    def Named_Entity_Recognition(self):
        self.clear()

        heading = Label(self.root, text='T App', bg='#273746', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold',))

        heading2 = Label(self.root, text='NER', bg='#273746', fg='white')
        heading2.pack(pady=(20, 20))
        heading2.config(font=('verdana', 20,))

        label1 = Label(self.root, text='Enter The Text', bg='#273746', fg='white')
        label1.pack(pady=(10, 10))
        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=13)

        ner_btn = Button(self.root, text='recognize entity', bg='#707B7C', fg='white', width=14, height=2,
                               command=self.do_ner)
        ner_btn.pack(pady=(17, 10))

        self.ner_result = Label(self.root, text='', bg='#273746', fg='white')
        self.ner_result.pack(pady=(30, 30))

        goback_btn = Button(self.root, text='Go Back', bg='#707B7C', fg='white', width=14, height=2,
                            command=self.home_gui)
        goback_btn.pack(pady=(10, 10))



    def do_ner(self):
        text=self.ner_input.get()
        result=self.apio.ner(text)
        txt=''
        for x in result:
            txt+=x+"\n"
        self.ner_result['text'] =txt



    def Syntax_Analysis(self):
        self.clear()

        heading = Label(self.root, text='T App', bg='#273746', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 24, 'bold',))

        heading2 = Label(self.root, text='Syntax Analysis', bg='#273746', fg='white')
        heading2.pack(pady=(20, 20))
        heading2.config(font=('verdana', 20,))

        label1 = Label(self.root, text='Enter The Text', bg='#273746', fg='white')
        label1.pack(pady=(10, 10))
        self.syntax_analysis_input = Entry(self.root, width=50)
        self.syntax_analysis_input.pack(pady=(5, 10), ipady=13)

        syntax_analysis_btn = Button(self.root, text='Fetch Syntax', bg='#707B7C', fg='white', width=14, height=2,
                         command=self.do_syntax_analysis)
        syntax_analysis_btn.pack(pady=(17, 10))

        self.syntax_analysis_result = Label(self.root, text='', bg='#273746', fg='white')
        self.syntax_analysis_result.pack(pady=(30, 30))

        goback_btn = Button(self.root, text='Go Back', bg='#707B7C', fg='white', width=14, height=2,
                            command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_syntax_analysis(self):
        text=self.syntax_analysis_input.get()
        result=self.apio.syntax_analysis(text)
        self.syntax_analysis_result['text']=result




nlp=NLPApp()
