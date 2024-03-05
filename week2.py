# Task 1 a program tha accepts users input into a list and sum them up

# numList = []
# total = 0


# while True:
#     numUser = int(input(f"please Enter a number and press enter on your Keyboard :"))
#     numList.append(numUser)
#     another = input('Enter another ? (y/n)')
#     if another == 'y':
#         continue
#     else:
#        break
# for num in numList:
#     total += num
#     print(total)

#Task 2 Tuple
    
# books = ('Reacher','Peter Pan','Lost','James Bond','The Call')
# for book in books:
#     print(type(book))
# print(type(books))


#Task 3 Dictionary
 
# person = {}
  

# name = input("please Enter your name here :")
# Age = int(input(f"please Enter Age here :"))
# bestColor = input(f"please Enter your best color here :")

# person['Name']=name
# person['Age']=Age
# person['best color']=bestColor

# print(person)

#Task 4 sets

# x = {}
# y = {}

# x =input('Enter set of numbers')
# y =input('Enter set of numbers')

# z = x.intersection(y)

# print(set(z))






                            #Assignment

my_list =[]

list = [50,60,70]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list[2]=15

print(my_list)

my_list.extend(list)

print(f"this list: {my_list} is an extended list from List")

sort = sorted(my_list)
print(f"this list:{sort} has been sorted")
print(f"No:{my_list.index(15)} is the index of 30 in the list")












