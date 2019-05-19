#in this function we are taking a word and finding its position in each file. the positions are in a list format. if list is empty then that word is not present in file
def PosIndex(word):

    file1 = open('corpus/austen-emma.txt', 'r')
    File1 = list(file1.read().split())

    file2=open('corpus/austen-persuasion.txt', 'r')
    File2 = list(file2.read().split())

    file3 = open('corpus/chesterton-brown.txt', 'r')
    File3 = list(file3.read().split())

    file4=open('corpus/austen-sense.txt', 'r')
    File4 = list(file4.read().split())

    file5 = open('corpus/bible-kjv.txt', 'r')
    File5 = list(file5.read().split())

    file6=open('corpus/blake-poems.txt', 'r')
    File6 = list(file6.read().split())

    file7 = open('corpus/bryant-stories.txt', 'r')
    File7 = list(file7.read().split())

    file8=open('corpus/burgess-busterbrown.txt', 'r')
    File8 = list(file8.read().split())

    file9 = open('corpus/carroll-alice.txt', 'r')
    File9 = list(file9.read().split())

    file10=open('corpus/chesterton-ball.txt', 'r')
    File10 = list(file10.read().split())

    first=[]
    second=[]
    third=[]
    fourth=[]
    fifth=[]
    sixth=[]
    seventh=[]
    eighth=[]
    ninth=[]
    tenth=[]
    list3=[[File1,first],[File2,second],[File3,third],[File4,fourth],[File5,fifth],[File6,sixth],[File7,seventh],[File8,eighth],[File9,ninth],[File10,tenth]]
    new=[]
    temp=[]
    for i in list3:
        if word in i[0]:
            for position, name in enumerate(i[0]):
                if name == word:
                    temp.append(position)
        new.append(temp)
        temp=[]
    return new


def check(word):#this function takes in a phrase and breaks into words. Then each words position and file are stored. Once that is done we check the phrases one by one in each doc and match positions
    word=word.split()
    allList=[]
    for i in word:
        allList.append(PosIndex(i))
    count=0
    print("Begining search for phrase...")
    for j in range(len(allList[0])):
        if len(allList[0][j])!=0:
            for k in allList[0][j]:
                if (len(word)==3):

                    if k+1 in allList[1][j] and k+2 in allList[2][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==4):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==5):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==6):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j] and k+5 in allList[5][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==7):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j] and k+5 in allList[5][j] and k+6 in allList[6][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==8):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j] and k+5 in allList[5][j] and k+6 in allList[6][j] and k+7 in allList[7][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==9):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j] and k+5 in allList[5][j] and k+6 in allList[6][j] and k+7 in allList[7][j] and k+8 in allList[8][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))

                elif (len(word)==10):
                    if k+1 in allList[1][j] and k+2 in allList[2][j] and k+3 in allList[3][j] and k+4 in allList[4][j] and k+5 in allList[5][j] and k+6 in allList[6][j] and k+7 in allList[7][j] and k+8 in allList[8][j] and k+9 in allList[9][j]:
                        count=count+1
                        print("Found phrase in file "+str(j+1) + " and at position " + str(k))


    if count==0:
        print("Phrase not found \n \n")



b=True
while(b):
    print("\nTo exit enter 'e'")
    a=input("Please enter more than 2 word phrase to start search:\n")
    if a=="e":
        b=False
        break
    check(a.lower())
