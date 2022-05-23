import random
def check(mangija,plats):
    roll = 1
    kaardinumber = 2
    suurim = 0
    score = 0
    P = 0
    A = 0
    R = 0
    RI = 0
    mangus = mangija + plats
    while roll != 7:
        for i in mangus:
            if int(i[0]) > suurim:
                suurim = int(i[0])
    score += suurim
    for x in mangus:
        if x[1] == "P":
            P += 1
        elif x[1] == "A":
            A += 1
        elif x[1] == "R":
            R += 1
        elif x[1] == "RI":
            RI += 1
        if P >= 5 or A >= 5 or R >= 5 or RI >= 5:
            score += 1000
    while kaardinumber != 15:
        for y in mangus:
            
        
"""P=poti A=artu R=ruutu RI=risti"""
paarid = [['14','P'],['2','P'],['3','P'],['4','P'],['5','P'],['6','P'],['7','P'],['8','P'],['9','P'],['10','P'],['11','P'],['12','P'],['13','P'],['14','A'],['2','A'],['3','A'],['4','A'],['5','A'],['6','A'],['7','A'],['8','A'],['9','A'],['10','A'],['11','A'],['12','A'],['13','A'],['14','R'],['2','R'],['3','R'],['4','R'],['5','R'],['6','R'],['7','R'],['8','R'],['9','R'],['10','R'],['11','R'],['12','R'],['13','R'],['14','RI'],['2','RI'],['3','RI'],['4','RI'],['5','RI'],['6','RI'],['7','RI'],['8','RI'],['9','RI'],['10','RI'],['11','RI'],['12','RI'],['13','RI']]
for x in paarid:
   paarid.remove(x)
   kaardid = [['14','P'],['2','P'],['3','P'],['4','P'],['5','P'],['6','P'],['7','P'],['8','P'],['9','P'],['10','P'],['11','P'],['12','P'],['13','P'],['14','A'],['2','A'],['3','A'],['4','A'],['5','A'],['6','A'],['7','A'],['8','A'],['9','A'],['10','A'],['11','A'],['12','A'],['13','A'],['14','R'],['2','R'],['3','R'],['4','R'],['5','R'],['6','R'],['7','R'],['8','R'],['9','R'],['10','R'],['11','R'],['12','R'],['13','R'],['14','RI'],['2','RI'],['3','RI'],['4','RI'],['5','RI'],['6','RI'],['7','RI'],['8','RI'],['9','RI'],['10','RI'],['11','RI'],['12','RI'],['13','RI']]
   for y in paarid:
        kaardid.remove(x)
        kaardid.remove(y)
        paar = [x,y]
        roll = 0
        while roll != 100:
            random.shuffle(kaardid)
            mangija1 = [kaardid[0],kaardid[1]]
            mangija2 = [kaardid[2],kaardid[3]]
            mangija3 = [kaardid[4],kaardid[5]]
            mangija4 = [kaardid[6],kaardid[7]]
            mangija5 = [kaardid[8],kaardid[9]]
            mangija6 = [kaardid[10],kaardid[11]]
            platsikaardid = [[kaardid[12],kaardid[13],[kaardid[14],kaardid[15],[kaardid[16]]
            if 
            
            
   paarid += ["empty"]


'''
   while "A" in kaardid[0] or "P" in kaardid[0] or "R" in kaardid[0] or "RI" in kaardid[0]:
      random.shuffle(kaardid)
      if "empty" in kaardid:
          kaardid.remove("empty")
      kaardid.remove(kaardid[0])
      print(kaardid)
      kaardid += ["empty"]
'''
print('keeks')
                
