#Question 1
#Occurrence remover
input_list = input('Enter space separated elements of list: ').split()
x=input("enter element to remove: ")

print('Before removing: ',input_list)

if(x in input_list):
	for i in range(input_list.count(x)):
		input_list.remove(x)

print('After removing: ',input_list)




#Question 2
#Pangram checker
import string
user_str = input('Enter your string: ').lower()

all_alphabets= string.ascii_lowercase
count=len(all_alphabets)

for i in all_alphabets:
	if(i in user_str):
		count-=1

if(count==0):
	print('String is pangram')
else:
	print('String is not pangram')
