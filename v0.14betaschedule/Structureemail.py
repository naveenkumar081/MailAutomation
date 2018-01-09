from __future__ import print_function
import smtplib
import time
import datetime
import urllib
import urllib.request as ur
from urllib.error import URLError, HTTPError
import sys
import os
import logging
import logging.config
import schedule
import time
print('\n')
print("               ---Welcome to Mail Automation Application---")
print('\n')
daye=input("Enter Sending Day In Three Letters:")
tyme=input("Enter Sending Time within double quotes 15:00:")
logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
def internetcheck():
    try:
        ur.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1)
        #urllib.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
        return True
    except URLError as e:
        return False
now = datetime.datetime.now()
from email.mime.text import MIMEText
ls=[] #recevier emailids
lt=[] #recevier names
xs=[] #signin emailids
ys=[] #signin passwords
lg=[] #sample emailids
lh=[] #sample names
vs=[]
g= open('EnterSampleEmails.txt','r')
gr=g.read()
lg = gr.split(",")
time.sleep(3)
h=open("EnterSampleNames.txt",'r')
th=h.read()
lh=th.split(",")
time.sleep(3)
v=open('EnterIDs.txt','r')#inquotes
vr=v.read()
vs =vr.split(",")
x=open('EntersigninEmailID.txt','r')#inquotes
xr=x.read()
xs = xr.split(",")
y=open('EntersigninEmailPassword.txt','r')#inquotes
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
c= open('Entersubject.txt','r')
cr=c.read()#inquotes
a = open('EntertheHTMLPart-I.txt','r')
ar=a.read()
im= open('EnterImagePart.txt','r')
imr=im.read()
b= open('EntertheHTMLPart-II.txt','r')
br=b.read()
logging.debug('Selected Sample Option')
def solve():
    for i in range(0, len(lg)):
        logging.debug('enterd interation No:%d'%i)
        title = lh[i]
        msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
            title=title)
        msg_01content = ar
        msg_02content = imr
        msg_03content = br
        msg = msg_00content + msg_01content + msg_02content + msg_03content
        message = MIMEText(msg, 'html')
        message['From'] =vs[i]
        message['To'] = ls[i]
        message['Subject'] = cr
        msg_full = message.as_string()
        if i <= 10:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    logging.error(str(now))
                    logging.error("Internet Connection Not Established")
                    for u in range(0,1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                        else:
                            print("Awake from sleep, Got connection...", end='\r')
                            logging.debug(str(now))
                            logging.debug("Internet Connection Established")
                            sys.stdout.flush()

                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[0], ys[0])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[0], [lg[i]], msg_full)
                    print(" \n Sent to ", i, lh[i])
                    logging.debug('Sending to : %s'%lh[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)
            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    logging.error(str(now))
                    logging.error("Internet Connection Not Established")
                    for u in range(0, 1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                        else:
                            print("Awake from sleep, Got connection...")
                            logging.debug(str(now))
                            logging.debug("Internet Connection Established")
                            sys.stdout.flush()
                            break
                else:
                    file = open("Errorlog.txt", "w")
                    file.write("Date Time:{}".format(str(now)))
                    file.write("Error: MailerID {} /n".format(xs[0]))
                    file.write("Error: MailerID {} /n".format(i))
                    file.close()
                    print("Date Time:{}".format(str(now)))
                    print("Error: MailID {}".format(xs[0]))
                    print("Error: Sent upto {}".format(i))
                    logging.error("Unexpected Error Occured")
                    logging.error(str(now))
                    logging.error("Sent upto:%d"%i)
                    break
        else:
            logging.debug('Contact Developer...Needs Renovation.')
            print("Contact Developer...Needs Renovation")
print("d",daye)
#print("tyme",tyme)
a=tyme
b=daye
#print(a)
if b=='sun':
    schedule.every().sunday.at(tyme).do(solve)
elif b=='mon':
    schedule.every().monday.at(tyme).do(solve)
elif b=='tue':
    schedule.every().tuesday.at(tyme).do(solve)
elif b=='wed':
    schedule.every().wednesday.at(tyme).do(solve)
elif b=='thu':
    schedule.every().thursday.at(tyme).do(solve)
elif b=='fri':
    schedule.every().friday.at(tyme).do(solve)
elif b=='sat':
    schedule.every().saturday.at(tyme).do(solve)
#schedule.every().saturday.at(tyme).do(solve)
#schedule.every().sunday.at(tyme).do(solve)
while True:
    schedule.run_pending()
    time.sleep(1)               
