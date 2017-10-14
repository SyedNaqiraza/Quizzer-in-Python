from Tkinter import *
from PIL import ImageTk, Image
import sqlite3
import unicodedata
class MyFirstGUI:
    def __init__(self, master):
        self.error = "Sorry you are not registered"
        self.conn = sqlite3.connect('UsersData.db')
        self.master = master
        master.title("Quiz Program")
        master.configure(background='RoyalBlue1')
        master.geometry("870x670")
        master.resizable(False, False)

        self.bar = Frame(root, relief=RIDGE, borderwidth=5)
        self.bar.pack(side=TOP)

        self.img = ImageTk.PhotoImage(Image.open("NUST.jpg"))
        self.icon_size = Label(self.bar)
        self.icon_size.image = self.img  # <== this is were we anchor the img object
        self.icon_size.configure(image=self.img)
        self.icon_size.pack()

        self.label = Label(master, text="Welcome to Online Quiz Platform",font=("Helvetica", 16),background='RoyalBlue1')
        self.label.pack()

        self.close_button = Button(master, text="Close Application", command=master.quit,font=("Helvetica", 8) )
        self.close_button.place(x=776,y=650)

        self.Submit = Button(master, text="Submit", command=self.information, font=("Helvetica", 8))
        self.Submit.place(x=330, y=330)

        self.User=Label(text="Username",font=("Helvetica", 12),background='RoyalBlue1')
        self.User.place(x=100,y=230)

        self.username = Entry(master)
        self.username.place(x=100,y=250,width=270,height=20)

        self.Pass=Label(text="Password",font=("Helvetica", 12),background='RoyalBlue1')
        self.Pass.place(x=100,y=275)

        self.password=Entry(master)
        self.password.place(x=100, y=300, width=270, height=20)

        self.text=Label(text="Not Registred ? Register as a student ", font=("Helvetica", 12),background='RoyalBlue1')
        self.text.place(x=600,y=180)


        self.Ruser=Label(text="Name(Username)",font=("Helvetica", 12),background='RoyalBlue1')
        self.Ruser.place(x=600, y=230)

        self.Rusername = Entry(master)
        self.Rusername.place(x=600, y=250, width=250, height=20)

        self.RPass = Label(text="Password", font=("Helvetica", 12), background='RoyalBlue1')
        self.RPass.place(x=600, y=275)

        self.Rpassword = Entry(master)
        self.Rpassword.place(x=600, y=300, width=250, height=20)

        self.RSubmit = Button(master, text="Submit", command=self.Rinformation, font=("Helvetica", 8))
        self.RSubmit.place(x=600, y=330)


        self.Warn = Label(text="Try with a different Username", font=("Helvetica", 12), background='RoyalBlue1')
        self.Caution = Label(text="FILL Both of the fields", font=("Helvetica", 12), background='RoyalBlue1')

        self.Error=Label(textvariable=self.error,font=("Helvetica", 12), background='RoyalBlue1')
        self.welcome=Label(text="Welcome Sir Shumayl ",font=("Helvetica", 12), background='RoyalBlue1')

        self.Schoice=Label(text="Choose one subject of which you want to make quiz ",font=("Helvetica", 12) ,background='RoyalBlue1')

        self.Sopt=Label(text="1 -Machine Learning 2-Advanced Programming",font=("Helvetica", 12) ,background='RoyalBlue1')

        self.Senter=Entry(master)

        self.Sbutton = Button(self.master, text="Enter", command=self.InstructorMode, font=("Helvetica", 8))


    def information(self):
        self.Username=self.username.get()
        self.Password=self.password.get()
        conn = sqlite3.connect('UsersData.db', timeout=39)
        c = conn.cursor()
        if (self.Username =="" or self.Password==""):
            self.Caution.place(x=200, y=355)

        else:
            c.execute('SELECT * FROM Users')
            String = c.fetchall()
            print String
            if (String==None):
                self.Error.place(x=600,y=355)
            else :
                    if (self.Username in String and self.Password in String):
                       self.Loginuser=self.Username
                       if (self.Username=='Shumayl'):
                           self.InstructorMode()
                       else:
                           self.StudentMode()
                    else:
                        loginerror="Sorry Username or Password is incorrect"
                        self.Error = Label(textvariable=loginerror, font=("Helvetica", 12), background='RoyalBlue1')
                        self.Error.place(x=600, y=355)

    def Rinformation(self):
        conn = sqlite3.connect('UsersData.db',timeout=39)
        c = conn.cursor()
        Rusername=self.Rusername.get()
        Rpassword=self.Rpassword.get()
        if (Rusername =="" or Rpassword==""):
            self.Caution.place(x=600, y=355)
        else:
            self.Caution.place_forget()
            while 1:
              check=0
              c.execute('SELECT * FROM Users')
              String=c.fetchall()
              if (c.fetchall()==None):
                 print "fun2"
                 c.execute("INSERT INTO Users VALUES (?, ?, ?);",
                       (Rusername, 'Student', Rpassword))
                 conn.commit()
              else:
                   print "FUN3"
                   lenofstr = len(String)
                   for i in range(0,lenofstr):
                     if (String[i][0]==Rusername):
                        self.Warn.place(x=600, y=355)
                        check=1
                        break
              if(check==0):
                    c.execute("INSERT INTO Users VALUES (?, ?, ?);",(Rusername, 'Student', Rpassword))
                    conn.commit()
                    self.Warn.place_forget()
                    break
              break
            conn.close()

    def InstructorMode(self):
        self.Submit.place_forget()
        self.User.place_forget()
        self.username.place_forget()
        self.Pass.place_forget()
        self.password.place_forget()
        self.text.place_forget()
        self.Ruser.place_forget()
        self.Rusername.place_forget()
        self.RPass.place_forget()
        self.Rpassword.place_forget()
        self.RSubmit.place_forget()
        self.Caution.place_forget()


        self.welcome.place(x=10,y=40)
        self.Schoice.place(x=10,y=160)
        self.Sopt.place(x=10,y=180)
        self.Senter.place(x=10,y=210)
        self.Sbutton.place(x=40,y=230)

    def InstructorInfo(self):
            print "A"
    def StudentMode(self):
        self.Submit.place_forget()
        self.User.place_forget()
        self.username.place_forget()
        self.Pass.place_forget()
        self.password.place_forget()
        self.text.place_forget()
        self.Ruser.place_forget()
        self.Rusername.place_forget()
        self.RPass.place_forget()
        self.Rpassword.place_forget()
        self.RSubmit.place_forget()
        self.Caution.place_forget()

        self.LoginUser=Label(text="Logged In",font=("Helvetica", 12),background='RoyalBlue1')
        self.LoginUser.place(x=760, y=30,)

        conn = sqlite3.connect('UsersData.db', timeout=39)
        c = conn.cursor()
        c.execute('SELECT * FROM MCQS')
        data = c.fetchall()
        if data:
            Sorry=Label(text="Right Now no Test is made by Instructor Sorry, Try next time ",font=("Helvetica", 12),background='RoyalBlue1')
            Sorry.place(x=250,y=200)
        else:
            Choose=Label(text="Choose From Above",font=("Helvetica", 12),background='RoyalBlue1')
            Options=Label(text="1.Machine Learning\n\n 2.Advance Programming",font=("Helvetica", 12),background='RoyalBlue1')
            Options.place(x=50,y=150)
            self.Ans.place(x=80,y=210)
            self.OptAns=self.Ans.get()
            print self.OptAns
            self.optans.place(x=96, y=250)
        conn.close()
    def startquiz(self):
        if self.OptAns==1:
            print "A"
        if self.OptAns==2:
           print "A"
if __name__ == '__main__':
 root = Tk()
 my_gui = MyFirstGUI(root)
 root.mainloop()
