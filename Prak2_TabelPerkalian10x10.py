
print("Develop by : Dewi Nur Arifah/MI-2020A/20051397079")
print("           ~~ TABEL PERKALIAN 10x10 ~~           ")

print("+-----------------------------------------------------------------------------+")
for i in range (1, 11):
    for j in range (1, 11):
        x = i*j
        if x < 10:
            print ("|  ", x, end=" | ")
        elif x >= 10 and x < 100:
            print ("| ", x, end=" | ")
        else:
            print ("|", x, end=" |")
    print()

print("+-----------------------------------------------------------------------------+")

