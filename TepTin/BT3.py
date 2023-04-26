#3
import os
def mo_va_viet_tep_tin_nhi_phan(x):
    f = open(x,'r+b')
    with open(x,'r+b') as f:
        print(f.read(1))
        print(f.read(3))
        print(f.read(2))
        print(f.read(1))
        print(f.read(1))
    f.close()
    f = open(x,'w+b')
    sentence = bytearray("Viet tep nhi phan".encode("ascii"))
    f.write(sentence)
    f.close()
mo_va_viet_tep_tin_nhi_phan(r'D:\data\While.drawio.png')
