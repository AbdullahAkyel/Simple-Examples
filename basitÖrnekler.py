#%% Örnek 1: Girilen kullanıcı ismine göre ekrana “Merhaba Kullanıcı” yazdıran python kodunu yazınız.

name = input("İsminizi girin: ")
print("Merhaba {}!".format(name))


#%% Örnek 2: Klavyeden girilen iki sayıyı toplayan ve sonucu ekranda gösteren python kodunu yazınız.

num1 = int(input("Birinci sayiyi girin: "))
num2 = int(input("İkinci sayiyi girin: "))

total = num1 + num2

print("Toplam {}".format(total))


#%% Örnek 3: Klavyeden girilen iki sayıyının ortalamasını bulan ve sonucu ekranda gösteren python kodunu yazınız.

num1 = int(input("Birinci sayiyi girin: "))
num2 = int(input("İkinci sayiyi girin: "))

average = (num1 + num2) / 2

print(average)


#%% Örnek 4: Klavyeden girilen vize ve final notuna göre vizenin %40 ve finalin %60 ını alan ve sonucu ekranda gösteren python kodunu yazınız.
#   60'ı geçerse "geçti", geçmezse "kaldı" yazsın.

vize = int(input("Vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

result = vize*0.4 + final*0.6

if result >= 60:
    print("Ortalamanız: {} Gecti!".format(result))
    
else:
    print("Ortalamanız: {} Kaldi!".format(result))


#%% Örnek 5: Klavyeden girilen üç yazılı notunun ortalamasını bulan ekranda gösteren python kodunu yazınız.

note1 = int(input("Birinci notu girin: "))
note2 = int(input("İkinci notu girin: "))
note3 = int(input("Ücuncu notu girin: "))

average = (note1 + note2 + note3) / 3

print("Ortalamanız: {}".format(average))


#%% Örnek 6:  Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod örneğini yapınız.

num = int(input("Bir sayi giriniz: "))

if num % 2 == 0:
    print("Sayiniz çift sayidir!")
    
else:
    print("Sayiniz tek sayidir!")
    
    
#%% %Örnek 7:  Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu bulan python kodunu yazınız.

num = int(input("Bir sayi giriniz: "))

if num == 0:
    print("0")
    
elif num < 0:
    print("Sayiniz negatif bir tam sayidir!")
    
else:
    print("Sayiniz pozitif bir tam sayidir!")
    
    
#%% Örnek 8:  Klavyeden girilen yaşa göre ehliyet alıp alamayacağını bulan python kodunu yazınız.

gerekenYas = 18

age = int(input("Yasinizi girin: "))

if age == gerekenYas or age > gerekenYas:
    print("Ehliyet alabilirsiniz!")
else:
    print("Malesef ehliyet alamazsiniz :(")
    
    
#%% Örnek 9:  1 den 10 a kadar olan sayıları alt alta yazdıran python kodunu yazınız.

num = 1

while num < 11:
    print(num)
    num += 1
    
    
''' ya da

num = 1

for num in range(1,11):
    print(num)

'''


#%% Örnek 10:  1 den 20 ye kadar olan çift sayıları alt alta yazdıran python kodunu yazınız.

num = 2

for num in range(2,21):
    if num % 2 == 0:
        print(num)
        
        
#%% Örnek 13:  1 den 20 ye kadar olan tek sayıları alt alta yazdıran python kodunu yazınız.

num = 1

for num in range(1,20):
    if not num % 2 == 0:
        print(num)
        
        
#%% Örnek 14:  1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.

num = 1

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        
        
#%% Örnek 15:  Klavyeden girilen sayıya kadar olan sayıları alt alta yazdıran python kodunu yazınız.

num = 0

num2 = int(input("Bir sayi girin: "))

for num in range(num,num2 + 1):
    print(num)


#%% Örnek 16:  Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.

short_edge = int(input("Dikdörtgenin kisa kenarini girin: "))
long_edge = int(input("Dikdörtgenin uzun kenarini girin: "))

environment = short_edge * 2 + long_edge * 2
print("Dikdörtgenin cevresi {}".format(environment))

area = short_edge * long_edge
print("Dikdörtgenin alanı {}".format(area))
    
    
#%% Örnek 17:  Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız. (tekrar incele!)

text = input("Bir metin girin: ")
counter = 0

while counter < len(text):
    print(text[counter])
    counter += 1
    
#%% Örnek 18:  Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.

counter = 0
num1 = int(input("Birinci sayiyi girin: "))
num2 = int(input("İkinci sayiyi girin: "))

for i in range(num1+1,num2):
    counter += i
    
print(counter)


#%% Örnek 19:  Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.

num = int(input("Bir sayi girin: "))
counter = 2

while counter < num:
    if num % counter == 0:
        print("Sayiniz bir asal sayi değildir!")
        break
    counter += 1
else:
    print("Sayiniz bir asal sayidir!")
    
    
#%% Örnek 20:  Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız. (WOW!)

num = int(input("Bir sayi girin: "))
single = 0
double = 0

for i in range(1,num+1):
    if not i % 2 == 0:
        single += i
    else:
        double += i
        
print("Tek sayilarin toplami {}".format(single))
print("Cift sayilarin toplami {}".format(double))


#%% Örnek 21:  Klavyeden maaşı ve zam oranı girilen kişinin zamlı maaşını hesaplayan python kodunu yazınız.

salary = 5000
rate_hike = 0.10

new_salary = salary + salary* rate_hike

print("Yeni maasiniz {}".format(new_salary))


#%% Örnek 22:  Klavyeden yarıçapı girilen dairenin çevresini ve alanını hesaplayan python kodunu yazınız.

r = 5
pi = 3.14
environment = 2*pi*r
area = pi*r**2

print("Dairenin cevresi {}".format(environment))
print("Dairenin alani {}".format(area))


#%% Örnek 23:  Klavyeden kısa kenar ve uzun kenar uzunluğu girilen dikdörtgenin alanını fonksiyon kullanarak hesaplayan python kodunu yazınız.

short_edge = float(input("Kisa kenari girin: "))
long_edge = float(input("Uzun kenari girin: "))

def area(short_edge,long_edge):
    result = short_edge * long_edge
    print("Alan: {}".format(result))
    return result

area(short_edge,long_edge)


#%% Örnek 24:  Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç tanesinin 5’in katı olduğunu bulan python kodunu yazınız.
    
list1 = [1,5,7,8,15,25,35,26,75,78,94,102]

for i in list1:
    if i % 5 == 0:
        print(i)
        
        
#%% Örnek 25:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların toplamını bulan python kodunu yazınız.

counter = 0
start = int(input("Baslangic degerini girin: "))
finish = int(input("Bitis degerini girin: "))

for i in range(start+1,finish):
    if i % 2 == 0:
        counter += i
print(counter)


#%% Örnek 26:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların toplamını bulan python kodunu yazınız.

counter = 0
start = int(input("Baslangic degerini girin: "))
finish = int(input("Bitis degerini girin: "))

for i in range(start+1,finish):
    if not i % 2 == 0:
        counter += i
print(counter)


#%% Örnek 27:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların ortalamasını bulan python kodunu yazınız.
# 2 34567 8

counter = 0
start = int(input("Baslangic degerini girin: "))
finish = int(input("Bitis degerini girin: "))

for i in range(start+1,finish):
    counter += i
    
result = counter / (finish - start - 1)
print(result)


#%% Örnek 36: Bir otoparkın ücret tarifesi aşağıdaki gibidir: (WOW!)
# 1 saate kadar: 5 TL
# 1-5 saat arası: Saat başı 4 TL
# 5 saatten fazla: Saat başı 3 TL
# Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.

pay = 0
counter = 0

time = int(input("Ne kadar kalacaginizi yaziniz: "))

if time == 1:
    print("Odemeniz gereken ucret: 5 TL'dir.")
          
elif time > 1 and time < 6:
    counter = time - 1
    pay = 4 * counter
    print("Odemeniz gereken ucret: {}".format(pay+5))
    
elif time > 5:
    counter = time - 5
    pay = 3 * counter
    print("Odemeniz gereken ucret: {}".format(pay+5+16))
    
    
#%% Örnek 37:  Klavyeden girilen bir ifadeyi ekrana 10 defa yazdıran python kodunu yazınız.

counter = 0
text = input("Bir metin girin: ")

while counter < 10:
    print(text)
    counter += 1
    

#%% Örnek 38:  Klavyeden girilen bir ifadeyi klavyeden girilen bir sayı kadar ekrana yazdıran python kodunu yazınız.

text = input("Bir metin girin: ")
num = int(input("Kac defa yazacağını girin: "))
counter = 0

while not counter == num:
    print(text)
    counter += 1
    
    
#%% Örnek 41:  Klavyeden başlangıç değeri, bitiş değeri ve artış miktarı girilen sayıları alt alta yazdıran python kodunu yazınız.

start = int(input("Baslangic degerini girin: "))
finish = int(input("Bitis degerini girin: "))
increase = int(input("Artis miktarini girin: "))

for i in range(start,finish,increase):
    print(i)
    
    
#%% Örnek 42:  0 dan 100 e kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

counter = 0
i = 0

while i < 100:
    counter += i
    i += 2
print(counter)


#%% Örnek 43:  0 dan 100 e kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

counter = 0
i = 1

while i < 100:
    counter += i
    i += 2
print(counter)


#%% Örnek 44:  Klavyeden girilen sayıya kadar olan sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

num = int(input("Bir sayi girin: "))
counter = 0
i = 0

while i < num:
    counter += i
    i += 1
print(counter)


#%% Örnek 47:  Klavyeden girilen bir metni harflarine ayıran python programını while döngüsü ile yazdıran kodunu yazınız. (WOW!)

text = input("Bir metin girin: ")
counter = 0

while counter < len(text):
    print(text[counter])
    counter += 1
    
    
#%% Örnek 48:  0 ile 100 arasında 10 tane rastgele tam sayı üreten ve bu sayılardan en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodunu yazınız. (incele!)

import random
 
sayilar = []
for i in range(0, 10):
    rand = random.randint(0, 100)
    sayilar.append(rand)
    print(rand)
 
minNumber = sayilar[0]
maxNumber = sayilar[0]
 
for i in range(0, 10):
    if minNumber > sayilar[i]:
        minNumber = sayilar[i]
    if maxNumber < sayilar[i]:
        maxNumber = sayilar[i]
 
print("Dizideki En Büyük Değer : {0} ".format(maxNumber))
print("Dizideki En Küçük Değer : {0} ".format(minNumber))


#%% Örnek 62:  Klavyeden girilen şifrenin “bilişim” olup olmadığını kontrol eden ve ona göre yönlendirme yapan python kodunu yazınız.

password = "bilisim"
text = input("Sifreyi girin: ")


if text == password:
    print("Giris yapiliyor...")
else:
    print("Sifre yanlis!")

    
    
#%% Örnek 64:  Klavyeden 1 ile 5 arasında bir değer giren ve bu değeri yazı ile yazdıran bu değerlerin dışında bir değer girildiğinde uyarı mesajı veren python kodunu yazınız.


num = int(input("1-5 arasinda bir deger girin: "))
if num == 1:
    print("Bir")
elif num == 2:
    print("İki")
elif num == 3:
    print("Uc")
elif num == 4:
    print("Dort")
elif num == 5:
    print("Bes")
else:
    print("Lütfen 1-5 arasinda bir sayi girin!")
    
    
#%% Örnek 68:  0 ile 50 sayısı arasında 4 e bölünen sayıları listeleyen programın python kodlarını yazınız.

list1 = []

for i in range(0,51):
    if i % 4 == 0:
        list1.append(i)
print(list1)


#%% Örnek 69:  Klavyeden girilen beş tane sayıdan en büyüğünü bulup ekranda gösteren python kodunu yazınız.


list1 = []

for i in range(0,5):
    num = int(input("Bir sayi girin: "))
    list1.append(num)

maxNumber = list1[0]
 
for i in range(0, 5):
    if maxNumber < list1[i]:
        maxNumber = list1[i]
        
print("En büyük değer: ",maxNumber)


#%% Örnek 70:  Klavyeden kullanıcının girdiği ismin kaç harfli olduğunu bulan programın python kodlarını yazınız.

text = input("İsminizi girin: ")

print(len(text))
    

#%% Örnek 73:  Klavyeden girilen taban ve üs değerine göre o sayının üssünü hesaplayan ve sonucu ekranda gösteren python kodunu yazınız.

taban = int(input("Taban değerini girin: "))
us = int(input("Us değerini girin: "))

print(taban**us)


#%% Örnek 74:  Klavyeden girilen bir sayının karekökünü bulan ve ekranda gösteren python kodunu yazınız.

us = 1/2
num = int(input("Bir sayi girin: "))

print(num**us)


#%% Örnek 75:  Klavyeden girilen iki sayının EKOK ve EBOB’unu bulan ve ekranda gösteren python kodunu yazınız.

num1 = int(input("Birinci sayiyi girin: "))
num2 = int(input("İkinci sayiyi girin: "))


if num1 % num2 == 0:
    print("Girdiginiz sayilarin Ekok'u {}".format(num1))
elif num2 % num1 ==0:
    print("Girdiginiz sayilarin Ekok'u {}".format(num2))
else:
    print("Girdiginiz sayilarin Ekok'u {}".format(num1*num2))
    


if num1 % num2 == 0:
    print("Girdiginiz sayinin Ebob'u {}".format(num2))
elif num2 % num1 == 0:
    print("Girdiginiz sayinin Ebob'u {}".format(num1))
else:
    print("Girdiginiz sayinin Ebob'u {}".format("1'dir"))
    
    
#%% Örnek 77:  Klavyeden girilen bir sayının mutlak değerini bulan ve ekranda gösteren python kodunu yazınız.

num = int(input("Bir sayi girin: "))

if num < 0:
    print("Sayinizin mutlak degeri: {}".format(num*-1))
else:
    print("Sayinizin mutlak degeri: {}".format(num))
    

#%% Örnek 81:  Klavyeden 10’luk tabanda girilmiş bir sayıyı 2’lik, 8’lik ve 16’lık tabana çeviren ve ekranda gösteren python kodunu yazınız.

num = int(input("Bir sayi girin: "))

print("2'lik tabanda: {}".format(bin(num)))
print("8'lik tabanda: {}".format(oct(num)))
print("16'lık tabanda: {}".format(hex(num)))


#%% Örnek 100:  Klavyeden girilen bir şifrenin karakterlerini kontrol ederek girilen şifrenin 4 karakter olana kadar yeni şifre isteyen,
# girilince de doğru şifreyi ekranda gösteren python kodunu yazınız.

password = input("Sifrenizi girin: ")

while not len(password) == 4:
    print("Sifreyi yeniden girin!")
    password = input("Sifrenizi girin: ")
    
print("Dogru sifre 'game'")