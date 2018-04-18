from __future__ import print_function
import smtplib
from tkinter import *
import numpy as np
from tkinter import ttk 
import tkinter 
import tkinter as tk
import time
import datetime
import urllib
import urllib.request as ur
from urllib.error import URLError, HTTPError
import sys

import os
import schedule
import logging
import logging.config
import threading
import  tkinter.messagebox
import random
import textwrap
import glob
import logging.handlers
import csv
import socket
from twilio.rest import Client
from collections import defaultdict
try:
    import Tkinter as tk
    import Queue as qu
except ImportError:
    import tkinter as tk
    import queue as qu
now = datetime.datetime.now()
l=now.strftime("%Y ")
l=l+now.strftime("%m ")
l=l+now.strftime("%d ")
socket.getaddrinfo('localhost', 8080)  
logging.basicConfig(filename='{0}_logfile.log'.format(l),level=logging.DEBUG)

from email.mime.text import MIMEText
APP_TITLE = "Mail Automation"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 500
APP_HEIGHT = 300
UPDATE_TIME = 1000 # Milliseconds

QUEUE_SIZE = 500
POLLING_TIME = 1000
from email.mime.text import MIMEText
global tri
global bac
tri=0
bac=0
space=0
#-----fetching email from list-----#
class mainwindow(object):
    ls=[]     #recevier emailids
    lt=[]     #recevier names
    xs=[]     #signin emailids
    ys=[]     #signin passwords
    lg=[]     #sample emailids
    lh=[]     #sample names
    vs=[]
    count1=10
    readls=[] #recevier emailids
    readlt=[] #recevier names
    readxs=[] #signin emailids
    readys=[] #signin passwords
    readlg=[] #sample emailids
    readlh=[] #sample names
    readvs=[]
    report=[]
    c=[]
    ar=0
    imr=0
    br=0
    cr=0 
    def  __init__(self):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global l
        global cr
        global xs
        global count
        columns = defaultdict(list) 
        
        g= open('EnterSampleEmails.txt','r')
        gr=g.read()
        lg = gr.split(",")    #reading sampleemails from files and appending on to a list
        mainwindow.readlg.append(lg)
        time.sleep(3)
        h=open("EnterSampleNames.txt",'r')
        th=h.read()
        lh=th.split(",")
        mainwindow.readlh.append(lh)
        time.sleep(3)
        v=open('EnterIDs.txt','r')#inquotes
        vr=v.read()
        vs =vr.split(",")
        mainwindow.readvs.append(vs)
        time.sleep(3)
        x=open('EntersigninEmailID.txt','r')#inquotes
        xr=x.read()
        xs = xr.split(",")
        mainwindow.readxs.append(xs)
        time.sleep(3)
        y=open('EntersigninEmailPassword.txt','r')#inquotes
        yr=y.read()
        ys = yr.split(",")
        mainwindow.readys.append(ys)
        time.sleep(3)
        s= open('EnterRecevierEmails.txt','r')
        sr=s.read()
        ls = sr.split(",")
        mainwindow.readls.append(ls)
        time.sleep(3)
        t=open("EnterRecevierNames.txt",'r')
        tr=t.read()
        lt=tr.split(",")
        mainwindow.readlt.append(lt)
        time.sleep(3)
        count=0
        for i in range(0,1):
            for j in range(0,10):
                if(mainwindow.readlt[i][j]!='\0'):
                    count=count+1
        count1=count
        
        # c= open('Entersubject.txt','r')
        # cr=c.read()#inquotes
        # mainwindow.readcr.append(cr)
        # time.sleep(3)
        # a = open('EntertheHTMLPart-I.txt','r')
        # ar=a.read()
        # mainwindow.readar.append(ar)
        # time.sleep(3)
        # im= open('EnterImagePart.txt','r')
        # imr=im.read()
        # mainwindow.readimr.append(imr)
        # time.sleep(3)
        # b= open('EntertheHTMLPart-II.txt','r')
        # br=b.read()
        # mainwindow.readbr.append(br)
        # time.sleep(3)
        # for i in range(len(mainwindow.readlg)):
        #     mainwindow.lg.append(mainwindow.readlg[i].replace("?",""))
        # for i in range(len(mainwindow.readlh)):
        #     mainwindow.lh.append(mainwindow.readlh[i].replace("?",""))
        # for i in range(len(mainwindow.readxs)):
        #     mainwindow.xs.append(mainwindow.readxs[i].replace("?",""))
        # for i in range(len(mainwindow.readys)):
        #     mainwindow.ys.append(mainwindow.readys[i].replace("?",""))
        # for i in range(len(mainwindow.readvs)):
        #     mainwindow.vs.append(mainwindow.readvs[i].replace("?",""))
        # for i in range(len(mainwindow.readlt)):
        #     mainwindow.lt.append(mainwindow.readlt[i].replace("?",""))
        # for i in range(len(mainwindow.readls)):
        #     mainwindow.ls.append(mainwindow.readls[i].replace("?",""))
        
        secondmain()
