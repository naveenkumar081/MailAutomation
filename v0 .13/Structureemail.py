import smtplib
import time
from email.mime.text import MIMEText
print("---Welcome to Mail Automation Application---")
print("kindly follow the below rules:")
print("-HTML text should be less than 4000")
print("-HTML text should be single quoted")
print("-Remove single quotes in areas of font type times newroman")
print("-Add Image seperately using img src not with class")
print("-Remove nonascii characters in Names")
ls=[]
lt=[]
xt=[]
yt=[]
x=open('EntersigninEmailID.txt','r')
xr=x.read()
xs = xr.split(",")
y=open('EntersigninEmailPassword.txt','r')
yr=y.read()
ys = yr.split(",")
s= open('EnterRecevierEmails.txt','r')
sr=s.read()
ls = sr.split(",")
time.sleep(3)
t=open("EnterRecevierNames.txt",'r')
tr=t.read()
lt=tr.split(",")
time.sleep(3)
a = open('EntertheHTMLPart-I.txt','r')
ar=a.read()
im= open('EnterImagePart.txt','r')
imr=im.read()
b= open('EntertheHTMLPart-II.txt','r')
br=b.read()
for i in range (0,len(ls)): 
	title = lt[i]
	msg_00content='<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(title=title)
	msg_01content=ar
	msg_02content=imr
	msg_03content=br
	msg=msg_00content+msg_01content+msg_02content+msg_03content
	message = MIMEText(msg, 'html')
	message['From'] = 'Vedicfolks<vedicfolks@gmail.com>'
	message['To'] = ls[i]
	# Enter the subject below
	message['Subject'] ='Vaikunta Ekadashi 2017 Special Rituals - A Chance To Attain Superior Protection For All Kinds Of Sufferings'
	msg_full = message.as_string()
	server = smtplib.SMTP('smtp.gmail.com:587') #setting up service provider name : port number
	server.starttls() #asking server to start
	if i<=100:
                server.login('sharmilavedicfolks@gmail.com','Shinchan') #Sender Mail, Sender Mail Password
                server.sendmail('sharmilavedicfolks@gmail.com',  #Sender Mail,Receiver Mail
                                [ls[i]],msg_full)
        if i>100 and i<=200:
                server.login('sharmiladevi.vedicfolks@gmail.com','vedicfolks@32') #Sender Mail, Sender Mail Password
                server.sendmail('sharmiladevi.vedicfolks@gmail.com',  #Sender Mail,Receiver Mail
                                [ls[i]],msg_full)
        if i>200 and i<=300:
                server.login('vedicfolks.sharmi@gmail.com','namashivaya@23') #Sender Mail, Sender Mail Password
                server.sendmail('vedicfolks.sharmi@gmail.com',  #Sender Mail,Receiver Mail
                                [ls[i]],msg_full)
        if i>300 and i<=400:
                server.login('vedicfolks.sharmila@gmail.com','sharmiladevivedicfolks') #Sender Mail, Sender Mail Password
                server.sendmail('vedicfolks.sharmila@gmail.com',  #Sender Mail,Receiver Mail
                                [ls[i]],msg_full)
        if i>400 and i<=500:
                server.login('swathiarun108@gmail.com','vedicfolks123') #Sender Mail, Sender Mail Password
                server.sendmail('swathiarun108@gmail.com',  #Sender Mail,Receiver Mail
                                [ls[i]],msg_full)
	print(" \n Sent to ",i,lt[i]) #Sent Log
	server.quit() #asking server to quit
	time.sleep(6) #sleeptime
