from random import randint

while True:
    tutulanSayi = randint(1, 100)
    denemeHakki = 7
    denemeSayisi = 0

    print("\nSayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum, tahmin etmeye çalışın.")
    print(f"Maksimum {denemeHakki} hakkınız var.")

    while denemeHakki > 0:
        
        try:
            kullaniciSayi = int(input("Lütfen bir sayı giriniz: "))
            if kullaniciSayi not in range(1,101):
                print("Girdiğiniz sayı 1 ile 100 arasında olmalı !!")
                continue
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
            continue
        
        denemeSayisi += 1  
        
        if kullaniciSayi > tutulanSayi:
            denemeHakki -= 1
            print(f"Daha küçük bir sayı girin! Kalan hak: {denemeHakki}")
        elif kullaniciSayi < tutulanSayi:
            denemeHakki -= 1
            print(f"Daha büyük bir sayı girin! Kalan hak: {denemeHakki}")
        else:
            print(f"\nTebrikler! {tutulanSayi} doğru tahmin. {denemeSayisi}. denemede bildiniz.")
            break  

    if denemeHakki == 0:
        print(f"\nÜzgünüm, tahmin hakkınız bitti. Doğru sayı: {tutulanSayi}")

    tekrar = input("\nTekrar oynamak ister misiniz? (E/H): ").strip().lower()
    if tekrar != 'e':
        print("Oyun bitti. Teşekkürler!")
        break