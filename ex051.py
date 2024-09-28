#Progressão Aritmética
print("=" * 24)
print("\033[36m10 TERMOS DE UMA PA\033[m")
print("=" * 24)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,decimo + razao, razao):
    print("{}".format(c), end= " - ")
print("\033[34mACABOU\033[m")