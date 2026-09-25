# Grabados para la introducción de DeMoreto

Seis originales creados con la herramienta integrada de generación de imágenes: busto clásico, restauración de un marco, pintor ante el caballete, acanto, urna y paleta. Los prompts completos y las rutas de generación están en `generations.json`.

## Archivos finales

Originales PNG: `new-design/assets/loader/{busto,restauracion,pintor,acanto,urna,paleta}.png`.
Atlas optimizado para la web: `new-design/assets/loader/engravings.webp`, 116.040 bytes. Solo se redimensionaron y agruparon los originales para su distribución.

## Funcionamiento

La portada precarga el atlas. La cuadrícula se inserta únicamente después de decodificarlo. Siete columnas en escritorio, tres en móvil y celdas cuadradas. Un tercio de las ilustraciones cambia cada 240 ms, sin intervalos en blanco. La introducción dura al menos 1,5 segundos y espera a la imagen principal hasta un máximo de 4 segundos, más 350 ms de salida. Un fallo del atlas omite la introducción; la espera de ese recurso se limita a 2,2 segundos.

Se muestra una vez por sesión. `http://localhost:8765/new-design/?intro=1` permite repetirla. Clic, Escape o Tab permiten continuar inmediatamente. Se omite con movimiento reducido. No modifica el comportamiento de las fichas interiores.

## Verificación

Chromium de Playwright: escritorio 1440 × 1000, móvil 390 × 844, cambio real de motivos, retirada de la capa, persistencia de sesión, atlas retrasado, imagen principal retrasada, fallo del atlas y movimiento reducido. Sin errores JavaScript. Capturas: `desktop.png` y `mobile.png`.

Verificación general: 137 páginas, 98 publicaciones, 275 archivos del archivo, sin referencias locales rotas.
