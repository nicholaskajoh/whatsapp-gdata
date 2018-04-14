import re

def clean_text(text):
    text = text.replace(',','')
    text = re.sub(r'("|“|”)', '\\"', text)
    return text

output = "id,date,time,user,text"

with open("whatsapp-group-data.txt", 'r') as data:
    messages = data.readlines()

for i in range(len(messages)):
    messages[i] = messages[i].strip('\n')
    message = messages[i].split(' - ', 1)

    # check that the first portion of the message variable is a date and time
    # if not then it's part of the previous message, so append it to the previous message
    if re.match(r'(\d+/\d+/\d+, \d+:\d+)', message[0]):
        _id = i + 1
        date, time = message[0].split(', ')
        message = message[1].split(': ', 1)
        if len(message) == 2:
            user, text = message[0], message[1]
        else:
            user, text = "", message[0]

        output += "\n%d,%s,%s,%s,%s" % (_id, date, time, user, clean_text(text))
    else:
        output += " %s" % clean_text(message[0])

with open("whatsapp-group-data.csv", 'w') as data_file:
    data_file.write(output)