import requests

def get_emails():
  emails = {}
  try:
      email_file = open('emails2.txt', 'r')

      for line in email_file:
          (email, name) = line.split(',')
          emails[email] = name.strip()

  except FileNotFoundError as err:
      print(err)

  return (emails)

def get_schedule():
  try:
      schedule_file = open('schedule.txt' ,'r')
      schedule = schedule_file.read()
  except FileNotFoundError as err:
      print(err)

  return (schedule)



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
    print(forecast)

def main():
      emails = get_emails()
      print(emails)
      schedule = get_schedule()
      print(schedule)
      forecast = get_weather_forecast()



main()
