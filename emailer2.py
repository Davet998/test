import requests
import smtplib

def get_emails():
  emails = {}
  try:
      email_file = open('emails2.txt', 'r')

      for line in email_file:
          (email, name) = line.split(',')
          emails[email] = name.strip()

  except FileNotFoundError as err:
      print(err)

  return emails

def get_schedule():
  try:
      schedule_file = open('schedule.txt' ,'r')
      schedule = schedule_file.read()
  except FileNotFoundError as err:
      print(err)

  return schedule



def get_weather_forecast():
    appid_file = open('appid.txt' ,'r')
    appid = appid_file.read()
    appid = appid.strip()
    #print(appid)
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=' + appid
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    #print(weather_json)
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    #print(description)
    #print(temp_min))
    #print(temp_max))
    forecast = 'The weather now is ' + description + ' with a minimum temperature of '
    forecast += str(temp_min) + ' a high of ' + str(temp_max) + ' degrees C.'
    return forecast

def send_emails(emails, schedule, forecast):
    # Connect to SMTP Server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    # Start TLS
    server.starttls()

    email_cred = open('email.txt', 'r')
    for line in email_cred:
        (from_email, email_password) = line.split(',')

    #print(from_email)
    #print(email_password)

    # Login
    server.login(from_email, email_password)
    #send email
    for to_email, name in emails.items():
        # Build message
        message = 'Subject: Latest from Python!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule

        server.sendmail(from_email, to_email, message)

    server.quit()

def main():
      emails = get_emails()
      print(emails)
      schedule = get_schedule()
      print(schedule)
      forecast = get_weather_forecast()
      print(forecast)
      send_emails(emails, schedule, forecast)

main()
