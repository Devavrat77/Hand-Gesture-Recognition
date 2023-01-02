def insertion_sort(a):
    for i in range(1,len(a)):
        k = a[i]
        j = i-1
        while(j>=0 and k<a[j]):
            a[j+1] = a[j]
            j = j-1
        a[j+1]=k
    print(a)

def shell_sort(a):
    n = len(a)
    gap = n//2
    while(gap>0):
        for i in range(gap,n):
            t = a[i]
            j = i
            while(j>= gap and a[j-gap]>t):
                a[j] = a[j-gap]
                j = j- gap
            a[j]= t
        gap = gap//2




marks=[] # Creating array


n= int(input("Enter number of marks : "))
for i in range(n):
    temp=float(input(f"enter marks of student {i+1} "))
    marks.append(temp)

#sorting the marks list using insertion sort algorithm
insertion_sort(marks)

# displaying top 5 marks of class
for i in range(5):
    print(marks[i],end=" ")
