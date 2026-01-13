# number 1 .Last week you wrote a program that printed out a cheery greeting including yourname. Take a copy of it, and modify it so that the user enters their name at the keyboard, and then receives a greeting.
user_name= input("Hello,what is your name?:")
print(f"Hello,{user_name}. Good to meet you!")


#number 2
temp=float(input("enter the temperature in celcius:"))
fahrenheit = (temp*9/5)+32
print(f"{temp}C is equivalent to {fahrenheit}F.")

#number 3
students = int (input ("how many students?"))
group_size = int(input("Required group size?"))
groups= students//group_size
leftover=students%group_size
group_word="group" if groups==1 else "groups"
student_word="Student" if leftover==1 else "students"
print (f"There will be {groups} {group_word} with {leftover} {student_word}.")