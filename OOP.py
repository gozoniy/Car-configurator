import time
MM=open("Mmenu.txt","r",encoding="UTF-8").readlines()
men=open("menuO.txt","r",encoding="UTF-8").readlines()
trns=open("transmissions.txt","r",encoding="UTF-8").readlines()
li=open("lights.txt","r",encoding="UTF-8").readlines()
change=open("changes_select.txt","r",encoding="UTF-8").readlines()
class CAR:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def write(self, a,b,c,d,e,f):
        self.color=a
        self.brand=b
        self.model=c
        self.engine=d
        self.transmission=e
        self.lights=f
    def getInfo(self):
        return(self.color+","+self.brand+","+self.model+","+self.engine+","+self.transmission+","+self.lights)
        
#test comment
        
def menu(T): #выбор из файл-меню
    num="t"
    for i in range(len(T)):
        T[i]=T[i].replace("\n","")
    T=list(filter(None,T))
    print(T[0])
    for i in range(1,len(T)):
        if T[i]!="\n":
            print(" "+str(i),") ",T[i],sep="")
    print("\n","-"*10,sep="")
    while not num.isnumeric():
        num=input()
    while not(int(num)) in range(1,len(T)):
        num=input()
    return(int(num),T[int(num)].replace("\n",""))

def stW(file,n,st): #запись в файл n-ой строки
    save=open(file+".txt","r",encoding="UTF-8")
    l=save.readlines()
    save.close()
    
    save=open(file+".txt","w",encoding="UTF-8")
    if st=="":
        l[n]=None
    else:
        l[n]=st+"\n"
    l=list(filter(None,l))
    save.seek(0)
    for i in range(len(l)):
        save.write(l[i])
    save.close()
    print('Успешно сохранено!')   
def ent(t): 
    print('Укажите '+t)
    return input()

ch=0
x1,x2=1,1
while x1:
    M=menu(MM)[0]
    if M==3: break
    if M==1:  #Запись
        if not ch:
            print('Укажите марку и модель')
            br,mo=input().split()
            C1=CAR(br,mo)
        while x2:
            m=menu(men)[0]
            if m==5: break
            if m==1: CAR.color=ent('цвет')
            elif m==2: CAR.engine=ent('двигатель')
            elif m==3: CAR.transmission=menu(trns)[1]
            elif m==4: CAR.lights=menu(li)[1]
        cfg=C1.getInfo()
        if ch: stW("saves/cars",cfg1,time.ctime()[4:]+" - "+str(cfg))
        if not ch:
            save=open('saves/cars.txt',"a+",encoding="UTF-8")
            save.write("\n"+time.ctime()[4:]+" - "+str(cfg))
            save.close()
    if M==2:  #Чтение сохранений
        save=open('saves/cars.txt',"r+",encoding="UTF-8")
        sv=save.readlines()
        if len(sv)<=1: print("Нет сохранений")
        else:
            cfg1=menu(sv)[0]
            chng=menu(change)[0]
            if chng==3: continue
            elif chng==1:
                YY=sv[cfg1].split(" - ")[1].split(",")
                C1=CAR(YY[1],YY[2])
                CAR.color=YY[0]
                CAR.engine=YY[3]
                CAR.transmission=YY[4]
                CAR.lights=YY[5]
                ch=1
            elif chng==2:
                stW("saves/cars",cfg1,"")
#Закадка от Жака Фреско
