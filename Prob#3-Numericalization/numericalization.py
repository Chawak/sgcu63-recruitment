
digitprintcode=[[0,3,3,3,0],[1,1,1,1,1],[0,1,0,2,0],[0,1,0,1,0],[3,3,0,1,1],[0,2,0,1,0],[0,2,0,3,0],[0,1,1,1,1],[0,3,0,3,0],[0,3,0,1,0]]
def writeline(printcode,number,x): #print each line of each digit
    #fullrow
    if printcode==0:
        print(str(number)*5*x,end=" ")        
    #right
    elif printcode==1:
        print(" "*x*4+str(number)*x,end=" ")
    #left    
    elif printcode==2:
        print(str(number)*x+" "*x*4,end=" ")
    #bothside    
    elif printcode==3:
        print(str(number)*x+" "*x*3+str(number)*x,end=" ")
num,y,x=input().split()
y=int(y)
x=int(x)
digit=[]
for i in num:
    digit+=[int(i)]
for i in range(5):
    for j in range(y):
        for k in Lnum:
            writeline(digitprintcode[k][i],k,x)
        print("")
