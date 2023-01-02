#Selection sort algorithm 
def selection_sort(a,m):        #a = array , m= len(a)
    for i in range(m):
        min_index = i
        for j in range(i+1,m):
            if a[j]<a[i]:
                min_index = j
        a[min_index], a[i] = a[i] , a[min_index]
    print(a)

#bubble sort algotithm
def bub_sort(a,m):
    for i in range(0,m-1):
        for j in range(0,m-i-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]= a[j+1], a[j]
    print(a)

def insertion_sort(a):
    for i in range(1,len(a)):
        k = a[i]
        j = i-1
        while(j>=0 and k<a[j]):
            a[j+1] = a[j]
            j = j-1
        a[j+1]=k
    print(a)


a = []
n= int(input("enter length of array : "))
for i in range(n):
    a.append(int(input(f"Enter element number {i+1} : ")))

print("Choices : \n1. Selection sorting \n2. Bubble sorting \n3. Insertion sorting \n4. Exit")

flag = True
while flag:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        selection_sort(a,len(a)) 
    elif choice == 2:
        bub_sort(a,len(a))
    elif choice ==3:
        insertion_sort(a)
    elif choice == 4:
        flag = False
    else:
        print("You entered wrong choice ")
        print("\n program ended ")
        flag = False

