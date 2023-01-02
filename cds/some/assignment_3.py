#m=[]
def inp_matrix(r,c):
    m=[]
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"enter element {j+1} in row {i+1}: ")))
        m.append(row)

    return m

def disp_matrix(r,c,m):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
    print()

def addition(r , c , m1 , m2):
    
    add=[]
    for i in range(r):
        row=[]
        for j in range(c):
            sum = m1[i][j] + m2[i][j]
            row.append(sum)
        add.append(row)
    
    return add

def substraction(r , c , m1 , m2):
    sub=[]
    for i in range(r):
        row=[]
        for j in range(c):
            dif = m1[i][j] - m2[i][j]
            row.append(dif)
        sub.append(row)
    
    return sub

def transpose(r,c,m):
    res=[]
    for j in range(c):
        row=[]
        for i in range(r):
            row.append(m[i][j])
        res.append(row)
    
    return res

def multiplication(r1,c1,c2,m1,m2):
    mul=[]
    for i in range(r1):
        add=[]
        for j in range(c2):
            sum=0
            for k in range(c1):
                mult = (m1[i][k])*(m2[k][j])
                sum+=mult
            add.append(sum)
        mul.append(add)
    return mul

print("data for matrix 1 :- ")
r= int(input("Enter number of rows : "))
c = int(input("Enter number of coloums : "))
#inp_matrix(r,c)
m1 = inp_matrix(r,c)
#disp_matrix(r,c,m1)

print("data for matrix 2 :- ")
r1= int(input("Enter number of rows : "))
c1 = int(input("Enter number of coloums : "))
m2 = inp_matrix(r1,c1)
#disp_matrix(r,c,m2)

print("enter choice as  1 for addition \n2 for substraction \n3 for transpose \n 4 for multiplication \n5 for exit ")
flag = True
while flag:
    choice =int(input("Enter your choice : "))
    if choice == 1:
        # performing addition of two matrix m1+m2
        if r1==r and c1 == c:
            print("displaying addition of matrix m1 + m2")
            m_add = addition(r , c, m1 , m2)
            disp_matrix(r, c , m_add)
        else:
            print("the two matrices are not symmetric, \nplease enter row of matrix 1 = row of matrix 2 vice versa for coloumn")
    elif choice ==2:
        #performing substraction of two matrix m1-m2
        print("displaying substraction of matrix m1 - m2 ")
        m_sub = substraction(r , c, m1 , m2)
        disp_matrix(r, c , m_sub)
    elif choice ==3:
        # creating transpose of matrix m1:
        print("displaying transpose of matrix m1")
        m_trans = transpose(r , c, m1)
        disp_matrix(c, r , m_trans)
    elif choice ==4:
        #performing multiplication of two matrix m1*m2
        print("displaying multiplication of matrix m1 * m2 ")
        m_mul = multiplication(r,c,c1, m1 , m2)
        disp_matrix(r, c , m_mul)
    elif choice ==5 :
        flag = False
    else:
        print("You entered invalid choice, try again")




