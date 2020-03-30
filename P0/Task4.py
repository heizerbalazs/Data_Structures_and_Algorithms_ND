"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def solution():
    normal_activity = [[text[i] for i in range(2)] for text in texts] + [call[1] for call in calls]
    possible_telemarketers = []
    for call in calls:
        if call[0] not in normal_activity:
            if call[0] not in possible_telemarketers:
                possible_telemarketers.append(call[0])
    possible_telemarketers.sort()
    return possible_telemarketers

print('These numbers could be telemarketers: ', *solution(), sep='\n')