#-----checks for internet connection-----#        
    def internetcheck(self):
        try:
            ur.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
            return True
        except ur.URLError as err:
            return False
    
#------first page of gui------# 
class secondwindow(mainwindow):
    def __init__(self,master):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        global ment
        numberentry=0
        codeentry=0
        self.g=open('quotesone.txt','r',encoding="utf8")
        self.gr=self.g.read()
        prop = self.gr.split("||")
        quote=random.choice(prop)
        self.master = master
        self.hdr_frm_r = tk.Frame(self.master, background='yellow', width=600, height=50)
        self.hdr_frm_r.grid(column=2, row=0 , columnspan= 10)
        self.intruction = Label(self.hdr_frm_r , text='MAIL AUTOMATION',font='Italic 25 bold',fg="green")
        
        self.intruction.grid(row=0, column=2, sticky=W)
        
        self.image = tk.PhotoImage(file="image.gif")
        self.label = tk.Label(image=self.image)
        self.label.grid(row=1,column=1)
        #self.title = Label(self.master, text='Mail Automation',font='Italic 15 bold',fg="black")
        
        #self.title.grid(row=1, column=2, sticky=W)
        self.name = Label(self.master, text='ON TIME   :',font='Helvetica 13 bold')
        self.name.grid(row=1,column=2,sticky=N)
        self.Sample= Button(self.master, text='Sample',command=samplepath,bg="blue",fg="white")
        self.Sample.grid(row=1,column=3,sticky=W+N)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=4,column=2)
        self.Actual= Button(self.master, text='Regular',command=self.receviernumber1,bg="blue",fg="white") 
        self.Actual.grid(row=1, column=4,sticky=W+N)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=6,column=2)
        self.name2 = Label(self.master, text='SCHEDULE :',font='Helvetica 13 bold')
        self.name2.grid(row=1,column=2,sticky=S)
        self.Sample= Button(self.master, text='Regular',command=self.receviernumber2,bg="blue",fg="white")
        self.Sample.grid(row=1,column=3,sticky=W+S)
        self.btn_frm_r = tk.Frame(self.master, background='yellow', width=600, height=50)
        self.btn_frm_r.grid(column=0, row=8 , columnspan= 10)
        self.name1 = Label(self.btn_frm_r, text=textwrap.fill(quote, 50),font='Helvetica 13 bold')
        self.name1.grid(column=0,row=8)
#------ receviernumber1 is for getting  Recevier Number and code for sending mail in ACTUAL mode---#  
    def receviernumber1(self):
        global numberentry
        global codeentry
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        roots=Tk()
        self.k = 500 
        self.s = 200
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        roots.title("Mail Automation") 
        self.receviernumber = Label(roots, text='Recevier Number :',font='Helvetica 10 bold')
        self.receviernumber.grid(row=2)
        self.code = Label(roots, text='Specific Code     :',font='Helvetica 10 bold')
        self.code.grid(row=3)
        self.sub= Label(roots, text='Subject              :',font='Helvetica 10 bold')
        self.sub.grid(row=4,sticky=N)
        secondwindow.numberentry= tk.Entry(roots)
        secondwindow.numberentry.grid(row=2, column=1,sticky=W)
        secondwindow.codeentry= tk.Entry(roots)
        secondwindow.codeentry.grid(row=3, column=1,sticky=W)
        secondwindow.subjectentry=tk.Text(roots,width = 20, height=4, font=("Helvetica 12 bold "))
        secondwindow.subjectentry.grid(row=4,column=1)
        self.B1=Button(roots, text=" Start ",bg="blue",fg="white",command=actualpath
            ).grid(row=5,column=1)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()
