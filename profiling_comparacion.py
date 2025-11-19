import cProfile
import pstats
import io
import time
import matplotlib.pyplot as plt
import numpy as np
from codigo_original import encontrar_primos
from codigo_optimizado import encontrar_primos_optimizado, criba_eratostenes

def profile_codigo_original():
    """Ejecuta profiling del código original"""
    print("Ejecutando profiling del código original...")
    profiler = cProfile.Profile()
    profiler.enable()
    
    primos = encontrar_primos(100000)
    
    profiler.disable()
    
    # Guardar resultados
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    with open('profiling_original.txt', 'w') as f:
        f.write(s.getvalue())
    
    return len(primos)

def profile_codigo_optimizado():
    """Ejecuta profiling del código optimizado"""
    print("Ejecutando profiling del código optimizado (método 1)...")
    profiler = cProfile.Profile()
    profiler.enable()
    
    primos = encontrar_primos_optimizado(100000)
    
    profiler.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    with open('profiling_optimizado.txt', 'w') as f:
        f.write(s.getvalue())
    
    return len(primos)

def profile_criba():
    """Ejecuta profiling de la Criba de Eratóstenes"""
    print("Ejecutando profiling de Criba de Eratóstenes...")
    profiler = cProfile.Profile()
    profiler.enable()
    
    primos = criba_eratostenes(100000)
    
    profiler.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    with open('profiling_criba.txt', 'w') as f:
        f.write(s.getvalue())
    
    return len(primos)

def comparar_tiempos(repeticiones=3):
    """Compara los tiempos de ejecución de los diferentes métodos"""
    print(f"\nComparando tiempos de ejecución ({repeticiones} repeticiones)...")
    
    tiempos_original = []
    tiempos_optimizado = []
    tiempos_criba = []
    
    for i in range(repeticiones):
        print(f"\nEjecución {i+1}/{repeticiones}")
        
        # Código original
        inicio = time.time()
        encontrar_primos(100000)
        tiempos_original.append(time.time() - inicio)
        print(f"  Original: {tiempos_original[-1]:.4f}s")
        
        # Código optimizado
        inicio = time.time()
        encontrar_primos_optimizado(100000)
        tiempos_optimizado.append(time.time() - inicio)
        print(f"  Optimizado: {tiempos_optimizado[-1]:.4f}s")
        
        # Criba de Eratóstenes
        inicio = time.time()
        criba_eratostenes(100000)
        tiempos_criba.append(time.time() - inicio)
        print(f"  Criba: {tiempos_criba[-1]:.4f}s")
    
    return tiempos_original, tiempos_optimizado, tiempos_criba

