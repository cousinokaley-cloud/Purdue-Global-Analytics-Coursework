def celsius(tempc):
    tempf = tempc * 9/5 + 32 + 0.5
    return int(tempf)
def weather_statement(tempf):
    if tempf >= 95:
        return "A heat advisory has been issued."
    elif tempf >= 85:
        return "Pleasant but warm."
    elif tempf >= 70:
        return "Very pleasant weather today."
    elif tempf >= 50:
        return "Pleasant but cool."
    elif tempf >= 33:
        return "Cold weather."
    elif tempf <= 32:
        return "A freeze warning has been issued."
celsius1 = 35.5
celsius2 = 30.5
celsius3 = 22.2
celsius4 = 16.1
celsius5 = 7.3
celsius6 = -1
farenheit1 = celsius(celsius1)
statement1 = weather_statement(farenheit1)
print("The temperature is", str(celsius1) + "C or", str(farenheit1) + "F.", statement1)  
farenheit2 = celsius(celsius2)
statement2 = weather_statement(farenheit2)
print("The temperature is", str(celsius2) + "C or", str(farenheit2) + "F.", statement2) 
farenheit3 = celsius(celsius3)
statement3 = weather_statement(farenheit3)
print("The temperature is", str(celsius3) + "C or", str(farenheit3) + "F.", statement3) 
farenheit4 = celsius(celsius4)
statement4 = weather_statement(farenheit4)
print("The temperature is", str(celsius4) + "C or", str(farenheit4) + "F.", statement4) 
farenheit5 = celsius(celsius5)
statement5 = weather_statement(farenheit5)
print("The temperature is", str(celsius5) + "C or", str(farenheit5) + "F.", statement5)
farenheit6 = celsius(celsius6)
statement6 = weather_statement(farenheit6)
print("The temperature is", str(celsius6) + "C or", str(farenheit6) + "F.", statement6) 


