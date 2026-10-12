# Technical Assessment - Technical Support Engineer (Kushki)

Prueba técnica realizada en el ambiente UAT de Kushki, con una cuenta de México.

## Estado de cada sección

| Sección | Estado | Documento |
|---|---|---|
| I. Kajita | Inconcluso | [docs/2-kajita.md](docs/2-kajita.md) |
| II. Procesamiento API | Inconcluso | [docs/3-api-postman.md](docs/3-api-postman.md) |
| III. Manejo de situaciones con comercios | Completo | ... |
| IV. Feedback | Completo | [docs/4-feedback.md](docs/4-feedback.md) |
| Bonus: formulario de pago | Inconcluso | `app.py` y `static/index.html` |

URL pública del Bonus: ...

## Cómo ejecutar el Bonus localmente

1. Clona el repositorio y entra a la carpeta.
2. Crea y activa un entorno virtual (`python -m venv venv`).
3. Instala las librerías: `pip install -r requirements.txt`.
4. Copia `.env.example` como `.env` y completa tus llaves de UAT.
5. Ejecuta `python app.py` y abre http://127.0.0.1:5000.

## Notas

Se dejan inconclusos ejercicios ya que no se tiene activo el método de pago con tarjetas. 