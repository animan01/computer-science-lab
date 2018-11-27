# Import lib.
import csv
import re


def save_csv_file(type, data):
    with open('csv/' + type + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for key, value in data.items():
            headline = datamail = []

            if (key == 'metadata'):
                headline = ['Date', 'Subject', 'Signature']
                datamail = value['Date'] + value['Subject'] + value['Default Signature']

            if (key == 'emails'):
                headline = ['Sender', 'Receiver']
                datamail = value['Sender'] + value['Receiver']

            if (key == 'message'):
                headline = ['Message']
                datamail = value['Message']

            if (key == type):
                writer.writerow(headline)
                writer.writerow(datamail)


def parse_to_csv_file(type):
    if (type == 'message'):
        print("Message text")

    if (type == 'metadata'):
        print("Subject text")

    if (type == 'emails'):
        print("Emails sender and receiver")


def generate_pattern(name):
    pattern = name + ': (g?.+)'

    return pattern


# Work with file email.txt.
with open('email.txt', 'r') as email:
    data = email.read()

    # Get value.
    date = re.findall(generate_pattern('Date'), data)
    subject = re.findall(generate_pattern('Subject'), data)
    signature = re.findall(generate_pattern('Default Signature'), data)
    sender = re.findall(generate_pattern('From'), data)
    receiver = re.findall(generate_pattern('To'), data)
    message = re.findall('\n\n(.+)\n', data)

    data_arr = {'metadata': {'Date': date, 'Subject': subject, 'Default Signature': signature},
                'emails': {'Sender': sender, 'Receiver': receiver}, 'message': {'Message': message}}
    print(data_arr)

save_csv_file('metadata', data_arr)
save_csv_file('emails', data_arr)
save_csv_file('message', data_arr)
