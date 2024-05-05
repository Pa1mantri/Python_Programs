#magic square information https://en.wikipedia.org/wiki/Magic_square

def matrix(n):
    

    matrix =[]                #creates a empty list by the name matrix
    for i in range(n):        #The outer loop iterates to create 3 rows
        l=[]                  # creates an empty list by name l
        for j in range(n):    #inner loop creates 3 columns in the matrix for each row
            l.append(0)
            #print(matrix)
        matrix.append(l)      # This commands adds a row to the matrix.
    
    i = n//2
    j = n-1
    
    num = n*n
    count=1
    
    while(count<=9):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i<0):
                i = n-1
        if(matrix[i][j]!=0):
            j=j-2
            i=i+1
            continue
        
        else:
            matrix[i][j]=count
            count+=1
        i=i-1
        j=j+1
          
    #The below loop helps in printing each element of the matrix   
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")  #this will print all the elements in one row
        print()                          # to make it look like a matrix this statement
                                        #includes next line after every row.
matrix(3)  
