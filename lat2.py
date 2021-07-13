data=input("masukan kalimat dalam bentuk angka ");
jml=0;

if not  data.isdigit():                                       
    print("yang dimasukan bukan  angka");          
else:                                             
    for i in range(0,len(data)):
          jml=jml+int(data[i]);
    print(" jumlah total ",jml);