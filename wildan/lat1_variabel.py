# nama = "wildan";
# umur = 80;
# koma = 85.5;
# x=y=z=50;
# # print(nama,koma,x,y,z);
# a,b,c=5,10,15;
# print(a,b,c);

# -----------------
# variabel lokal
# -----------------
# def add():
#     a = 20
#     b = 30
#     c = a+b
#     print('jumlah adalah : ',c)

# add()

# -----------------
# variabel global
# -----------------
x = 10

def add():
    global x
    print(x)

add()
print(x)
del x
# print(x)