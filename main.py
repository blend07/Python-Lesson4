# Challenge
# numbers = [1 , 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9,]

# uniquelist = set(numbers)

# print(uniquelist)

# message= input("Type your message here: ")

# print(message)

#for loop

# numbers = [1,2,3,4,5,6,7,8,9]

# for num in numbers:
#     if num %2 == 0:
#         print(num)
# print("Keta numra jane qift")

# first_name = "Blend"

# for char in first_name:
#     print(char)

dictionarie_name = {"Blend" : 4, "Suela" : 5, "Darsej" : 1, "Leoni":3}

values = dictionarie_name.values()
totalsum=0
for value in values:
    print(value)
    totalsum+= value
    print("Shuma totale eshte:", totalsum)

for key in dictionarie_name.keys():
    print(key)

for i in range(1,10):
    print(i)

numrat = [1, 242, 432, 63, 62, 3, 123, 66, 32, 21, 92]
largest_num = numrat[0] #1

for num in numrat:
    if num > largest_num:
        largest_num = num
print(largest_num)

count = 0

while count <= 5:
    print(count)
    count +=