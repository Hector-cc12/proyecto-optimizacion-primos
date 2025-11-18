# 🚀 Proyecto de Optimización de Código Python

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Proyecto educativo de optimización de algoritmos en Python, enfocado en la búsqueda de números primos hasta 100,000 con análisis comparativo de rendimiento.

## 📋 Descripción

Este proyecto implementa y compara **tres enfoques diferentes** para encontrar números primos:

| Método | Tiempo | Speedup | Estado |
|--------|--------|---------|--------|
| **Código Original** | ~285 segundos | 1.00x | ❌ Sin optimizar |
| **Código Optimizado** | ~2.3 segundos | 121.7x | ✅ Optimizado |
| **Criba de Eratóstenes** | ~0.05 segundos | 5,458x | ⚡ Máxima eficiencia |

### 🎯 Mejora Total: **5,458x más rápido**

## 🎓 Objetivos del Proyecto

- ✅ Aplicar técnicas de optimización de código
- ✅ Medir y comparar tiempos de ejecución
- ✅ Utilizar herramientas de profiling (cProfile)
- ✅ Implementar buenas prácticas de programación (PEP 8)
- ✅ Visualizar resultados con Matplotlib
- ✅ Documentar el proceso completo

## 📁 Estructura del Proyecto

```
proyecto-optimizacion-primos/
├── 📄 codigo_original.py           # Implementación sin optimizar
├── 📄 codigo_optimizado.py         # Versión optimizada
├── 📄 profiling_y_comparacion.py   # Scripts de análisis
├── 📊 comparacion_optimizacion.png # Gráficos de resultados
├── 📝 profiling_*.txt              # Reportes de profiling
├── 📖 DOCUMENTACION.md             # Documentación completa
├── 📋 README.md                    # Este archivo
├── 📦 requirements.txt             # Dependencias
├── 🔒 LICENSE                      # Licencia MIT
└── 🚫 .gitignore                   # Archivos ignorados
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación
- **NumPy**: Operaciones vectorizadas eficientes
- **Matplotlib**: Visualización de datos
- **cProfile**: Análisis de rendimiento
- **Git/GitHub**: Control de versiones

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Hector-ccl2/proyecto-optimizacion-primos.git

# 2. Navegar al directorio
cd proyecto-optimizacion-primos

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Dependencias

```
numpy>=1.20.0
matplotlib>=3.3.0
```

## 📖 Documentación Completa

Para información detallada sobre:
- 🔍 Análisis del código original
- 🛠️ Problemas identificados
- ⚙️ Técnicas aplicadas paso a paso
- 📊 Análisis de profiling completo
- 💡 Conclusiones y recomendaciones

## 🌳 Ramas del Proyecto

- **`main`**: Rama principal con código estable
- **`optimizacion-codigo`**: Rama con todas las optimizaciones implementadas

```bash
# Cambiar a la rama de optimización
git checkout optimizacion-codigo
```

## 📚 Recursos de Aprendizaje

- 📘 [Complejidad Algorítmica - Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- 📗 [NumPy Performance](https://numpy.org/doc/stable/user/performance.html)
- 📙 [Python Profiling - cProfile](https://docs.python.org/3/library/profile.html)
- 📕 [PEP 8 Style Guide](https://pep8.org/)
- 📓 [Criba de Eratóstenes](https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)


## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Hector Ccl**

- 💼 GitHub: [@Hector-ccl2](https://github.com/Hector-ccl2)
- 📧 Email: [tu-email@ejemplo.com]
- 🎓 Proyecto Educativo - 2025


**Última actualización:** Noviembre 2025
