def makeTable(string):
    new=[]
    table=[]
    alpha=list(string)
    start=0
    for i in alpha:
        if i not in new:
            new.append(i)
    table.append(new)
    for i in range(len(string)):
        table.append([])        
        for j in range(len(new)):
            table[i+1].append(0)
    for k in range(len(string)):
        word=alpha[k]
        index=new.index(word)
        table[k+1][index]=k+1
    return(table)


def nameFind(f,table):
    stri=[]
    for i in range(1,len(table)):
        ind=table[i].index(i)
        stri.append(table[0][ind])
    string=''.join(stri)
    finalans=""
    file = open(f, "r") 
    array=file.readlines()
    for i in range(1,len(array)+1):
        new=array[i-1]
        new=new.split()
        if string in new:
            finalans=finalans+"  "+str(i)
    print("The table is: ")
    print(table)
    print("\n")
    print("The lines are:\n"+finalans)


a=makeTable("wahaj")
nameFind("test.txt",a)
