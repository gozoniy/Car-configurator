import time
import os
MM=open("Mmenu.txt","r",encoding="UTF-8").readlines()
men=open("menuO.txt","r",encoding="UTF-8").readlines()
trns=open("transmissions.txt","r",encoding="UTF-8").readlines()
li=open("lights.txt","r",encoding="UTF-8").readlines()
lo=open("lock.txt","r",encoding="UTF-8").readlines()
change=open("changes_select.txt","r",encoding="UTF-8").readlines()
class CAR: #Класс параметров машины
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def getInfo(self):
        return(self.color+","+self.brand+","+self.model+","+self.engine+","+self.transmission+","+self.lights+","+self.locked)
        
def menu(T): #выбор из массив-меню
    num="t"
    for i in range(len(T)):
        T[i]=T[i].replace("\n","")
    T=list(filter(None,T))
    print(T[0])
    for i in range(1,len(T)):
        print(" "+str(i),") ",T[i],sep="")
    print("\n","-"*10,sep="")
    while not num.isnumeric():
        num=input()
    while not(int(num)) in range(1,len(T)):
        num=input()
    return(int(num),T[int(num)].replace("\n",""))

def ent(t): 
    print('Укажите '+t)
    q="-, "
    while ("-" in q)or("," in q)or(" " in q):
        q=input()
    return q

ch,x1,x2=0,1,1
C,E,T,LI,LO=0,0,0,0,0
while x1:
    M=menu(MM)[0]
    if M==3: break #Выход
    if M==1:  #Запись
        if not ch: #Запрос имени (если новый)
            print('Укажите марку и модель')
            br,mo=input().split()
            C1=CAR(br,mo)
        while x2:
            m=menu(men)[0]
            if m==6:
                if not(C and E and T and LI and LO): print("Не все данные указаны")
                else: break
            if m==1:
                CAR.color=ent('цвет')
                C=1
            elif m==2:
                CAR.engine=ent('двигатель')
                E=1
            elif m==3:
                CAR.transmission=menu(trns)[1]
                T=1
            elif m==4:
                CAR.lights=menu(li)[1]
                LI=1
            elif m==5:
                CAR.locked=menu(lo)[1]
                LO=1
        cfg=C1.getInfo()
        save=open('saves/'+br+"_"+mo+'.txt',"w",encoding="UTF-8")
        save.write(time.ctime()[4:]+" - "+str(cfg))
        save.close()
    if M==2:  #Чтение
        sv=os.listdir("saves")
        sv.insert(0,"Сохранённые авто")
        if len(sv)<=1: print("Нет сохранений")
        else:
            cfg1=menu(sv)[0]
            u=open("saves/"+sv[cfg1],"r",encoding="UTF-8").read()
            print(u)
            chng=menu(change)[0]
            if chng==3: continue
            elif chng==1:
                YY=u.split(" - ")[1].split(",")
                br,mo=YY[1],YY[2]
                C1=CAR(YY[1],YY[2])
                CAR.color=YY[0]
                CAR.engine=YY[3]
                CAR.transmission=YY[4]
                CAR.lights=YY[5]
                CAR.locked=YY[6]
                ch=1
            elif chng==2:
                os.remove("saves/"+sv[cfg1])