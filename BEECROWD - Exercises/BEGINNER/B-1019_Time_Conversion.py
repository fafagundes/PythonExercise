"""Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example."""

var_Seconds = int(input())

# var_Hours = var_Seconds // (60*60)
# var_Rest_hours = var_Seconds - var_Hours * (60*60)
# var_Minutes = var_Rest_hours // 60
# var_Seconds = var_Rest_hours % 60

var_Hours = var_Seconds // 3600
var_Minutes = (var_Seconds % 3600) // 60
var_Seconds = (var_Seconds % 3600) % 60

print(f"{var_Hours}:{var_Minutes}:{var_Seconds}")
