"""
Arkadaş Panosu
--------------
GitHub Desktop öğrenmek için basit bir program.
Çalıştırmak için:  python3 main.py
"""

from arkadaslar import ARKADASLAR

BASLIK = "ARKADAŞ PANOSU"



def cizgi(uzunluk=40):
    print("=" * uzunluk)


def arkadasi_yazdir(sira, arkadas):
    print(f"{sira}. {arkadas['isim']}")
    print(f"   Şehir        : {arkadas['sehir']}")
    print(f"   Sevdiği yemek: {arkadas['sevdigi_yemek']}")
    print(f"   Mesajı       : \"{arkadas['mesaj']}\"")
    print()


def main():
    cizgi()
    print(BASLIK.center(40))
    cizgi()
    print()

    for sira, arkadas in enumerate(ARKADASLAR, start=1):
        arkadasi_yazdir(sira, arkadas)

    cizgi()
    print(f"Toplam {len(ARKADASLAR)} kişi panoya katıldı.")
    cizgi()


if __name__ == "__main__":
    main()


def nokta():
    cizgi()
    print(BASLIK.center(40))
    cizgi()
    print()

    for sira, arkadas in enumerate(ARKADASLAR, start=1):
        arkadasi_yazdir(sira, arkadas)

    cizgi()
    print(f"Toplam {len(ARKADASLAR)} kişi panoya katıldı.")
    cizgi()

        

def main():
    cizgi()
    print(BASLIK.center(40))
    cizgi()
    print()

    for sira, arkadas in enumerate(ARKADASLAR, start=1):
        arkadasi_yazdir(sira, arkadas)

    cizgi()
    print(f"Toplam {len(ARKADASLAR)} kişi panoya katıldı.")
    cizgi()


