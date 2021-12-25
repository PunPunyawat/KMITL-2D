print("*** Converting hh.mm.ss to seconds ***");
inputall = input("Enter hh mm ss : ")
numH,numM,numS = inputall.split() # ต่อ input 
numH=int(numH);
numM=int(numM);
numS=int(numS);

changetomi = numH * 60;
changetoSec = (changetomi+numM) * 60;
total = changetoSec + numS;


if(numH<0):
    print("hh("+str(numH)+") is invalid!")
    exit()
    
if(numM>=60 or numM<0):
    print("mm("+str(numM)+") is invalid!")    
    exit()

if(numS<0 ):
    print("mm("+str(numS)+") is invalid!")    
    exit()   


if(int(numH)<=9):
    numH="0"+str(numH);
if(int(numM)<=9):
    numM="0"+str(numM);
if(int(numS)<=9):
    numS="0"+str(numS);

print(str(numH)+":"+str(numM)+":"+str(numS)+" = "+str(f'{total:,}')+" seconds");