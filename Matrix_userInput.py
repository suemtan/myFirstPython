# implementation for taking user input matrix


def takeuserInput(rows,columns):
    #initialize matrix
    matrix=[]

    print("Enter entries by row : ")

    # create matrix with rows and columns
    # for row
    for i in range(rows):
        a =[]

        #for column
        for j in range(columns):
            a.append(int(input()))
        matrix.append(a)

    #print matrix
    for r in range(rows):
        for c in range(columns):
            print(matrix[r][c]),
        print(" ")




# main function
if __name__=="__main__":

    rows = int(input("Enter number of rows : "));
    columns = int(input("Enter number of columns : "));


    takeuserInput(rows, columns);


