var_Spent_time = int(input())
var_Average_speed = int(input())

# calculate the spent time(in hours) and multiply by average speed (km/h). After divide
# the resulte by 12 (Km/L)

var_Resulte = (var_Average_speed * var_Spent_time) / 12

print(f"{var_Resulte:.3f}")
