kilo = float(input("Kilonuzu kg cinsinden girin: "))
boy = float(input("Boyunuzu metre cinsinden girin: "))
 
vki = kilo / (boy ** 2)

if vki < 18.5:
    print("Zayıf")
elif vki >= 18.5 and vki < 24.99:
    print("Normal")
elif vki >= 25 and vki < 29.99:
    print("Fazla kilolu")
elif vki >= 30 and vki < 34.99:
    print("1. derece obez")
elif vki >= 35 and vki < 39.99:
    print("2. derece obez")
else:
    print("3. derece obez")
 
print("Vücut Kitle İndeksiniz:", vki)