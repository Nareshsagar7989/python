# print('hello world')

# a = 'hello world'
# print(a)

# a =777
# b = 56
# c,d = a,b
# print(c,d)

# task
# assingn 3 values and multiply each adjacent values
# x,y,z = 56,90,34
# x,y,z = 56*90,90*34,34*56
# print(x,y,z)

# name = 'nareshsagar'
# age = 20
# phone = 7989053026
# student = True
# print(type(name))
# print(type(age))
# print(type(phone))
# print(type(student))

# d = int(input('enter number of days:'))
# hours = 24 * d
# min = hours * 60
# seconds = min * 60
# print(f'{d} days equals to {hours} hours and equals to {min} minutes and equals to {seconds} seconds')

# n = int(input("enter the number of hours:"))
# min = n * 60
# print(f'u entered {n} hours and the total minutes equals to: {min} minutes')

# age = int(input('enter your age:'))
# days = age * 365
# print(f'you entered the age as {age} years,equal to {days} days')


# tuple
# tuple = (45,78,99)
# print(tuple)

#set
# set = { 45, 78, 90}
# print(tuple)

#dictionary
# dict = {
#     'name' : 'naresh',
#     'age' : 20
# }
# print(dict)

# list
# list = ['naresh' ,'ajay' ,20 ,22 ]
# print(f'{list},{type(list)}') 

a = [78 ,'john' ,90.5 ]

# set doesnot support indexing but can be done by converting to other type list
'''b = {89 ,90 }
c = (23 ,45 ,67 )
d = {
    "name" : "john",
    "age" : 23
}
print(a[1])
print(list(b)[1])
print(c[2])
print(d["name"])
'''
# code to check whether a number is even or odd
'''a = int(input('enter the num:'))
if(a % 2 == 0):
    print('even')
else:
    print('odd')
'''
'''a = int(input('enter a:'))
print('even' if a % 2 == 0 else 'odd')
percentage = int(input('enter the percentage: '))'''
'''if percentage >= 75:
    print('eligible for program')
else:
    print('not eligible for program')'''

# print('you can enter the program' if percentage >= 75 else "u r not allowed")

'''username = 'shiva'
password = 'shiva@370'
a = input('enter username: ')
b = input('enter password: ')
if a == username and b == password:
    print('login successful')
else :
    print('incorrect username or password')'''

# range

'''a = range(4)
b = list(a)
for i in a:
    print(i,end ="\n")'''
#list

'''a = [78 ,34 ,12 ,90 ,33 ,21 ]
for i in a:
    if i % 2 == 0:
        print(f'even :{i}')
    else:
        print(f'odd :{i}')'''

'''a = [1,2,3,4,1,4,5]
c = []
b = len(a)
for i in a:
    for j in range(i+1,b):
        if a[i] == a[j]:
           print(a[i])'''


#while statement
# a = int(input('enter number:'))
'''a = 0
while a < 5:
    print("hello")
    a += 1'''

#functions

'''def greet(name):
    # print(f'hello {name}')
    t = print(f'hello {name}')
name = input('enter the name')
print(t)'''

name = input('enter the name: ')
age = int(input('enter the age: '))
height = int(input('enter the height in cm: '))
height_in_meters = float(height/100)
weight = float(input('enter the weight: '))

bmi = weight/(height_in_meters)**2
print(bmi)
if bmi < 18.5:
    print('under weight')
elif bmi >= 18.5 and bmi <= 24.9:
    print('healthy weight')
elif bmi >= 25.0 and bmi <=29.9:
    print('over weight')
elif bmi >= 30.0 and bmi >= 34.9:
    print('obesity')
else:
    print('severe obesity')