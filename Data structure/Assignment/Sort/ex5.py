"""
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68

"""
class LeagueScore_sort:
    def __init__(self,name,win,loss,draw,score,conced):
        self.name = name
        self.totalp = (3*win) +(0*loss)+ draw
        self.gd = score-conced

    def __str__(self):
        return '[\''+self.name+'\'' + ', {\'points\': '+str(self.totalp)+'}, {\'gd\': '+str(self.gd) + '}]'

def bubble_sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j].totalp < l[j+1].totalp:
                l[j],l[j+1] = l[j+1],l[j]  
            elif l[j].totalp == l[j+1].totalp:
                if l[j].gd < l[j+1].gd:
                    l[j],l[j+1] = l[j+1],l[j]         
    return l

# s = [str(e).split(",") for e in input("Enter Input : ").split('/')]  fast input 
temp=[]
inp = input("Enter Input : ").split("/")

for i in inp:
    temp.append(i.split(","))

lss = [ LeagueScore_sort(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5])) for i in temp]
print("== results ==\n"+  "\n".join([str(e) for e in bubble_sort(lss)]))
