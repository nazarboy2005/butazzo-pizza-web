
from datetime import datetime

a = '6:00 AM'
time_format = '%I:%M %p'
formatted_time = datetime.strptime(a, time_format).time()
print(type(formatted_time))
print(formatted_time)