# Aula V - Demonstração por indução finita 

# 1. Mostre que o teorema é válido para  o menor n possível que satisfaz a hipótese;  
# 2. Assuma que o teorema é válido para n = k; 
# 3. Aumma que o teorema é válido para n = k + 1


# Função da soma dos n primeiros números naturais:  

def sum_n(n): 
    try: 
        if n == 0:
            raise ValueError("O número selecionado precisa ser diferente de zero!")
        return n * (n+1)/2
    except ValueError as e: 
        print(e)

# A soma dos quadradis dos n primeiros números naturais: 

def sum_n_quadrado(n): 
    try: 
        if n == 0:
            raise ValueError("O número selecionado precisa ser diferente de zero!")
        return (n * (n+1) * (2*n +1))/6
    except ValueError as e: 
        print(e)

# Guardando o input 

n = int(input("Digite um número desejado:"))

# Retornando os output das funções 

if __name__ == "__main__": 
    print("A soma dos", n, "primeiros números é: ", sum_n(n))
    print("O  quadrado dos ", n, "primeiros números é: ", sum_n_quadrado(n))