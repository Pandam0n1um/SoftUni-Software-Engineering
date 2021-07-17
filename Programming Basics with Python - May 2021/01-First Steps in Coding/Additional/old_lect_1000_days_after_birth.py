import datetime

birthday = input()

birthday_datetime = datetime.datetime.strptime(birthday,"%d-%m-%Y")

birthday_1000 = birthday_datetime + datetime.timedelta(days=+1000)
birthday_1000_string = datetime.datetime.strftime(birthday_1000, "%d-%m-%Y")

print(birthday_1000_string)