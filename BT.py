#Đọc văn bản
f = open(r'D:\data\hjhj.txt')
z = f.read()
print (z)
#Ghi văn bản
with open(r'D:\data\hjhj.txt','w') as f:
    f.write("huhu\n")
    f.write("yameroo")

