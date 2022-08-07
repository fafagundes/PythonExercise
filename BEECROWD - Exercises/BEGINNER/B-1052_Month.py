"""
Read an integer number between 1 and 12, including. Corresponding to this number, you must print the month of the year, in english, with the first letter in uppercase.

Input
The input contains only an integer number.

Output
Print the name of the month according to the input number, with the first letter in uppercase.
"""
months = ["january", "february", "march", "april", "may", "june", "july", "august",
          "september", "october", "november", "december"]

n_month = int(input())

for i, month in enumerate(months):
    if n_month == i+1:
        print(months[i].capitalize())
    elif 0 >= n_month > 12:
        break
