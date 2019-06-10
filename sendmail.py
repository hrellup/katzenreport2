#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import syslog
import emailconfig



RECIPIENTS = ['fabian.puller@pfennigsberg.de', 'jens.puller@pfennigsberg.de']
FROM = emailconfig.DATA['from']
SUBJECT = 'Katzenreport'
SERVER = emailconfig.DATA['server']
PORT = emailconfig.DATA['port']
USER = emailconfig.DATA['user']
PASSWORD = emailconfig.DATA['password']

TEST = "TEST.JPG"


def go(image, result):
	
	syslog.syslog('sendmail start')

	emaillist = [elem.strip().split(',') for elem in RECIPIENTS]
	msg = MIMEMultipart()
	msg['Subject'] = SUBJECT
	msg['From'] = FROM

	 
	msg.preamble = 'Multipart massage.\n'
	 
	part = MIMEText("Hi, siehe Anhang" + "\n" + str(result))
	msg.attach(part)
	 
	part = MIMEApplication(open(str(image),"rb").read())
	part.add_header('Content-Disposition', 'attachment', filename=str(image))
	msg.attach(part)
	 

	server = smtplib.SMTP(SERVER+":"+str(PORT))
	server.ehlo()
	server.starttls()
	server.login(USER, PASSWORD)
	 
	server.sendmail(msg['From'], emaillist , msg.as_string())


	syslog.syslog('sendmail end')
	
	
if __name__ == "__main__":
	
	go(TEST, "TestMail")
