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

def convert_time():
  v_Day_Start = int(input(f"Dia "))
  v_Hour_Start, v_Minute_Start, v_Second_Start = list(map(int, input().split(" : ")))
  v_Day_End = int(input(f"Dia "))
  v_Hour_End, v_Minute_End, v_Second_End = list(map(int, input().split(" : ")))

  v_Total_Days = v_Day_End - v_Day_Start - 1
  v_Time_1 = v_Second_Start + 60 * v_Minute_Start + 3600 * v_Hour_Start
  v_Duration = (24 * 3600) - v_Time_1
  v_Time_2 = v_Second_End + 60 * v_Minute_End + 3600 * v_Hour_End
  v_Duration += v_Time_2
  v_Hours_Total = v_Duration // 3600
  v_Duration = v_Duration % 3600
  v_Minutes_Total = v_Duration // 60
  v_Seconds_Total = v_Duration % 60
  if v_Hours_Total >= 24:
    v_Hours_Total = v_Hours_Total - 24
    v_Total_Days += 1

  print(f"{v_Total_Days} dia(s)")
  print(f"{v_Hours_Total} hora(s)")
  print(f"{v_Minutes_Total} minuto(s)")
  print(f"{v_Seconds_Total} segundo(s)")


convert_time()
