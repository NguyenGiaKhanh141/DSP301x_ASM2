import statistics as s
filename=input()
def mofile():
    try:
        file=open(filename,"r")
        print("Successfully opened",filename)
        return(file)
    except:
        print("File cannot be found")

y=mofile()

def laydong(file):
    lines=file.read().splitlines()
    #print(lines)
    return(lines)

l=laydong(y)

def thongbao(lines):
    z=0
    k=0
    Char=0
    for i in lines :
        if i.count(",") == 25 :
            z=z+1
        else :
            k=k+1

    print("**** ANALYZING ****")

    for i in lines :
        if i.count(",") != 25 :
            print("Invalid line of data: does not contain exactly 26 values:",i,sep='\n')
    for i in lines :
        m = i.split(",")
        if len(m[0]) != 9 :
            z=z-1
            k=k+1
            print("Invalid line of data: N# is invalid :",i,sep='\n')
        elif len(m[0]) ==9 :
            p=m[0]
            n=p[1:]
            if p[0]=='N':
                for char in n:
                  if  char.isalpha():
                    z=z-1
                    k=k+1
                    print("Invalid line of data: N# is invalid :",i,sep='\n')
            elif p[0]!='N':
                z=z-1
                k=k+1
                print("Invalid line of data: N# is invalid :",i,sep='\n')

    if k==0 :
             print("No errors found!")

    print('**** REPORT ****')
    print("Total valid lines of data:",z)
    print("Total invalid lines of data:",k)


thongbao(l)

def listcautraloihople(lines):
    lst=[]
    for i in lines :
        if i.count(",") == 25 :
            lst.append(i)
    return(lst)
# a=listcautraloihople(l)
# print(len(a))


def listhople(lst):
    for i in lst :
        m = i.split(",")
        if len(m[0]) != 9 :
            lst.remove(i)
        elif len(m[0]) == 9 :
            p=m[0]
            n=p[1:]
            if p[0]=='N':
                for char in n:
                  if  char.isalpha():
                    lst.remove(i)
            elif p[0]!='N':
                lst.remove(i)
    return(lst)



a=listcautraloihople(l)

b=listhople(a)
# print(len(listhople(a)))

def chamdiem(lst):
    dapandebai = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = dapandebai.split(',')
    diemHS=[]
    for i in lst :
        m = i.split(",")
        k=m[1:]
        z=0
        diem=0
        for l in k:
            if k[z]== answer_key[z]:
               diem=diem+4
            elif k[z]== '':
               diem=diem
            else :
               diem=diem-1
            z=z+1
        j=[m[0],diem]
        diemHS.extend(j)
    return(diemHS)

c=chamdiem(b)

def strdiemHS(diemHS):
    z=0
    diemHSstr=[]
    for i in c:
        if type(c[z])==int:
            k=str(i)
            diemHSstr.append(k)
            z=z+1
        elif type(c[z])==str:
            diemHSstr.append(i)
            z=z+1
    return(diemHSstr)

o=strdiemHS(c)
#print(o)

def grade(classgrade) :
    filename2 = filename.replace(".txt", "_grades.txt")
    with open(filename2,'w+') as f:
        f.write('\n'.join((o)))


m=grade(o)

def diemcham(c):
    diemcham=[]
    z=0
    for i in c:
        if type(c[z])==int:
            diemcham.append(i)
            z=z+1
        elif type(c[z])==str:
            z=z+1
    return(diemcham)

d=diemcham(c)
#print(d)

def TB(diemcham):
    a=s.mean(d)
    a=round(a,2)
    print("Mean (average) score:",a)
    print("Highest score:",max(diemcham))
    print("Lowest score:",min(diemcham))
    print("Range of scores:",max(diemcham)-min(diemcham))
    b=s.median(diemcham)
    b=round(b,2)
    print("Median score:",b)


e=TB(d)
