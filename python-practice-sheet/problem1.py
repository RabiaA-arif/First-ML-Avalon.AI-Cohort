# Breaking the Record
import array as arr 
n: int = 6
score = arr.array('i',[12,33,10,5,3,31])
for i in range(n):
    print(score[i])
    for j in range(i+1):
        print(i)

