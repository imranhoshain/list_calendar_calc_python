#Nested List
print("Nested List Program")
nlist1 = ['1', '5', ['10', '6', ['8', '4']], '0', '9']
print(nlist1[0])
print(nlist1[4])


#length
print("Length Program")
A=[3,7,6,8,0,5]
print(len(A))
Name=["Imran","Hoshain"]
N=len(Name)
print(N)

#Concate
print("Concate Program")
list1 = [0, 1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = list1 + list2
print ("Concatenated list: " + str(result))

#Membership
print("Membership Program")
x = 20
y = 10
list = [10, 50,60,80,70]
if (x not in list):
    print("X is Not present in given list")
else :
    print("x is present in given list")
if (y in list):
    print("y is present in given list")
else:
    print("y is not present in given list")


#Iteration
print("Iteration Program")
list = [1,2,5,8,6,4]

for i in list:
    print(i)
list = [2,5,8,9]
length=len(list)
for i in range(length):
    print(list[i])



#Indexing
print("Indexing Program")
name = "Imran Hoshain Dev"
if(name[0].islower()):
    name =name.capitalize()
    print(name)
first_name= name[0:7].upper()
second_name=name[8:16].lower()
print(first_name)
print(second_name)

#Slicing
print("Slicing Program")
name = "Imran Hoshain"
name= name[0:10:2]
print(name)

