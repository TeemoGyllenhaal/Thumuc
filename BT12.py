#Đọc văn bản
f = open(r'D:\data\hjhj.txt','r')
z = f.read()
print (z)
#Ghi văn bản
with open(r'D:\data\hjhj.txt','a') as f:
    f.write("huhu\n")
    f.write("yameroo\n")
f.close()
