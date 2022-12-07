#Liệt kê tất cả thư mục:
import os
def current_path(): 
    print(os.getcwd()) 
    print()
print("Current working directory before") 
current_path()
os.chdir('D:/data')
print("Current working directory after") 
current_path()
path = r'C:\Users\Teemo Gyllenhaal\Documents'
dir_list = os.listdir(path)
print("tất cả file trong", path,":")
print(dir_list)
path = r'D:\data'
tontai= os.path.exists(path)
print(tontai)
path = r'D:\yamero'
tontai= os.path.exists(path)
print(tontai)
#Xóa thư mục
directory = "nnlt2"
parent_dir = "D:/data"
path = os.path.join(parent_dir, directory)
os.rmdir(path)
print("Directory '% s' removed" % directory)