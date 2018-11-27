import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "web.minning2017" + ORG_EMAIL
FROM_PWD    = "aq1212qa"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])


    for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(i, '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                print ('From : ' + email_from + '\n')
                print ('Subject : ' + email_subject + '\n')

#read_email_from_gmail()


import imaplib
import base64

#email_user = input('Email: ')
#email_pass = input('Password: ')

# Access data
email_user = "web.minning2017@gmail.com"
email_pass = "aq1212qa"

import poplib
import string, random
import logging

SERVER = "pop.gmail.com"
USER = email_user
PASSWORD = email_pass

# connect to server
logging.debug('connecting to ' + SERVER)
server = poplib.POP3_SSL(SERVER)
# server = poplib.POP3(SERVER)

# log in
logging.debug('log in')
server.user(USER)
server.pass_(PASSWORD)
