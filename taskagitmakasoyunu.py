import random

user_wins = 0
computer_wins = 0
options = ["taş", "kağıt", "makas"]

while True:
    giris = input("taş / kağıt / makas yazın veya Q basarak çıkış yapın :")
    if giris == 'Q':
        break
    if giris not in options:
        continue
    
    randomsayi = random.randint(0, 2)
    bilgisayar = options[randomsayi]
    print("Bilgisayarın seçimi:", bilgisayar)
    
    if giris == bilgisayar:
        print("Round berabere")
    elif (giris == "taş" and bilgisayar == "makas") or \
         (giris == "kağıt" and bilgisayar == "taş") or \
         (giris == "makas" and bilgisayar == "kağıt"):
        print("Kazandınız")
        user_wins += 1
    else:
        print("Kaybettiniz")
        computer_wins += 1

print(user_wins, "kere kazandınız")     
print(computer_wins, "kere bilgisayar kazandı")
print("İyi oyundu")
