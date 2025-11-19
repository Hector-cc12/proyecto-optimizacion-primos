import time
import numpy as np
import math

def es_primo_optimizado(n):
    """Verifica si un número es primo (versión optimizada)"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Solo verificar hasta la raíz cuadrada
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_optimizado(limite):
    """Encuentra todos los números primos usando list comprehension"""
    # Incluir 2 y luego solo números impares
    primos = [2] + [num for num in range(3, limite + 1, 2) 
                    if es_primo_optimizado(num)]
    return primos

def criba_eratostenes(limite):
    """Implementación de la Criba de Eratóstenes con NumPy"""
    # Crear array booleano, True = primo
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False
    
    # Aplicar criba
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            # Marcar múltiplos como no primos
            es_primo[i*i::i] = False
    
    # Retornar índices donde es_primo es True
    return np.where(es_primo)[0].tolist()

if __name__ == "__main__":
    print("=" * 60)
    print("MÉTODO 1: Optimización con raíz cuadrada y list comprehension")
    print("=" * 60)
    inicio = time.time()
    primos1 = encontrar_primos_optimizado(100000)
    fin = time.time()
    tiempo1 = fin - inicio
    
    print(f"Cantidad de primos encontrados: {len(primos1)}")
    print(f"Tiempo de ejecución: {tiempo1:.4f} segundos")
    print(f"Primeros 10 primos: {primos1[:10]}")
    print(f"Últimos 10 primos: {primos1[-10:]}")
    
    print("\n" + "=" * 60)
    print("MÉTODO 2: Criba de Eratóstenes con NumPy")
    print("=" * 60)
    inicio = time.time()
    primos2 = criba_eratostenes(100000)
    fin = time.time()
    tiempo2 = fin - inicio
    
    print(f"Cantidad de primos encontrados: {len(primos2)}")
    print(f"Tiempo de ejecución: {tiempo2:.4f} segundos")
    print(f"Primeros 10 primos: {primos2[:10]}")
    print(f"Últimos 10 primos: {primos2[-10:]}")
    
    print("\n" + "=" * 60)
    print("RESUMEN DE MEJORAS")
    print("=" * 60)
    print(f"Método 1 - Tiempo: {tiempo1:.4f} segundos")
    print(f"Método 2 - Tiempo: {tiempo2:.4f} segundos")
    print(f"Mejor método: {'Criba de Eratóstenes' if tiempo2 < tiempo1 else 'List Comprehension'}")