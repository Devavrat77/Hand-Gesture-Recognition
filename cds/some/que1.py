marks_list = []
new_list =[]

def absent_present(Total_students):
        # n = number of students in class        
    for students in range(Total_students):
        mark = int(input("Enter mark (enter -999 if absent ) : "))
        marks_list.append(mark)
    present = 0
    for marks in marks_list:
        if marks != -999:
            present +=1
            new_list.append(marks)
        # absent = Total_students - present
        #print(f"Absent students are {absent }. \nPresent students are {present}. \nMarks of students are {new_list} \n")
        #present_mark_list = new_list.copy()
    return present

def average( new_list  ):
    avg=0
    # present = absent_present(Total_students)
    for i in new_list:
        avg += (i/present) 
    #print("Average marks of class are : ",end="")
    return avg

def max_marks(new_list):
    maximum = 0
    for mark in new_list:
        if mark > maximum:
            maximum = mark
    return maximum

def min_marks(new_list):
    minimum = 100
    for mark in new_list:
        if mark <= minimum:
            minimum = mark
    return minimum

def freq(new_list):
    unique = list(set(new_list))
    count = 0 
    ind = 0
    for i in unique:
        if count <= new_list.count(i):
            count = new_list.count(i)
            ind = unique.index(i)
        else :
            continue
    return unique[ind]


    
Total_students = int(input("Enter total number of students : "))
present = absent_present(Total_students)


a = True
while a:

    print("\nEnter :\n 1 for Average\n 2 for highest and lowest marks\n 3 for number of absent and present students\n 4 for marks with maximum frequency\n 5 to exit\n")
    choice = int(input())

    if choice == 1:
        
        # Total_students = int(input("Enter total number of students : "))
        # present = absent_present(Total_students)

        Average = average(new_list)
        print("Average marks of class are ", Average)
        continue

    elif choice ==2:
        
        # Total_students = int(input("Enter total number of students : "))
        # present = absent_present(Total_students)

        maximum = max_marks(new_list)
        minimum = min_marks(new_list)

        print(f"Maximum marks in class are {maximum}. \nMinimum marks in class are {minimum}")
        continue

    elif choice ==3:
        
        # Total_students = int(input("Enter total number of students : "))
        # present = absent_present(Total_students)

        absent = Total_students - present

        print(f"Absent students are {absent }. \nPresent students are {present}.\n")
        continue
    
    elif choice == 4:
        
        # Total_students = int(input("Enter total number of students : "))
        # present = absent_present(Total_students)

        frequency = freq(new_list)
        print(f'the marks with the maximum frequency are {frequency}')
        continue
    
    elif choice==5:
        a=False

    else:
        print("You entered wrong choice ")
        continue