#------ receviernumber2 is for getting  code for sending mail in scheduled mode---#          
    def receviernumber2(self):
        global numberentry
        global codeentry
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        roots=Tk()
        self.k = 500 
        self.s = 150
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        roots.title("Mail Automation") 
        self.code = Label(roots, text='Specific Code :',font='Helvetica 10 bold')
        self.code.grid(row=3)
        self.sub= Label(roots, text='Subject :',font='Helvetica 10 bold')
        self.sub.grid(row=4,sticky=N)
        secondwindow.code= tk.Entry(roots)
        secondwindow.code.grid(row=3, column=1)

        secondwindow.subjectentry1=tk.Text(roots,width = 20, height=4, font=("Helvetica 12 bold "))
        secondwindow.subjectentry1.grid(row=4,column=1)
        self.B1=Button(roots, text=" Start  ",bg="blue",fg="white",command=main#main is at end  main will allocate seperate root schedule function 
            ).grid(row=5,column=1)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()
#---------schedule function is to get sending day and time ------#
    def schedule(self):
        self.k = 600
        self.s = 150 
        self.wk = self.winfo_screenwidth() 
        self.hw = self.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        self.title("Mail Automation") 
        tk.Label(self, text="Welcome to Mail Automation Application",font='Italic 13 bold',fg="black").grid(column=1, row=1, sticky=W)
        self.receviernumber = Label(self, text='Enter Sending Day In Three Letters:')
        self.receviernumber.grid(row=2)
        self.code = Label(self, text='Enter Sending Time')
        self.code.grid(row=3)
        secondwindow.numberentry= tk.Entry(self)
        secondwindow.numberentry.grid(row=2, column=1,sticky=W)
        secondwindow.codeentry= tk.Entry(self)
        secondwindow.codeentry.grid(row=3, column=1,sticky=W)
        self.text=tk.Label(self)
        self.text.grid(row=4,column=1)
        self.B1=Button(self, text=" Start  ",bg="blue",fg="white",command=scd#--this takes to scd to schedule those time
            ).grid(row=5,column=1,sticky=W)
        self.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
