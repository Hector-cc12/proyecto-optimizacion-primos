# 🚀 Proyecto de Optimización de Código Python

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

# Optimización de Código Python: Búsqueda de Números Primos

Proyecto de análisis y optimización de algoritmos para la búsqueda de números primos, demostrando técnicas de mejora de rendimiento en Python.

## 📋 Descripción

Este proyecto compara tres enfoques diferentes para encontrar números primos del 1 al 100,000:

1. **Método Original**: Algoritmo básico sin optimizaciones
2. **Método Optimizado**: Uso de raíz cuadrada y list comprehensions
3. **Criba de Eratóstenes**: Algoritmo clásico con NumPy

## 🎯 Objetivos

- Demostrar técnicas de optimización de código en Python
- Aplicar herramientas de profiling (cProfile)
- Visualizar mejoras de rendimiento
- Documentar buenas prácticas de programación

## 📊 Resultados

| Método | Tiempo | Mejora | Speedup |
|--------|--------|--------|---------|
| Original | ~40s | - | 1x |
| Optimizado | ~3s | 92% | 13x |
| Criba | ~0.3s | 99% | 133x |

*Los tiempos pueden variar según el hardware*

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- NumPy
- Matplotlib
- cProfile
- Git/GitHub

## 📦 Instalación

```bash
# Clonar el repositorio
git clone [URL-del-repositorio]
cd proyecto-optimizacion

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar código original
```bash
python codigo_original.py
```

### Ejecutar código optimizado
```bash
python codigo_optimizado.py
```

### Ejecutar análisis completo con profiling
```bash
python profiling_comparacion.py
```

## 📁 Estructura del Proyecto

```
proyecto-optimizacion/
├── codigo_original.py           # Código sin optimizar
├── codigo_optimizado.py         # Código optimizado (3 métodos)
├── profiling_comparacion.py     # Script de análisis
├── profiling_original.txt       # Resultados profiling original
├── profiling_optimizado.txt     # Resultados profiling optimizado
├── profiling_criba.txt          # Resultados profiling criba
├── comparacion_rendimiento.png  # Gráficos comparativos
├── DOCUMENTACION.md             # Documentación completa
├── README.md                    # Este archivo
└── requirements.txt             # Dependencias
```

## 📈 Técnicas de Optimización Aplicadas

### 1. Optimización Matemática
- Uso de raíz cuadrada para reducir iteraciones
- Exclusión de números pares (excepto 2)

### 2. Optimización con Python
- List comprehensions
- Reducción de llamadas a funciones

### 3. Optimización Algorítmica
- Criba de Eratóstenes: O(n log log n)
- Operaciones vectorizadas con NumPy

## 📖 Documentación

Para más detalles, consulta [DOCUMENTACION.md](DOCUMENTACION.md)

## 🎓 Conceptos Aprendidos

- ✅ Análisis de complejidad algorítmica
- ✅ Profiling con cProfile
- ✅ Optimización con NumPy
- ✅ Visualización de datos con Matplotlib
- ✅ Buenas prácticas en Python (PEP 8)
- ✅ Control de versiones con Git

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

##  Autor

**Hector-cc12**
- GitHub: [@Hector-cc12](https://github.com/Hector-cc12)
- Repositorio: [proyecto-optimizacion-primos](https://github.com/Hector-cc12/proyecto-optimizacion-primos/edit/main/README.md)


##  Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

##  Contacto

Para preguntas o sugerencias, puedes:
- Abrir un [issue](https://github.com/Hector-cc12/proyecto-optimizacion-primos/issues)
- Enviar un pull request
- Contactar al autor a través de GitHub
