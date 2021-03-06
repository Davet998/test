#emailer.py
#emails-txt
emails = []
try:
    email_file = open('emails.txt', 'r')

    for line in email_file:
        emails.append(line.strip())

except FileNotFoundError as err:
    print(err)

print(emails)


emails = {}
try:
    email_file = open('emails2.txt', 'r')

    for line in email_file:
        (email, name) = line.split(',')
        emails[email] = name.strip()

except FileNotFoundError as err:
    print(err)

print(emails)


#Read schedule.txt
try:
    schedule_file = open('schedule.txt' ,'r')
    schedule = schedule_file.read()
except FileNotFoundError as err:
    print(err)

print(schedule)
