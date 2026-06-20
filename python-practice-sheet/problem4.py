# count even and odd using list comprehension
list = []
for i in range(5):
    input_list = int(input("Enter the number:"))
    list.append(input_list)
    
list_input = [j%2==0 for j in len(list)]
print(list_input)
# print(list)
