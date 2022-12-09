
#4
import os
def mo_file(x):
    f = open(x,'r', encoding = 'UTF-8')
    print(f.read())
    #5
    #Đóng tệp tin
    f.close()
mo_file(r'D:\data\hjhj.txt')
