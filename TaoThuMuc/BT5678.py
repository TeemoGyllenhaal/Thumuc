#câu 5
#Liệt kê tất cả thư mục:
import os
def liet_ke(x):
    path = x
    dir_list = os.listdir(path)
    print("tất cả file trong", path,":")
    print(dir_list)
liet_ke(r'C:\Users\Teemo Gyllenhaal\Documents')
#câu 6
#Kiểm tra tồn tại thư mục hay không
def kiem_tra(x):
    path = x
    tontai= os.path.exists(path)
    print(tontai)
kiem_tra(r'D:\data')
#7
#Xóa thư mục
def xoa_thu_muc(x,y):
    directory = x
    parent_dir = y
    path = os.path.join(parent_dir, directory)
    os.rmdir(path)
    print("Thư mục '% s' đã xóa tại: " % directory)
xoa_thu_muc(r"nnlt2",r"D:/data")