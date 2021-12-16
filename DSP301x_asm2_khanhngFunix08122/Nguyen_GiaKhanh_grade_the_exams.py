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
#đọc input mở file

def laydong(file):
    lines=file.read().splitlines()
    return(lines)

l=laydong(y)
#đọc file lấy từng dòng trong dữ liệu file vào 1 list

def thongbao(lines):
    z=0
    k=0
    Char=0
    for i in lines :
        if i.count(",") == 25 :
            z=z+1
        else :
            k=k+1
            print("Invalid line of data: does not contain exactly 26 values:",i,sep='\n')
    #kiểm tra các dòng có đủ 26 phần tử không (tính cả mã sinh viên) bằng cách đếm dấu phẩy

    print("**** ANALYZING ****")

    for i in lines :
        m = i.split(",")
        if len(m[0]) != 9 :
            z=z-1
            k=k+1
            print("Invalid line of data: N# is invalid :",i,sep='\n')
        #kiểm tra mã sinh viên đủ kí tự không
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
        #kiểm tra nếu mã sinh viên đủ kí tự thì đã đúng cấu trúc mã sinh viên chưa

    if k==0 :
             print("No errors found!")

    print('**** REPORT ****')
    print("Total valid lines of data:",z)
    print("Total invalid lines of data:",k)
    
#toàn bộ hàm này chỉ để output ra thông báo các dòng không hợp lệ và đếm các dòng hợp lệ và không hợp lệ

thongbao(l)

def listcautraloihople(lines):
    lst=[]
    for i in lines :
        if i.count(",") == 25 :
            lst.append(i)
    return(lst)
#kiểm tra các dòng có đủ 26 phần tử không (tính cả mã sinh viên) nếu đủ thì cho dòng dữ liệu sv đó vào list(lst)
a=listcautraloihople(l)

def listhople(lst):
    for i in lst :
        #vì mỗi dòng dữ liệu sv trong list(lst) đang là 1 phần tử
        #nên cách này làm cho mỗi dòng thành 1 list và thành phần trong dòng đó thành 1 phần tử ngăn cách bởi dấu phẩy
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
        #nếu mã sv không hợp lệ thì dòng đó bị remove khỏi list(lst)
    return(lst)


b=listhople(a)


def chamdiem(lst):
    dapandebai = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = dapandebai.split(',')
    #vì đáp án đề bài đang ở dạng str nên biến về sang dạng list
    diemHS=[]
    for i in lst :
        m = i.split(",")
        #vẫn là biến các dữ liệu của 1 dòng thành từng phần tử
        k=m[1:]
        #bỏ qua phần tử đầu chính là mã sv để chỉ lấy câu trả lời của sv
        z=0
        #z số sẽ tiếp tục nhảy để so sánh từ phần tử thứ 1 đến hết giữa câu trả lời sv với đáp án
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
        #cho mã sv và điểm của sv đó vào j
        diemHS.extend(j)
        #cho các phần tử của j vào list(diemHS)
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
#vì điểm SV trong list(diemHS) là phần tử loại integer không viết vào file được nên phải chuyển sang string
o=strdiemHS(c)


def grade(classgrade) :
    filename2 = filename.replace(".txt", "_grades.txt")
    with open(filename2,'w+') as f:
        f.write('\n'.join((o)))
#ghi mã sv và điểm sv ra 1 file mới
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
#lấy điểm đã chấm từ list(diemHS) loại bỏ mã sv cho vào list(diemcham)
d=diemcham(c)

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

#tính mean, median, range, tìm Highest, Lowest
e=TB(d)
