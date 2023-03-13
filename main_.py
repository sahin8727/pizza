import csv
from datetime import datetime

# 'Menu.txt' içerisindeki menüyü ekrana yazdır:
def print_menu():
    with open('Menu.txt', 'r') as f:
        menu = f.read()
        print(menu)

# super class
class Pizza:
    def __init__(self):
        self.description = "Henüz tanımlanmadı!"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# sub class pizza türlerini tanımla:

# subclass
class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza hamuru üzerinde domates, biber, mantar, sucuk ve mozarella peyniri"
        self.cost = 80

# subclass
class Pastirmali(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza hamuru üzerinde domates, biber, mantar, kayseri pastırması ve mozarella peyniri"
        self.cost = 100

# subclass
class Vejeteryan(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza hamuru üzerinde domates, biber, mantar, zeytin, fesleğen ve mozarella peyniri"
        self.cost = 75

# subclass
class Karisik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza hamuru üzerinde domates, mısır, mantar, sucuk, salam ve mozarella peyniri"
        self.cost = 90

# Super class, aynı zamanda pizza class'ından inheritance yap

# super class
class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


    def get_description(self):
        return self.description


# subclass
# zeytin
class zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "İlave zeytin eklenecektir."
        self.cost = 5

# subclass
class mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "İlave mantar eklenecektir."
        self.cost = 8

class peynir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description="Ekstra peynir eklenecektir."
        self.cost=10

class keci_peyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description="Ekstra %100 keçi peyniri eklenecektir."
        self.cost=13


def place_order(pizza_choice,sos_choice,name,tc,kredi_karti,sifre,aciklama):
  
  #pizza seçimi
  if pizza_choice == "1":
    pizza = Klasik()
  
  elif pizza_choice == "2":
    pizza = Pastirmali()

  elif pizza_choice == "3":
    pizza = Vejeteryan()

  elif pizza_choice == "4":
    pizza = Karisik()
  
  else:
    print("Lütfen geçerli bir seçim yapınız!")
    return print_menu()
    

  #sos seçimi
  if sos_choice == "10":
    sos = zeytin(pizza=pizza)
  elif sos_choice == "11":
    sos = mantar(pizza=pizza)
  elif sos_choice == "12":
    sos = peynir(pizza=pizza)
  elif sos_choice == "13":
    sos = keci_peyniri(pizza=pizza) 
  else:
    print("Geçersiz sos seçimi")
    return print_menu()
    

  #sipariş tutarını hesapla:
  total_cost= int(pizza.cost) + int(sos.cost)
  print(f"---------------------\nSipariş tutarınız: {total_cost} TL dir.\n----------------------")

  #sipariş zamanını hesapla:
  order_time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  #sipariş bilgilerini kaydet:
  with open ("order_database.csv",mode="w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow([name,tc,kredi_karti,sifre,aciklama,pizza.get_description(),sos.get_description(),total_cost,order_time])
  
  print("Siparişiniz alınmıştır, teşekkür ederiz!")


print_menu()

#kullanıcıdan pizza seçimini iste:
pizza_choice = input("Lütfen pizza seçimini yapınız (1-4) :  ")

#kullanıcıdan sos seçimini iste:
sos_choice = input("Lütfen sos seçimini yapınız (10-13):  ")

# Kullanıcıdan fatura bilgilerini al:
name=input("Adınız: ")
tc=input("TC Kimlik No: ")
kredi_karti=input("Kredi Kartı No: ")
sifre=input("Şifreniz: ")
aciklama=input("Sipariş açıklaması: ")

place_order(pizza_choice,sos_choice,name,tc,kredi_karti,sifre,aciklama)