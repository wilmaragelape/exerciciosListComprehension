# Crie uma lista com os quadrados dos números de 1 a 10.

numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
quadrado = [numero ** 2 for numero in numeros]
print (quadrado)


#Transforme uma lista de strings em uma lista de inteiros.

strings = ["23", "50", "70", "90", "150"]
numero_int = [int(string) for string in strings]
print (numero_int)


# Crie uma lista com os números pares de 1 a 20.

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeros_pares = [numero for numero in numeros if numero % 2 ==0]
print(numeros_pares)


# Extraia as vogais de uma string e crie uma lista com elas.

frase = "A lua e o sol são dois amores antônimos"
vogais = [letra for letra in frase if letra.lower() in 'aeiou']
print(vogais)

