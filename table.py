#table printer which prints the table and also saves it to a file(The file is created by the program it self)
user_number = int(input("Enter the num whose table you want to print: \n"))
#the number of which the user wants to see the table of 
user_choice = int(input("Till how long do you want to see the table : \n"))
#this allows the user to print the table until the choice of his number for eg if user enters 5 above and 9 below then the program will display the table of 5 till 9
print(f"The table of {user_number} till {user_choice} is : \n")
f = open("tables.txt","w")
for i in range (1,user_choice+1):
    print(f"{user_number}*{i} ={user_number*i} ")
    f.write(f"{user_number}*{i} = {user_number * i} \n")
f.close()
#this writes the table into a seperate file named tables.txt and saves it every time the program is ran