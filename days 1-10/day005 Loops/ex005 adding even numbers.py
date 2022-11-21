total = 0

for n in range(1, 101):
    if n % 2 == 0:
        total += n

print(total)

total2 = 0

for n in range(2, 101, 2): #a função range tem 3 variaveis: start, stop, step. Step é quantos numeros devem ser pulados para o próximo, sendo que se não for adicionado, é considerado 1
    total2 += n

print(total2)
