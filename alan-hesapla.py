import math

def kare_alan(a):
    return a * a

def dikdortgen_alan(a, b):
    return a * b

def ucgen_alan(a, b):
    return (a * b) / 2

def daire_alan(b):
    return math.pi * (b ** 2)

def yamuk_alan(a, b, c):
    return (a + b) * c / 2

print("-" * 30)
print("Alanı hesaplanacak geometrik şekli seçiniz.")
secim = int(input("Kare için= '1'\nDikdörtgen için= '2'\nÜçgen için= '3'\nDaire için= '4'\nYamuk için= '5'\nSeçiminiz: "))

if secim == 1:
    a = float(input("Karenin bir kenar uzunluğunu giriniz: "))
    print("Kare alanı =", kare_alan(a))
elif secim == 2:
    a = float(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
    b = float(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
    print("Dikdörtgenin alanı =", dikdortgen_alan(a, b))
elif secim == 3:
    a = float(input("Üçgenin taban uzunluğunu giriniz: "))
    b = float(input("Üçgenin yüksekliğini giriniz: "))
    print("Üçgenin alanı =", ucgen_alan(a, b))
elif secim == 4:
    b = float(input("Dairenin yarıçap uzunluğunu giriniz: "))
    print("Dairenin alanı =", daire_alan(b))
elif secim == 5:
    a = float(input("Yamuğun üst taban uzunluğunu giriniz: "))
    b = float(input("Yamuğun alt taban uzunluğunu giriniz: "))
    c = float(input("Yamuğun yüksekliğini giriniz: "))
    print("Yamuğun alanı =", yamuk_alan(a, b, c))
else:
    print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer girin.")

print("-" * 30)
