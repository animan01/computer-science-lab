from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

file = open('email.txt', 'r')
file = file.readlines()

# Delete unnecessary symbol new line.
for i in range(len(file)):
    file[i] = file[i].rstrip()

# Access data
from_ = "web.minning2017@gmail.com"
user_passwd = "aq1212qa"

to = []
for i in range(len(file)):
    to = file[i]
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to
    print("Введіть тему повідомлення")
    msg['Subject'] = input()
    print("Введіть текст повідомлення")
    body = input()
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_, user_passwd)
    text = msg.as_string()
    server.sendmail(from_, to, text)
    server.quit()
