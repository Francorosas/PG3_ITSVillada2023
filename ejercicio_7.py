def num_step(numero_str):
    for i in range (len(numero_str)- 1):
        if abs(int(numero_str[i]) - int(numero_str[i + 1])) == 1:
            return True
        else:
            return False

numero = int(input("Ingrese un numero: "))
numero_str = str(numero)
print(num_step(numero_str))