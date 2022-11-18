def input_calories_by_day (day):
    if day == 'monday':
     return 3500
    if day == 'tuesday':
     return  1700
    if day == 'wednesday':
     return 2100
    if day == 'thursday':
     return 3000
    if day == 'friday':
     return 1500
    if day == 'saturday':
     return 2300
    if day == 'sunday':
     return 1400
    else: "Enter Valid Day"

def get_total_calories ():
    return input_calories_by_day('monday') + input_calories_by_day('tuesday') + input_calories_by_day('wednesday') + input_calories_by_day('thursday') + input_calories_by_day('friday') + input_calories_by_day('saturday') + input_calories_by_day('sunday') 
    
def get_ideal_calories ():
    ideal_daily_calories = 2000
    return ideal_daily_calories * 7

def calorie_health_plan ():
    actual_calories = get_total_calories ()
    ideal_calories = get_ideal_calories()
    if actual_calories == ideal_calories:
     print("Perfect Diet")
    if actual_calories >= ideal_calories:
     print("Eating too much")
    if actual_calories <= ideal_calories:
     print("Eat more")

calorie_health_plan ()