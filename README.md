# Technical Assessment - Technical Support Engineer (Kushki)

Prueba técnica realizada en el ambiente UAT de Kushki, con una cuenta de México.

## Estado de cada sección

| Sección | Estado | Documento |
|---|---|---|
| I. Kajita | Inconcluso | [Kajita](docs/1-kajita.md) |
| II. Procesamiento API | Inconcluso | [API-Postman](docs/2-api-postman.md) |
| III. Manejo de situaciones con comercios | Completo | [Ejercicio, Manejo de situaciones](docs/3-Manejo-de-situaciones-con-comercios.md) | 
| IV. Feedback | Completo | [Feedback](docs/4-feedback.md) |
| V. Bonus: formulario de pago | Inconcluso | `app.py` y `static/index.html` |

URL pública del Bonus: https://kushki-prueba-tecnica.onrender.com/

## Cómo ejecutar el Bonus localmente

1. Clona el repositorio y entra a la carpeta.
2. Crea y activa un entorno virtual (`python -m venv venv`).
3. Instala las librerías: `pip install -r requirements.txt`.
4. Copia `.env.example` como `.env` y completa tus llaves de UAT.
5. Ejecuta `python app.py` y abre http://127.0.0.1:5000.

## Notas

Se dejan inconclusos ejercicios ya que no se tiene activo el método de pago con tarjetas. En cuanto se active el método de pago con tarjetas o se solucione el problema, se correrán de nuevo las pruebas anexando los resultados correctos y completando cada sección.