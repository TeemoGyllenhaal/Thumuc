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
