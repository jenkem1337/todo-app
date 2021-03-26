yapılacakListesi = list()

def yapılacaklarListesineBirŞeyEkle(yapılacak, listeyeEkle):
    listeyeEkle.append(yapılacak)
    print("Yapılacak şey listeye eklendi..")
    input("Çıkmak için herhangi bir tuşa basınız")


def kontrol(yapılacak, liste):
    if yapılacak in liste:
        return True
    else:
        return False


def yapılacaklarListesindenÇıkar(yapılacak, listedenÇıkar):
    if kontrol(yapılacak, yapılacakListesi):
        listedenÇıkar.remove(yapılacak)
        print("Yapılması gereken yapıldığı için listeden çıkarıldı..")
        input("Çıkmak için herhangi bir tuşa basınız")
    else:
        print("Böyle bir şey yok...")

    
def listele():
    for i in yapılacakListesi:
        print(i)
        

giriş = """

1-Yapılacak Bir Şey Ekle
2-Yapılacak Bir Şey Çıkar
3-Yapılcakları Listele
0-Çıkış

"""


while True:
    print(giriş)
    
    tuş = input("Lütfen bir seçenek seçiniz : ")
    
    if tuş == "0":
        quit()
        break
    elif tuş == "1":
        yapılmasıGerekenGörev = input("Yapılması gereken görevi ekleyiniz : ")
        yapılacaklarListesineBirŞeyEkle(yapılmasıGerekenGörev, yapılacakListesi)
    elif tuş == "2":
        bitirilmişGörev = input("Bitirilmiş olan görevi giriniz ve çıkarın : ")
        yapılacaklarListesindenÇıkar(bitirilmişGörev, yapılacakListesi)
    elif  tuş == "3":
        listele()
    else:
        print("Hatalı gırış yaptınız lütfen tekrar deniyiniz...")