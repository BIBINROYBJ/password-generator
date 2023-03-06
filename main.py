#password generator project using python

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to password generator")
num_of_letters = int(input("how much letters should available in your password"))
num_of_numbers = int(input("how much numbers should available in your password\n"))
num_of_symbols = int(input("how much symbols should available in your password\n"))

password_list = []
for letter in range(1,num_of_letters + 1):
    password_list.append(random.choice(letters)) 
    
for number in range(1,num_of_numbers + 1):
    password_list.append(random.choice(numbers)) 

for symbol in range(1,num_of_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)    

password = ""
for i in password_list:
    password += i
print(f"your password is {password}") 