#----------Thread for Sample--------        
class AppThread(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join()
#-------Sample class-------         
class Sample(tk.Frame,mainwindow):

    def __init__(self,parent):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        logging.debug('Selected Sample Option')
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        parent.title("Mail Automation")
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        self.subjecth=Label(self.frame_head,text='Subject:') 
        self.subjecth.grid(row=1,column=0,sticky=E)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W) 
        self.receviernumber = Label(parent, text='From:')
        self.receviernumber.grid(row=2)
        self.code = Label(parent, text='To:')
        self.code.grid(row=3)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(parent, text=" Report  ",bg="blue",fg="white",
            ).grid(row=5,column=1)
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading)
        multi.start()
    def multithreading(self):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        for i in range(0, len(self.lg)):
            print(self.lg,"e")
            logging.debug('enterd interation No:%d'%i)
            title = self.lh[i]
            msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
                title=title)
            msg_01content = self.ar
            msg = msg_00content + msg_01content 
            message = MIMEText(msg, 'html')
            message['From'] =self.vs[i]
            message['To'] = self.ls[i]
            message['Subject'] = self.cr
            msg_full = message.as_string()
            sub=self.cr[11:]
            self.subject.config(text=str(sub))
            if i <= 10:
                try:
                    if self.internetcheck() == False:
                        tkinter.messagebox.showwarning('Warning','Network Failure,waiting for connections')
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0,1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                            
                                tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break      
                        
                    else:
                        
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[0], self.ys[0])  # Sender Mail, Sender Mail Password

                        server.sendmail(self.xs[0], [self.lg[i]], msg_full)
                        print(self.lg,"s")
                        self.start_thread(self.xs[0],self.lg[i])
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
                        logging.debug('Sending to : %s'%self.lh[i])
                        
                           
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        tkinter.messagebox.showinfo('Information','Network Failure,waiting for connections')
                        
                        
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showinfo('Information','Sleeping until internet connects...Trying %d times' % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                                
                                
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                
                    else:
                        roots=Tk()
                        self.k = 300 
                        self.s = 100
                        self.wk = roots.winfo_screenwidth() 
                        self.hw = roots.winfo_screenheight()
                        self.z = (self.wk/2) - (self.k/2)
                        self.u = (self.hw/2) - (self.s/2) 
                        self.text=Text(roots)
                        self.text.grid(row=3)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        file = open("Errorlog.txt", "w")
                        file.write("Date Time:{}".format(str(now)))
                        file.write("Error: MailerID {} /n".format(self.xs[0]))
                        file.write("Error: MailerID {} /n".format(i))
                        file.close()
                        self.d1="Date Time:{}".format(str(now))
                        tkinter.messagebox.showinfo('Information',"Date Time:{}".format(str(now)))
                        tkinter.messagebox.showinfo('Information',"Error: MailID {}".format(self.xs[0]))
                        tkinter.messagebox.showinfo('Information',"Error: Sent upto {}".format(i))
                        self.text.insert(END,"Date Time:{} \n".format(str(now)))
                        self.text.insert(END,"Error: MailID {} \n".format(self.xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto:%d"%i)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
                        break
            else:
                logging.debug('Contact Developer...Needs Renovation.')
                tkinter.messagebox.showinfo('Information','Contact Developer...Needs Renovation.')
                
     #----- start_thread for sample-----#  
    def start_thread(self,a,b):
        
        self.app_thread = AppThread(
            self.queue,self.queue1,a,b)
      #----- queue_polling1 for sample-----#   
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
 #----- queue_polling2 for sample-----#
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass                      
        #self.after(POLLING_TIME, self.queue_polling)
                 
    def close(self):
        #print("Application-Shutdown")
        self.app_thread.join()
        self.master.destroy()
#----------Thread for Actual--------        
class AppThread1(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join()
#------Actual classs------#        
class Actual(tk.Frame,mainwindow):
    key=0

    def __init__(self,parent):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        logging.debug('Selected Sample Option')
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        parent.title("Mail Automation") 
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        self.subjecth=Label(self.frame_head,text='Subject:',font='Helvetica 10 bold') 
        self.subjecth.grid(row=1,column=0,sticky=E+N)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W)
        self.receviernumber = Label(parent, text='From:',font='Helvetica 10 bold')
        self.receviernumber.grid(row=2)
        #self.t1=Label(parent)
        #self.t1.grid(row=3)
        self.code = Label(parent, text='To:',font='Helvetica 10 bold')
        self.code.grid(row=4,sticky=N)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=4, column=1,sticky=N)
        self.B1=Button(parent, text=" Report  ",bg="blue",fg="white",command=self.report
            ).grid(row=5,column=1)
        sub=secondwindow.subjectentry.get('1.0', END)
        subj=textwrap.fill(sub, 100)
        self.subject.config(text=str(subj))
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading1)
        multi.start()
    def multithreading1(self):
        global numberentry
        global codeentry
        global ment
        #ment=StringVar()
        logging.debug('Selected Actual Customers Option')
        j=0
        k=1
        df=secondwindow.codeentry.get()
        self.uo=secondwindow.numberentry.get()
        self.uo=int(self.uo)
        key=0
        for i in range(self.uo,mainwindow.count1):
            logging.debug('enterd interation No:%d'%i)
            title = mainwindow.readlt[0][i]
            msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
                title=title)
            msg_01content = self.ar
            msg = msg_00content #+ar
            message = MIMEText(msg, 'html')
            message['From'] =self.vs[j]
            message['To'] = self.ls[i]
            bk=',Feedback-ID:{df}:{fd}:01:01'.format(df=df,fd=i)
            message['Subject'] = self.cr+bk
            msg_full = message.as_string()
            print(msg_full)
            #sub=self.cr[11:]
            
            if i <= 500:
                try:
                    if self.internetcheck() == False:
                        
                        
                        #tkinter.messagebox.showwarning('Warning',"Network Failue,waiting for connections")

                        
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                    
                        for u in range(0,1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                
                                #tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                #if self.internetcheck() == True:
                                    #break
                            else:
                                count=10
                                messagess(count)
                                count=9
                                messagess(count)
                                #tkinter.messagebox.showwarning('Warning',"Awake from sleep, Got connection...")
                                #print("Awake from sleep, Got connection...", end='\r')
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break
                        
                                
                    else:
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[j], self.ys[j])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[j], [self.ls[i]], msg_full)
                        mainwindow.report.append(self.xs[j])
                        self.start_thread(self.xs[j],self.ls[i])
                        
                        
                    
                        if i==200:
                            
                            count=2
                            messagess(count)
                        if i==400:
                            
                            count=4
                            messagess(count)
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
                        server.quit()  # asking server to quit
                        time.sleep(10)
                        logging.debug('Sending to : %s'%self.lt[i])
                        Actual.key=i         
                        print(Actual.key)
                        if k!=0:
                            if j<30:
                                j=1
                            elif j>30 and j<60:
                                j=2
                            elif j>60 and j<90:
                                j=3
                            elif j>90 and j<120:
                                j=4
                            elif j>120 and j<150:
                                j=5
                            elif j>150 and j<180:
                                j=6
                            elif j>180 and j<210:
                                j=7
                            elif j>210 and j<240:
                                j=8
                            elif j>240 and j<270:
                                j=9
                            elif j>300 and j<330:
                                j=10
                            elif j>330 and j<360:
                                j=11
                            elif j>360 and j<390:
                                j=12
                            elif j>390 and j<420:
                                j=13
                            elif j>420 and j<450:
                                j=14
                            elif j>450 and j<480:
                                j=15
                            elif j>480 and j<510:
                                j=16
                            elif j>510 and j<540:
                                j=17
                            elif j>540 and j<580:
                                j=18
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        
                        #ment="Network Failue,waiting for connections"
                        #self.text.insert(END,ment)
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                
                                time.sleep(1)
                                #tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                #if self.internetcheck() == True:
                                    #break
                            else:
                                #tkinter.messagebox.showwarning('Warning',"Awake from sleep, Got connection...")
                                count=10
                                messagess(count)
                                count=9
                                messagess(count)
                                sys.stdout.flush()
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break
                    else:
                        roots=Tk()
                        self.k = 300 
                        self.s = 100
                        self.wk = roots.winfo_screenwidth() 
                        self.hw = roots.winfo_screenheight()
                        self.z = (self.wk/2) - (self.k/2)
                        self.u = (self.hw/2) - (self.s/2) 
                        self.text=Text(roots)
  
                        self.text.grid(row=3)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        file = open("Errorlog.txt", "w")
                        file.write("Date Time:{}".format(str(now)))
                        file.write("Error: MailerID {} /n".format(self.xs[j]))
                        file.write("Error: MailerID {} /n".format(i))
                        file.close()
                        self.text.insert(END,"Date Time:{} \n".format(str(now)))
                        self.text.insert(END,"Error: MailID {} \n".format(self.xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        self.text.insert(END,"Error section j={}".format(j))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto: %d"%i)
                        logging.error("Sent with: %d"%j)

                        
                        j=j+1

                        k=0
                        continue
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
               
            elif i>=500:
                logging.debug('Contact Developer...Needs Renovation.')
        
                print("Contact Developer.... Needs Renovation.")
        
        Actual.pend=(mainwindow.count1)-Actual.key
        if Actual.pend==0:
            count=5
            messagess(count)
        if Actual.pend!=0:
            count=6
            messagess(count)
       
        for i in range(len(self.xs)):
            mainwindow.c.append(mainwindow.report.count(self.xs[i]))
        
    #----- start_thread for Actual-----#            
    def start_thread(self,a,b):
       
        #if self.app_thread == None:
        #print(a)
        self.app_thread = AppThread1(
            self.queue,self.queue1,a,b)
        #else:
            #if not self.app_thread.isAlive():
        #self.app_thread = AppThread(
        #self.queue,a) 
    #----- queue_polling1 for Actual-----#      
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
    #----- queue_polling2 for Actual-----#            
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass  
    def report(self):
        roots=Tk()
        roots.title("Mail Automation")
        self.k = 400 
        self.s = 200
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2) 
        self.text=Text(roots)
        self.text.grid(row=3)
        for i in range(len(self.xs)):

            self.text.insert(END,"Signin ID:{} = {}  \n".format(self.xs[i],mainwindow.c[i]))
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()                    
        #self.after(POLLING_TIME, self.queue_polling)            
#----root for sample class----#
def samplepath():
    root = tk.Tk()
    app = Sample(root)
    
    root.mainloop()
 #------root for Actual class---#   
def actualpath():
    root = tk.Tk()
    app = Actual(root)
    
    root.mainloop()



    
#----------Thread for schedule--------
class AppThread2(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join()
#------solve class of schedule mode-----#        
class solve(tk.Frame,secondwindow):

    def __init__(self,parent):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        logging.debug('Selected Sample Option')
        solve.v = StringVar()
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        parent.title("Mail Automation")
        self.subjecth=Label(self.frame_head,text='Subject:',font='Helvetica 10 bold') 
        self.subjecth.grid(row=1,column=0,sticky=E+N)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W)

        self.receviernumber = Label(parent, text='From:',font='Helvetica 10 bold')
        self.receviernumber.grid(row=2,column=0,sticky=E)

        self.code = Label(parent, text='To:')
        self.code.grid(row=3,column=0,sticky=E)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(parent, text=" Report  ",bg="blue",fg="white",command=self.report
            ).grid(row=5,column=1)
        sub=secondwindow.subjectentry1.get('1.0', END)
        subj=textwrap.fill(sub, 100)
        self.subject.config(text=str(subj))
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading)
        multi.start()
    def multithreading(self):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        global tri
        global bac
        logging.debug('Selected Actual Customers Option')
        j=0
        if tri==1:
                i=bac
        df=secondwindow.code.get()
                
        for i in range(bac, len(self.ls)):
            
            logging.debug('enterd interation No:%d'%i)
            title = self.lt[i]
            msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
                title=title)
            msg_01content = self.ar
            
            msg = msg_00content + msg_01content 
            message = MIMEText(msg, 'html')
            message['From'] =self.vs[j]
            message['To'] = self.ls[i]
            bk=',Feedback-ID:{df}:{fd}:01:01'.format(df=df,fd=i)
            message['Subject'] =self. cr+bk
            msg_full = message.as_string()
            #sub=self.cr[11:]
            
            
            if i <= 500:
                try:
                    if self.internetcheck() == False:
                        #tkinter.messagebox.showwarning('Warning','Network Failure,waiting for connections')
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0,1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                #tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    bac=i
                                    tri=1
                                    count=10
                                    messagessedule(count)
                                    count=9
                                    messagessedule(count)
                                    
                            else:
                                count=10
                                messagessedule(count)
                                count=9
                                messagessedule(count)
                                #tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break

                    else:
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[j], self.ys[j])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[j], [self.ls[i]], msg_full)
                        mainwindow.report.append(self.xs[j])
                        self.start_thread(self.xs[j],self.ls[i])
                        if i==100:
                            
                            count=1
                            messagessedule(count)
                        if i==200:
                            
                            count=2
                            messagessedule(count)
                        if i==300:
                            
                            count=3
                            messagessedule(count)
                        if i==400:
                            
                            count=4
                            messagessedule(count)
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
                        server.quit()  # asking server to quit
                        time.sleep(10)
                        logging.debug('Sending to : %s'%self.lt[i])
                        solve.key=i
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        #tkinter.messagebox.showwarning('Warning','Network Failure,waiting for connections')
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                #tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    count=10
                                    messagessedule(count)
                                    count=9
                                    messagessedule(count)
                                    break
                            else:
                                count=10
                                messagessedule(count)
                                count=9
                                messagessedule(count)
                                #tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                sys.stdout.flush()
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break
                    else:
                        roots=Tk()
                        self.k = 300 
                        self.s = 100
                        self.wk = roots.winfo_screenwidth() 
                        self.hw = roots.winfo_screenheight()
                        self.z = (self.wk/2) - (self.k/2)
                        self.u = (self.hw/2) - (self.s/2) 
                        self.text=Text(roots)
                        self.text.grid(row=3)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        file = open("Errorlog.txt", "w")
                        file.write("Date Time:{}".format(str(now)))
                        file.write("Error: MailerID {} /n".format(self.xs[j]))
                        file.write("Error: MailerID {} /n".format(i))
                        file.close()
                        self.text.insert(END,"Date Time:{} \n".format(str(now)))
                        self.text.insert(END,"Error: MailID {} \n".format(self.xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        self.text.insert(END,"Error section j={}".format(j))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto: %d"%i)
                        logging.error("Sent with: %d"%j)
                        j=j+1
                        k=0
                        
                        
                        
                        continue
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
            elif i>=500:
                logging.debug('Contact Developer...Needs Renovation.')
        
                print("Contact Developer.... Needs Renovation.")
        solve.pend=(mainwindow.count1)-solve.key
        print(solve.pend)
        if solve.pend==0:
            count=5
            messagessedule(count)
        if solve.pend!=0:
            count=6
            messagessedule(count)

        
        for i in range(len(self.xs)):
            mainwindow.c.append(mainwindow.report.count(self.xs[i]))
        
    #----- start_thread of solve class-----#               
    def start_thread(self,a,b):
        
        self.app_thread = AppThread2(
            self.queue,self.queue1,a,b)
    
#----- queue_polling1 of solve class-----#          
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
#----- queue_polling2 of solve class-----#                
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass                      
    def report(self):
        roots=Tk()
        roots.title("Mail Automation")
        self.k = 400 
        self.s = 200
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2) 
        self.text=Text(roots)
        self.text.grid(row=3)
        for i in range(len(self.xs)):

            self.text.insert(END,"Signin ID:{} = {}  \n".format(self.xs[i],mainwindow.c[i]))
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()
#-----scd function takes to solvepath------#        
def scd():
    global tri
    global bac
    tyme=secondwindow.codeentry.get()
    daye=secondwindow.numberentry.get()
    
    a=tyme
    b=daye
    if b=='sun':
        schedule.every().sunday.at(tyme).do(solvepath)
    elif b=='mon':
        schedule.every().monday.at(tyme).do(solvepath)
    elif b=='tue':
        schedule.every().tuesday.at(tyme).do(solvepath)
    elif b=='wed':
        schedule.every().wednesday.at(tyme).do(solvepath)
    elif b=='thu':
        schedule.every().thursday.at(tyme).do(solvepath)
    elif b=='fri':
        schedule.every().friday.at(tyme).do(solvepath)
    elif b=='sat':
        schedule.every().saturday.at(tyme).do(solvepath)
    while True:
        schedule.run_pending()
        time.sleep(1)
def messagess(no):
    
    account_sid = "AC09f56551e91dd660b68aa5eb4cc8762a"
    auth_token = "70949c6fa3220b492a3849a91f5fa998"
    client = Client(account_sid, auth_token)
    if no==1:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 100 emails")
        logging.debug('sent upto 100 emails')
    if no==2:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 200 emails")
        logging.debug('sent upto 200 emails')
    if no==3:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 300 emails")
        logging.debug('sent upto 300 emails')
    if no==4:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 400 emails")
        logging.debug('sent upto 400 emails')
    if no==5:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent to all {} emails ".format(Actual.key))
        logging.debug('sent All :)')
    if no==6:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata has pendings {}".format(Actual.pend))

    if no==7:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Internet problem Holding its position ")
        
    if no==8:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Stalled and Process Started again sent upto {}".format(Actual.key))
    if no==9:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Stalled and Process Started again sent upto {}".format(Actual.key))
        logging.debug("Mail Automata Stalled and Process Started again ")
    if no==10:
        logging.debug("Mail Started Running")

def messagessedule(no):
    
    account_sid = "AC09f56551e91dd660b68aa5eb4cc8762a"
    auth_token = "70949c6fa3220b492a3849a91f5fa998"
    client = Client(account_sid, auth_token)
    if no==1:
       
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 100 emails")
        logging.debug('sent upto 100 emails')
    if no==2:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 200 emails")
        logging.debug('sent upto 200 emails')
    if no==3:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 300 emails")
        logging.debug('sent upto 300 emails')
    if no==4:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent upto 400 emails")
        logging.debug('sent upto 400 emails')
    if no==5:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata sent to all {} emails ".format(solve.key))
        logging.debug('sent All :)')
    if no==6:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata has pendings {}".format(solve.pend))
    if no==7:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Internet problem Holding its position ")
        
    if no==8:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Stalled and Process Started again sent upto {}".format(solve.key))
    if no==9:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Automata Stalled and Process Started again sent upto {}".format(solve.key))
        logging.debug("Mail Automata Stalled and Process Started again ")
    if no==10:
        
        message = client.api.account.messages.create(to="+917338766066",
                                             from_="+19202800064",
                                             body="Welcome to Airbots Service,Mail Started Running")
        logging.debug("Mail Started Running")




#------this sets root to class solve--#         
def solvepath():
    root = tk.Tk()
    app = solve(root)
    
    root.mainloop()
#---root for schedule fun in class secondwindow-----#
def main():
    root = tk.Tk()
    app = secondwindow.schedule(root)
    
    root.mainloop()
#--------------------------------------------------------------------------------------------------------#    
def secondmain():#mainwindow
    app_win = tk.Tk()
    app_win.title("Mail Automation")
    wk = app_win.winfo_screenwidth() 
    hw = app_win.winfo_screenheight() 
    z = (wk/2) - (APP_WIDTH/2)
    u = (hw/2) - (APP_HEIGHT/2)
    app_win.geometry('%dx%d+%d+%d' % (APP_WIDTH,APP_HEIGHT, z, u))
    #app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    
    app = secondwindow(app_win)
     
    app_win.mainloop()

mainwindow()
