#!/usr/bin/env python
c=[]
d=[]
e=[]
import time
def gmail_checker(username,password):
  import imaplib,re
  i=imaplib.IMAP4_SSL('imap.gmail.com')
  try:
    i.login(username,password)
    x,y=i.status('INBOX','(MESSAGES UNSEEN)')
    messages=int(re.search('MESSAGES\s+(\d+)',y[0]).group(1))
    unseen=int(re.search('UNSEEN\s+(\d+)',y[0]).group(1))
    return (messages,unseen)
  except:
    return False,0
x=open('EntersigninEmailID.txt','r')#inquotes
xr=x.read()
xs = xr.split(",")
y=open('EntersigninEmailPassword.txt','r')#inquotes
yr=y.read()
ys = yr.split(",")
for i in range(0,len(xs)):
    messages,unseen = gmail_checker(xs[i],ys[i])
    c.append(messages)
    d.append(unseen)
    e.append(xs[i])
    time.sleep(2)
for i in range(0,len(c)):
    print("%s EmailID || %i messages || %i unseen ||"%(e[i],c[i],d[i]))

