#câu 1
import os
#câu 2
cwd = os.getcwd()
print (cwd)
def current_path(): 
    print(os.getcwd()) 
    print()
print("Thư mục hiện tại")
current_path()
#câu 3
def chuyen_thu_muc():
    print("Vị trí làm việc trước đây") 
    current_path()
    os.chdir('D:/data')
    print("Vị trí làm việc sau khi thay đổi") 
    current_path()
chuyen_thu_muc()
#câu 4
#Tạo thư mục:
directory = "nnlt2"
parent_dir = "D:/data"
path = os.path.join(parent_dir, directory)
os.makedirs(path) 
print("Tập tin '% s' đã được tạo tại:" % directory)
