#temperature converter
print("="*40)
print("TEMPERAUTE CONVERTER")
print("="*40)



user_input = str(input("Which temperature are you entering (Celsius,Fahrenheit,Kelvin) \n")).lower().strip()
print("-"*40)
try:
      current_temp = float(input(f"Enter the current temperature in {user_input}: \n"))
except ValueError:
      print("Error!: you must enter a valid temperature")
      exit()
print("-"*40)
convert_temp = str(input("Which temperature do you want to convert it to (Celsius,Fahrenheit,Kelvin) \n"))
print("-"*40)

#guard_clasues
if convert_temp == user_input:
    print(f"You cannot convert {user_input} to {convert_temp}")
    exit()

#each function has current_temp set as the temp scale user entered and it converts the temp into desired scale based on the formula and retruns the value 
def celsius_temp():
    if convert_temp == "fahrenheit":
        temp_far = (current_temp*(9/5))+32
        print(f"Your temp in fahrenheit is {temp_far: .2f}")
        print("="*40)
        return temp_far

    if convert_temp == "kelvin":
            temp_kel = current_temp + 273.15
            print(f"Your temp in kelvin is {temp_kel: .2f}")
            print("="*40)
            return temp_kel

    
def fahrenheit_temp():
    if convert_temp == "celsius":
        temp_cel = (current_temp - 32)*(5/9)
        print(f"Your temp in celsius is {temp_cel: .2f}")
        print("="*40)
        return temp_cel

    if convert_temp == "kelvin":
            temp_kel = ((current_temp - 32)*(5/9)) + 273.15
            print(f"Your temp in kelvin is {temp_kel: .2f}")
            print("="*40)
            return temp_kel


def kelvin_temp():
    if convert_temp == "celsius":
        temp_cel = current_temp - 273.15
        print(f"Your temp in celsius is {temp_cel: .2f}")
        print("="*40)
        return temp_cel

    if convert_temp == "fahrenheit":
            temp_far = ((current_temp - 273.15)*1.8)+32
            print(f"Your temp in fahrenheit is {temp_far: .2f}")
            print("="*40)
            return temp_far

#checks what the userinput is and runs the appropraite function
if user_input == "celsius":
        celsius_temp()
if user_input == "fahrenheit":
        fahrenheit_temp()
if user_input == "kelvin":
        kelvin_temp()