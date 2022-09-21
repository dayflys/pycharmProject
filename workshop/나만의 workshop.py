num = int(input())
list1= []
for n in range(num):
    x = input()
    list1.append(x)

for i in range(len(list1)-1):
    if len(list1[i]) > len(list1[i+1]):
        list1[i],list1[i+1]=list1[i+1],list1[i]

print(list1)