"""
Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.

You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.

Input
The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.

Output
Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration of one minute. “dia” means day, “hora” means hour, “minuto” means minute and “Segundo” means second in Portuguese.
"""

""" #Não foi aceito
startday = int(input('Dia '))
starttime = list(map(int, input().split(':')))
endday = int(input('Dia '))
endtime = list(map(int, input().split(':')))

DAY = endday - startday - 1
HOURS = 0
MINUTES = 0
SECONDS = 0

print('{} dia(s)'.format(DAY))

if starttime[0] > endtime[0]:
    HOURS = (24 - starttime[0]) + endtime[0]
elif endtime[0] > starttime[0]:
    HOURS = endtime[0] - starttime[0]
else:
    HOURS = 0
print('{} minuto(s)'.format(HOURS))

if starttime[1] > endtime[1]:
    MINUTES = (60 - starttime[1]) + endtime[1]
elif endtime[1] > starttime[1]:
    MINUTES = endtime[1] - starttime[1]
else:
    MINUTES = 1
print('{} minuto(s)'.format(MINUTES))

if MINUTES == 59:
   HOURS = HOURS - 1

if starttime[2] > endtime[2]:
    SECONDS = (60 - starttime[2]) + endtime[2]
elif endtime[2] > starttime[2]:
    SECONDS = endtime[2] - starttime[2]
else:
    SECONDS = 0
print('{} segundo(s)'.format(SECONDS))

if SECONDS == 59:
    MINUTES = MINUTES - 1
"""

#O que foi aceito

l1 = input()
d1 = int(l1[4:])
l2 = input()
h1 = l2[0] + l2[1]
h1 = int(h1)
m1 = l2[5] + l2[6]
m1 = int(m1)
s1 = l2[10] + l2[11]
s1 = int(s1)
l3 = input()
d2 = int(l3[4:])
l4 = input()
h2 = l4[0] + l4[1]
h2 = int(h2)
m2 = l4[5] + l4[6]
m2 = int(m2)
s2 = l4[10] + l4[11]
s2 = int(s2)
dd = d2 - d1 - 1
t1 = s1 + 60 * m1 + 3600 * h1
dur = (24 * 3600) - t1
t2 = s2 + 60 * m2 + 3600 * h2
dur += t2
hd = dur//3600
dur = dur%3600
md = dur//60
sd = dur%60
if hd >= 24:
  hd = hd - 24
  dd += 1
print("{0} dia(s)".format(dd))
print("{0} hora(s)".format(hd))
print("{0} minuto(s)".format(md))
print("{0} segundo(s)".format(sd))
