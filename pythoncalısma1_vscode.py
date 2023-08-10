"""
# HelloWorld
print("Hello World!")
"""


"""
#kullanıcıdan isim alma
name = input('İsminizi Giriniz.')
print("Merhaba "+name)
"""


"""
#sayı girişi ve sayısal işlemler
sayi1 = input('1. sayıyı giriniz = ')
sayi2 = input('2. sayıyı giriniz = ')

toplam = float(sayi1) + float(sayi2)
print("Toplam = {0}" .format(toplam))

ortalama = (int(sayi1) + int(sayi2))/2
print("Ortalama = {0} " .format(ortalama))
"""



"""
#if kullanımı
ort = input("Ortalamanızı giriniz = ")
if (int(ort)>=60):
   print("Geçtiniz!")
else: 
   print("Kaldınız!")   
"""


"""
# tek çift
sayi = input("Sayıyı giriniz = ")
if (int(sayi)%2 == 0):
    print("Sayınız çift! ")
else:
    print("Sayınız tek! ")    
"""

#&lt; and &gt; are used for < and > (less than) (greater than)


"""
#1-100 arası sayıları listeleme
for i in range(1,101):
    print(i)
"""

#range döngüdür. range(10) çıktısı 0 1 2 3 4 5 6 7 8 9'dur mesela
#list(range(5)) çıktısı [0,1,2,3,4]
#len(list(range(5))) çıktısı 5

"""for seq in range(5,10):
    print(seq)
"""


    #• The for loop then iterates over each number in the sequence and assigns it to the variable seq.
    #• Inside the loop, the print() function is used to output the value of seq to the console.
    #The loop variable seq takes on each value in the range

"""
# 1-100 Arası Tek Sayıları Listele    
for i in range(1,101):
    if i%2!=0:
        print(i)
"""

"""
#1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listele
sayi = input("sayi giriniz = ")
for i in range(1, int(sayi)+1):
    print(i)
"""