print("============= Gerobak Fried Chicken ================")
print("=======================================================")
print("Kode    Jenis Potong     Harga")
print("===========================================================")
print('D        Dada            2500')
print('P        Paha            2000')
print('S        Sayap           1500')

banyaknyajenis= int(input("Banyak Jenis : "))
JenisPotong=[]
Kodepotong=[]
banyakpotong=[]
harga=[]
jumlah=[]

b=0
while  b<banyaknyajenis:
    print("jenis ke- ", b+1)
    Kodepotong.append(input("Kode potong [D/P/S] :"))
    banyakpotong.append(int(input("banyak potong :")))
    
    if Kodepotong[b]=="D" :
        JenisPotong.append("Dada")
        harga.append("2500")
        jumlah.append(banyakpotong[b]*int("2500"))
    elif Kodepotong[b]=="P" :
        JenisPotong.append("Paha")    
        harga.append("2000")
        jumlah.append(banyakpotong[b]*int("2000"))
    elif Kodepotong[b]=="S" :
         JenisPotong.append("Sayap")
         harga.append("1500")
         jumlah.append(banyakpotong[b]*int("1500"))
    else :
        JenisPotong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyakpotong[b]*int("0"))
    b=b+1

print("====== Gerobak fried Chicken ==========   ")
print("=====================================")
print("No  Jenis   Harga    Banyak   Jumlah")
print("    Potong  Satuan    Beli     Harga")
print("==========================================")

jumlahharga=0
a=0
while a <banyaknyajenis:
    jumlahharga=jumlahharga+jumlah[a]
    print("%i   %s   %s   %i  %i" % (a+1, JenisPotong[a], harga[a], banyakpotong[a], jumlah[a]))
    a=a+1
pajak=jumlahharga*0.1
totalharga=jumlahharga+pajak

print("==========================================")
print("         Jumlah Bayar  Rp.%i" %(jumlahharga))
print("                Pajak  Rp.%i" %(pajak))
print("         Total bayar   Rp.%i" %(totalharga))
print("==========================================")
print("============= Terima Kasih Sudah Berbelanja ================")