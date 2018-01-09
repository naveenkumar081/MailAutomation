from __future__ import print_function
import smtplib
import time
import datetime
import urllib2
import sys
import os
import logging
import logging.config
logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
def internetcheck():
    try:
        urllib2.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
        return True
    except urllib2.URLError as err:
        return False
now = datetime.datetime.now()
from email.mime.text import MIMEText
print("---Welcome to Mail Automation Application---")
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
decide=raw_input("Enter Sending Option Sample or Actual(s/a:)")
if decide=='s':
    logging.debug('Selected Sample Option')
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
            print("Contact Developer...Needs Renovation.")
elif decide=='a':
    logging.debug('Selected Actual Customers Option')
    j=0
    k=1
    for i in range(1, len(ls)):
        logging.debug('enterd interation No:%d'%i)
        title = lt[i]
        msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
            title=title)
        msg_01content = ar
        msg_02content = imr
        msg_03content = br
        msg = msg_00content + msg_01content + msg_02content + msg_03content
        message = MIMEText(msg, 'html')
        message['From'] =vs[j]
        message['To'] = ls[i]
        message['Subject'] = cr
        msg_full = message.as_string()
        if i <= 500:
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
                    server.login(xs[j], ys[j])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[j], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(10)
                    logging.debug('Sending to : %s'%lt[i])
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
                            sys.stdout.flush()
                            logging.debug(str(now))
                            logging.debug("Internet Connection Established")
                            sys.stdout.flush()
                            break
                else:
                    file = open("Errorlog.txt", "w")
                    file.write("Date Time:{}".format(str(now)))
                    file.write("Error: MailerID {} /n".format(xs[j]))
                    file.write("Error: MailerID {} /n".format(i))
                    file.close()
                    print("Date Time:{}".format(str(now)))
                    print("Error: MailID {}".format(xs[0]))
                    print("Error: Sent upto {}".format(i))
                    print("Error section j=",j)
                    logging.error("Unexpected Error Occured")
                    logging.error(str(now))
                    logging.error("Sent upto: %d"%i)
                    logging.error("Sent with: %d"%j)
                    j=j+1
                    k=0
                    continue 
        elif i>=500:
            logging.debug('Contact Developer...Needs Renovation.')
            print("Contact Developer.... Needs Renovation.")

    
