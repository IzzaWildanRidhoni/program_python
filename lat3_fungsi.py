def cekKabisat(tahun):
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400)== 0:
                print ("Tahun kabisat")
            else:
                print ("bukan tahun kabisat")
        else:
            print ("tahun kabisat")
    else:
        print (" bukan tahun kabisat")
    

tahun = int(input("masukkan tahun : "))
cekKabisat(tahun)

