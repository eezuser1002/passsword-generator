# Password Generator
import random
import string 

print('@@@@@@@@@@ Welcome to wahlae's password generator @@@@@@@@@@')

# request user data
length = int(input('\nEnter the length of password, we recommend 8 chars or more: '))
first_name = input(str("First Name:"))
last_name = input(str("Last Name:"))

# include random chars in the mixing of the pw 
symbols = string.punctuation

# combine the data
t_password = first_name + last_name + symbols

# randomly form the pw
temp = random.sample(t_password,length)

# create the pw
password_created = "".join(temp)

# print the pw
print(" Your password is: " + password_created)

