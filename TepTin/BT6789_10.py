#6
def mo_bang_cau_truc(x):
    try:
        f = open(x,'r', encoding = 'UTF-8')
        print(f.read())
    finally:
        f.close()
mo_bang_cau_truc(r'D:\data\hjhj.txt')
#7
def mo_bang_cau_truc_2(x):
    with open(x,'r',encoding = 'UTF-8') as f:
        print(f.read())
        f.close()
mo_bang_cau_truc_2(r'D:\data\hjhj.txt')
#8 
def viet_tep_tin(x):
    with open(x,'w',encoding = 'UTF-8') as f:
        f.write("\n")
        f.write("Chuc mung\n")
        f.write("nam moi\n")
        f.write("an khang thinh vuong\n")
        f.close()
viet_tep_tin(r'D:\data\hjhj.txt')
#9
mo_bang_cau_truc_2(r'D:\data\hjhj.txt')
#10
def mo_file_anh(x):
        f = open(x,'r+b')
        print(f.read())
        f.close()
mo_file_anh(r'D:\data\1282975.jpg')