def crear_graficos(tiempos_original, tiempos_optimizado, tiempos_criba):
    """Crea gráficos comparativos"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Análisis de Rendimiento - Búsqueda de Números Primos', 
                 fontsize=16, fontweight='bold')
    
    # Gráfico 1: Comparación de tiempos promedio
    metodos = ['Original', 'Optimizado\n(sqrt)', 'Criba\nEratóstenes']
    tiempos_promedio = [
        np.mean(tiempos_original),
        np.mean(tiempos_optimizado),
        np.mean(tiempos_criba)
    ]
    colores = ['#e74c3c', '#f39c12', '#2ecc71']
    
    axes[0, 0].bar(metodos, tiempos_promedio, color=colores, alpha=0.7, edgecolor='black')
    axes[0, 0].set_ylabel('Tiempo (segundos)', fontweight='bold')
    axes[0, 0].set_title('Comparación de Tiempos Promedio', fontweight='bold')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Añadir valores en las barras
    for i, v in enumerate(tiempos_promedio):
        axes[0, 0].text(i, v + max(tiempos_promedio)*0.02, f'{v:.4f}s', 
                       ha='center', fontweight='bold')
    
    # Gráfico 2: Mejora de rendimiento
    mejora_opt = ((tiempos_promedio[0] - tiempos_promedio[1]) / tiempos_promedio[0]) * 100
    mejora_criba = ((tiempos_promedio[0] - tiempos_promedio[2]) / tiempos_promedio[0]) * 100
    
    mejoras = [mejora_opt, mejora_criba]
    metodos_mejora = ['Optimizado vs\nOriginal', 'Criba vs\nOriginal']
    
    axes[0, 1].bar(metodos_mejora, mejoras, color=['#f39c12', '#2ecc71'], 
                   alpha=0.7, edgecolor='black')
    axes[0, 1].set_ylabel('Mejora (%)', fontweight='bold')
    axes[0, 1].set_title('Porcentaje de Mejora en Rendimiento', fontweight='bold')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(mejoras):
        axes[0, 1].text(i, v + max(mejoras)*0.02, f'{v:.1f}%', 
                       ha='center', fontweight='bold')
    
    # Gráfico 3: Distribución de tiempos
    axes[1, 0].boxplot([tiempos_original, tiempos_optimizado, tiempos_criba],
                       labels=metodos, patch_artist=True,
                       boxprops=dict(facecolor='lightblue', alpha=0.7))
    axes[1, 0].set_ylabel('Tiempo (segundos)', fontweight='bold')
    axes[1, 0].set_title('Distribución de Tiempos de Ejecución', fontweight='bold')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Gráfico 4: Speedup (aceleración)
    speedup_opt = tiempos_promedio[0] / tiempos_promedio[1]
    speedup_criba = tiempos_promedio[0] / tiempos_promedio[2]
    
    speedups = [1.0, speedup_opt, speedup_criba]
    axes[1, 1].plot(metodos, speedups, marker='o', linewidth=2, 
                    markersize=10, color='#3498db')
    axes[1, 1].set_ylabel('Speedup (veces más rápido)', fontweight='bold')
    axes[1, 1].set_title('Factor de Aceleración', fontweight='bold')
    axes[1, 1].grid(alpha=0.3)
    axes[1, 1].axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Línea base')
    
    for i, v in enumerate(speedups):
        axes[1, 1].text(i, v + 0.1, f'{v:.2f}x', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('comparacion_rendimiento.png', dpi=300, bbox_inches='tight')
    print("\nGráfico guardado como 'comparacion_rendimiento.png'")
    plt.show()

def generar_reporte():
    """Genera un reporte completo del análisis"""
    print("\n" + "="*70)
    print("GENERANDO REPORTE COMPLETO")
    print("="*70)
    
    # Profiling
    cant_original = profile_codigo_original()
    cant_optimizado = profile_codigo_optimizado()
    cant_criba = profile_criba()
    
    print(f"\nPrimos encontrados - Original: {cant_original}")
    print(f"Primos encontrados - Optimizado: {cant_optimizado}")
    print(f"Primos encontrados - Criba: {cant_criba}")
    
    # Comparación de tiempos
    tiempos_original, tiempos_optimizado, tiempos_criba = comparar_tiempos(3)
    
    # Crear gráficos
    crear_graficos(tiempos_original, tiempos_optimizado, tiempos_criba)
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE RESULTADOS")
    print("="*70)
    print(f"Tiempo promedio Original: {np.mean(tiempos_original):.4f}s")
    print(f"Tiempo promedio Optimizado: {np.mean(tiempos_optimizado):.4f}s")
    print(f"Tiempo promedio Criba: {np.mean(tiempos_criba):.4f}s")
    
    mejora_opt = ((np.mean(tiempos_original) - np.mean(tiempos_optimizado)) / 
                  np.mean(tiempos_original)) * 100
    mejora_criba = ((np.mean(tiempos_original) - np.mean(tiempos_criba)) / 
                    np.mean(tiempos_original)) * 100
    
    print(f"\nMejora con optimización (sqrt): {mejora_opt:.1f}%")
    print(f"Mejora con Criba de Eratóstenes: {mejora_criba:.1f}%")
    print("\nArchivos generados:")
    print("  - profiling_original.txt")
    print("  - profiling_optimizado.txt")
    print("  - profiling_criba.txt")
    print("  - comparacion_rendimiento.png")

if __name__ == "__main__":
    generar_reporte()