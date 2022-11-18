import math
#The temp in Kelvin
kelvin_temp = 301

#This is the temp in celsius
celsius_temp = kelvin_temp - 273.15 

#This is the fahrenheit temp
fahrenheit_temp = celsius_temp * 9/5 + 32

#This round the Fahrenheit Temp to the lowest value
fahrenheit_temp = math.floor(82.13)
print("The temperature is",fahrenheit_temp, "degrees fahrenheit")

