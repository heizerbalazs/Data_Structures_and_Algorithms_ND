# Complexity analysis

## Task 0

The solution of **Task 0** runs in linear time *O(1)*, if we assume that built in list objects are arrays.

- Getting the first element from an array has constant time complexity.
- Getting the last element from an array has constant time complexity.

## Task 1

The worst case scenario of **Task 1** is the situation, when all the numbers in both `texts` and `calls` are distinct. Assuming that there is n records in `texts` and m records `calls` the time complexity of the solution is linear *O(m+n)*. The same is true for the space comlexity.

## Task 2

The worst case scenario of **Task 2** is when none of the numbers appear twice in `calls` and the last call was the longest conversation. If *n* is the number of records, the run time is for the worst case scenario for each row in my solution is the following:
```
phone_numbers = [call[i] for i in range(2) for call in calls] \ O(2*n)
total_time = dict(zip(phone_numbers, [0 for i in phone_numbers])) \ O(2*n)
for call in calls:                                              \ O(2*n)
    total_time[call[0]] += int(call[3])
    total_time[call[1]] += int(call[3])
phone_number = max(total_time.keys(), key=lambda key: total_time[key]) \ O(2*n)
return phone_number, total_time[phone_number] \ O(2*n)
```
Then the run time in the worst case scenario is *O(10n)* and the space complexity is *O(3n)*.

## Task 3

### Part A

The worst case scenario for **Part A** is when all call in the list are made by people live in Banglore, and all number called by them have distinct prefixes. The first task is the collection of prefixes, which in this case has *O(n)* time and space complexity. Then the sorting of the collected prefixes has to be done which has *O(nlog(n))* time complexity.

The time complexity of my solution is *O(nlog(n)+n)* and the space complexity is *O(n)*.

### Part B

To solve **Part B** the program has to loop over all records in `calls`.
Therefore the time complexity of my solution is *O(n)* and the space complexity is *O(1)*.

## Task 4

1. I collected all numbers which are in the called number list of `calls` or can be found in the `texts` list. This step has time and space complexity *O(2n+m)*, where *n* is the number of records in `calls` and *m* is the number of records in `texts`.

2. I checked all records in `calls`. If the number wich initiated the call is not an element of the list created in the first step, then I added it to the `possible_telemarketers` list. In the worst case scenario it has *O(m)* time and space complexity.

3. Finally I sorted the `possible_telemarketers` list, wich has *O(mlog(m))* time complexity.

The over all time complexity of my solution is *O(2n+2m+mlog(m))* and the space complexity is *O(2n+2m)*.
