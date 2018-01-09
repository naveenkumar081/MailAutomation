from __future__ import print_function
import smtplib
import time
import datetime
import urllib2
import sys
def internetcheck():
    try:
        urllib2.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
        return True
    except urllib2.URLError as err: 
        return False
now = datetime.datetime.now()
from email.mime.text import MIMEText
print("---Welcome to Mail Automation Application---")
print("kindly follow the below rules:")
print("-HTML text should be less than 4000")
print("-HTML text should be single quoted")
print("-Remove single quotes in areas of font type times newroman")
print("-Add Image seperately using img src not with class")
print("-Remove nonascii characters in Names")
ls=[] #recevier emailids
lt=[] #recevier names
xs=[] #signin emailids
ys=[] #signin passwords
lg=[] #sample emailids
lh=[] #sample names
g= open('EnterSampleEmails.txt','r')
gr=g.read()
lg = gr.split(",")
time.sleep(3)
h=open("EnterSampleNames.txt",'r')
th=h.read()
lh=th.split(",")
time.sleep(3)
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
    for i in range(0, len(lg)):
        title = lh[i]
        msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
            title=title)
        msg_01content = ar
        msg_02content = imr
        msg_03content = br
        msg = msg_00content + msg_01content + msg_02content + msg_03content
        message = MIMEText(msg, 'html')
        message['From'] = 'Vedicfolks<vedicfolks@gmail.com>'
        message['To'] = ls[i]
        message['Subject'] = cr
        msg_full = message.as_string()
        if i <= 100:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0,1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                        else:
                            print("Awake from sleep, Got connection...", end='\r')
                            sys.stdout.flush()

                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[0], ys[0])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[0], [lg[i]], msg_full)
                    print(" \n Sent to ", i, lh[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)
            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                    break
elif decide=='a':
    for i in range(400, len(ls)):
        title = lt[i]
        msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
            title=title)
        msg_01content = ar
        msg_02content = imr
        msg_03content = br
        msg = msg_00content + msg_01content + msg_02content + msg_03content
        message = MIMEText(msg, 'html')
        message['From'] = 'Vedicfolks<vedicfolks@gmail.com>'
        message['To'] = ls[i]
        message['Subject'] = cr
        msg_full = message.as_string()
        if i <= 100:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0,1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                        else:
                            print("Awake from sleep, Got connection...", end='\r')
                            sys.stdout.flush()

                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[0], ys[0])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[0], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(10)
            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                    break

        if i > 100 and i <= 200:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0, 1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                            else:
                                print("Awake from sleep, Got connection...", end='\r')
                                sys.stdout.flush()
                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[1], ys[1])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[1], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)
            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                            break
        if i > 200 and i <= 300:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0, 1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                            else:
                                print("Awake from sleep, Got connection...", end='\r')
                                sys.stdout.flush()
                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[2], ys[2])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[2], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)


            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                    break

        if i > 300 and i <= 400:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0, 1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                        else:
                            print("Awake from sleep, Got connection...", end='\r')
                            sys.stdout.flush()

                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[3], ys[3])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[3], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)


            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                    break

        if i > 400 and i <= 500:
            try:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
                    for u in range(0, 1000000):
                        if internetcheck() == False:
                            time.sleep(1)
                            print("Sleeping until internet connects...Trying %d times" % u, end='\r')
                            sys.stdout.flush()
                            if internetcheck() == True:
                                break
                            else:
                                print("Awake from sleep, Got connection...", end='\r')
                                sys.stdout.flush()

                else:
                    server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                    server.starttls()  # asking server to start
                    server.login(xs[4], ys[4])  # Sender Mail, Sender Mail Password
                    server.sendmail(xs[4], [ls[i]], msg_full)
                    print(" \n Sent to ", i, lt[i])
                    server.quit()  # asking server to quit
                    time.sleep(6)


            except smtplib.SMTPException:
                if internetcheck() == False:
                    print("Network Failure,waiting for connections")
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
                    break
                    # Sent Log
                    # sleeptime
