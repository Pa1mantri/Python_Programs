//sorting the elements in a list in ascending order and finding the median.

marks=[70,49,39,58,86,48,98,58,98,38,99,88,76,87,10,1]

rangee = len(marks)
print(rangee)

for i in range(rangee-1):
    #print(i)
    for j in range(rangee-i-1):
        if marks[j] >= marks[j+1]:
            marks[j],marks[j+1]=marks[j+1],marks[j]
            #print(marks)

if rangee%2 ==0:
    M1 = marks[int(rangee/2)]
    M2 = marks[int((rangee/2)-1)]
    print(M2)
    print(M1)
    print((M1+M2)/2)        # if n is even, get the arithmetic mean of the two middle elements
else:
    print(marks[int(rangee/2)])        # if n is odd, the middle element is the median

