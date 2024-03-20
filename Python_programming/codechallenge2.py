integers = input("Enter integers")
integerLists = list(integers)
 
 
# using loop
for i in range(0, len(integerLists)):
    integerLists[i] = int(integerLists[i])
 
# Printing modified list
print("Sum of list entered is : " + str(sum(integerLists)))


favorite_books = ("Born a Crime", "The Lean startup", "The making of a manager", "Steps to Christ")
for book in favorite_books:
    print (book)

person_details = {}
person_details["name"] = input("What is your name: ")
person_details["age"] = input("How old are you: ")
person_details["favorite_color"] = input("What is your favorite color: ")

print (person_details)

integer1 = input("Enter integers")
integer_set = set(integer1)
print(integer_set)
integer2 = input("Enter integers")
integer_set2 = set(integer2)
print (integer_set2)

print("The common numbers in the two sets are", integer_set2.intersection(integer_set))

words = ["come", "go", "peter", "bring", "Monday", "water"]
odd_number_characters = [word for word in words if len(word) % 2 != 0 ]
print(odd_number_characters)