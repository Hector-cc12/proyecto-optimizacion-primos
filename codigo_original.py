import time

def es_primo(n):
    """Verifica si un número es primo (versión no optimizada)"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    """Encuentra todos los números primos hasta el límite"""
    primos = []
    for num in range(2, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    print("Buscando números primos del 1 al 100,000...")
    inicio = time.time()
    
    primos = encontrar_primos(100000)
    
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    
    print(f"Cantidad de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
    print(f"Primeros 10 primos: {primos[:10]}")
    print(f"Últimos 10 primos: {primos[-10:]}")