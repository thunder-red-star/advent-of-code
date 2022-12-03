import requests
from datetime import datetime
import time

session = None
year = 2022
day = 1

def pad_day(day):
    if day < 10:
        return '0' + str(day)
    return str(day)

while datetime.now().strftime("%Y-%m-%d %H:%M:%S") < f"{year}-12-{pad_day(day)} 00:00:00":
    time.sleep(1)
    print("Not ready...")
    time.sleep(1)

r = requests.get('https://adventofcode.com/{}/day/{}/input'.format(year, day), cookies={'session': session})

with open(pad_day(day) + "/input.txt", "w") as f:
    f.write(r.text.strip())

print("I got the input!")