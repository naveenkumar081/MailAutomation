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
s=raw_input("Enter the Recevier Emails")
ls = s.split(",")
time.sleep(3)
t=raw_input("Enter the Recevier Names")
lt= []
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
	server.login('sharmivedicfolks@gmail.com','vedicfolks123')#Sender Mail, Sender Mail Password
	server.sendmail('sharmivedicfolks@gmail.com',        #Sender Mail,Receiver Mail
                [ls[i]],
                msg_full)
	print(" \n Sent to ",i,lt[i]) #Sent Log
	server.quit() #asking server to quit
	time.sleep(6) #sleeptime 