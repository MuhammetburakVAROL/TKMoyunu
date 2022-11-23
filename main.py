import random

def TKMoyunu():

    oyun =["taş", "kağıt", "makas"]

    taş = oyun[0]

    kağıt = oyun[1]

    makas = oyun[2]


    print(30*"-")
    print("Taş,kağıt,makas oyununa hoş geldiniz!")
    print("Oyundan çıkmak için x tuşuna basın.")
    print(30*"-")

    while True:

        Tercih = input("Taş mı? Kağıt mı? Makas mı? ")
        bil_secim = random.choice(oyun)
        if Tercih!= "taş" and Tercih!= "kağıt" and Tercih!= "makas" and Tercih != "x":
            print("Lütfen geçerli opsiyonları kullanınız.")

        if Tercih == taş:
            if bil_secim == taş:
                print(f"Berabere kaldınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            elif bil_secim == makas:
                print(f"Kazandınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            else:
                print(f"Kaybettiniz\nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")

        if Tercih == kağıt:
            if bil_secim == kağıt:
                print(f"Berabere kaldınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            elif bil_secim == taş:
                print(f"Kazandınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            else:
                print(f"Kaybettiniz. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")

        if Tercih == makas:
            if bil_secim == makas:
                print(f"Berabere kaldınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            elif bil_secim == kağıt:
                print(f"Kazandınız. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")
            else:
                print(f"Kaybettiniz. \nBilgisayarın seçimi: {bil_secim} \n Sizin seçiminiz:{Tercih}")

        if Tercih == 'x':
            print("oyundan çıkarılıyor...")
            break
TKMoyunu()