print("Please enter a sentence")
value = input()
result = ""
myList=value.split(' ')
if(myList.count('is')>0 or myList.count('IS')>0 or myList.count('are')>0 or myList.count('ARE')>0):
    result = "present Tense"
elif (myList.count('was')>0 or myList.count('WAS')>0 or myList.count('were')>0 or myList.count('WERE')>0 or myList.count('did')>0 or myList.count('had')>0 or myList.count('have been')):
    result = "past Tesnse"
elif (myList.count('will')>0 or myList.count('WILL') or myList.count('SHALL')>0 or myList.count('shall')):
    result = "future Tense"
print(result)
