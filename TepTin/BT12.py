#1
#Đọc văn bản
def doc_van_ban(x):
    f = open(x,'r')
    z = f.read()
    print (z)
doc_van_ban(r'D:\data\hjhj.txt')
#2
#Ghi văn bản
def ghi_van_ban(x):
    with open(x,'a') as f:
        f.write('\n')
        f.write("huhu\n")
        f.write("yameroo\n")
        f.close()
ghi_van_ban(r'D:\data\hjhj.txt')