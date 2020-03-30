"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def solution():
    phone_numbers = [call[i] for i in range(2) for call in calls]
    total_time = dict(zip(phone_numbers, [0 for i in phone_numbers]))
    for call in calls:
        total_time[call[0]] += int(call[3])
        total_time[call[1]] += int(call[3])
    phone_number = max(total_time.keys(), key=lambda key: total_time[key])
    return phone_number, total_time[phone_number]

phone_number, total_time = solution()
print(f'{phone_number} spent the longest time, {total_time} seconds, on the phone during')