#Nama   : Zaki Makhasin
#NPM    : 5200411247

#Kalkulator Penghitung Depresiasi

#Membuat Form Input
print("\n")
print("Kalkulator Penghitung Depresiasi ! \n")
biaya = float(input("Harga Perolehan \t : "))
umur = int(input("UE (Tahun) \t\t : "))
awal = int(input("Tahun Ke (Awal) \t : "))
akhir = int(input("Tahun Ke (Akhir) \t : "))
residu = float(input("Nilai Sisa \t\t : "))

#Proses Penghitungan Depresiasi Dan Outpu
def penyusutan(umur,biaya,awal,akhir,residu):
    if (biaya != None and
        umur != None and
        awal != None and
        akhir != None and
        residu != None):

        if (awal < akhir):
            print("\n")
            print("Hasil Depresiasi")
            print("Tahun Ke- \t Harga Awal  \t Beban Penyusutan \t Akumulasi \t Nilai")
            susut = (biaya - residu) / umur
            for lama in range ( awal, (akhir +1),1 ):
                akumulasi = lama * susut
                saldo = biaya - akumulasi
                print(lama,"\t\t",biaya,"\t",susut,"\t\t",akumulasi,"\t", saldo)
        
        else : 
            print("Maaf, Input tidak Valid")
    else :
        print("Terimakasih")


penyusutan(umur, biaya, awal, akhir, residu)
print("\n")