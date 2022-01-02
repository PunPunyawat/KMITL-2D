class Queue:
    def __init__(self) :
        self.men=[];
        self.women = [];
        self.activity = ["Eat","Game","Learn","Movie"];
        self.location = ["Res.","ClassR.","SuperM.","Home"];
        
        self.parkmen=""
        self.Acmen=0 ; self.Lomen=0; self.Acwomen=0; self.Lowomen=0
        self.realAcMen=[]; self.realLoMen=[]
        self.realAcWoMen=[]; self.realLoWoMen=[]
        self.saveprintMEN=[]
        self.saveprintWOMEN=[]
        self.loveScore=0;
        #------------------------
 
    def enQueue(self,i,j):
        self.men.append(i);
        self.women.append(j);
     
q = Queue();
inpt = input("Enter Input : ").split(",")   # แต่ละวัน

for i in inpt:
    tempmen,tempwomen = i.split()
    q.enQueue(tempmen,tempwomen)
    
for i in q.men:
    tempAcmen,tempLomen = str(i).split(":")
    q.Acmen=int(tempAcmen); q.Lomen=int(tempLomen);
    parkmen = q.activity[q.Acmen]+":"+q.location[q.Lomen]

    q.realAcMen.append(q.activity[q.Acmen])
    q.realLoMen.append(q.location[q.Lomen])

    q.saveprintMEN.append(parkmen)

for i in q.women:
    tempAcmen,tempLomen = str(i).split(":")
    q.Acwomen=int(tempAcmen); q.Lowomen=int(tempLomen)
    parkmen = q.activity[q.Acwomen]+":"+q.location[q.Lowomen];

    q.realAcWoMen.append(q.activity[q.Acwomen])
    q.realLoWoMen.append(q.location[q.Lowomen])

    q.saveprintWOMEN.append(parkmen);

#----------------
print("My   Queue =",", ".join(q.men))
print("Your Queue =",", ".join(q.women))
print("My   Activity:Location =",", ".join(q.saveprintMEN))
print("Your Activity:Location =",", ".join(q.saveprintWOMEN))

for i in range(len(inpt)):
    if(q.realAcMen[i]==q.realAcWoMen[i] and q.realLoMen[i] != q.realLoWoMen[i]):
        q.loveScore+=1;
    elif(q.realAcMen[i]!=q.realAcWoMen[i] and q.realLoMen[i] == q.realLoWoMen[i]):
        q.loveScore+=2;
    elif(q.realAcMen[i]==q.realAcWoMen[i] and q.realLoMen[i] == q.realLoWoMen[i]):
        q.loveScore+=4;
    else:
        q.loveScore-=5;

if(q.loveScore>=7):
    print("Yes! You're my love! : Score is "+str(q.loveScore)+".")
elif(q.loveScore>0 and q.loveScore<7):
    print("Umm.. It's complicated relationship! : Score is "+str(q.loveScore)+".")
else:
    print("No! We're just friends. : Score is "+str(q.loveScore)+".")    





