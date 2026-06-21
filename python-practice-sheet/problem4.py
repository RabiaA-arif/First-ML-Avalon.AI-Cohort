# count even and odd using list comprehension
list = [2,3,13,12,14,16,11,10]
# for i in range(5):
#     input_list = int(input("Enter the number:"))
#     list.append(input_list)

list_input = ["even"  if x % 2 == 0 else "odd" for x in list]
print(list_input)
# print(list)
even = 0
odd = 0
for j in list_input:
    # print(j)
    if j == 'even':
        even+=1
    else:
        odd+=1


print(f"output : Even:{even} , Odd:{odd}")
