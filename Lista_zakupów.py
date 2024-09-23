lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
liczba_produktow = 0

print("Lista zakupów")
for sklep, produkty in lista_zakupow.items():
    print (f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {[i.capitalize() for i in produkty]}.")
    liczba_produktow += len(produkty)
print(f"W sumie kupuję {liczba_produktow} produktów.")
