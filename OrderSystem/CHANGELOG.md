# Changelog

## [0.1.0] - 2025-08-08
### Added
- CLI para registrar productos y precios.
- Cálculo de totales y propina.
- Exportación a `.txt` en carpeta `exports` con timestamp.
- Alineación dinámica de columnas.
- Agrupación de productos repetidos con subtotales.
- Reutilización del último precio ingresado para productos repetidos.

### Fixed
- Manejo de precios inválidos sin incrementar la cantidad de producto.
- Corrección de alineación para nombres cortos/largos con subtotales.
- Eliminación de exportación duplicada.
