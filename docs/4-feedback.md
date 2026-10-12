# IV. Feedback, Oportunidades de Mejora y Conceptos Técnicos

**Fecha y hora:** 11/10/2026
**Ambiente:** UAT, cuenta de México

---

## 1. Experiencia de Onboarding con Kushki

### Diagnóstico de la Experiencia
El proceso de integración inicial es ágil y directo en cuanto a la creación de la cuenta y el acceso a las credenciales Sandbox. Sin embargo, el hecho de que no estén activos todos los métodos de pago en Sandbox, reduce la posibilidad de que un cliente pueda probar todo el poder de la API de pagos de Kushki.

### Oportunidades de Mejora Identificadas
* **Activación Automática de Métodos de Pago en Sandbox:** Al crear una cuenta UAT, algunos métodos de pago (como Tarjetas) no vienen habilitados por defecto, requiriendo solicitudes manuales a Soporte/Onboarding que generan bloqueos (ej. código de error `K322`).

---

## 2. Experiencia con la Documentación Técnica y Propuesta de Mejora

### Diagnóstico y Oportunidades de Mejora
La documentación oficial provee guías visuales y ejemplos de integración bien estructurados. No obstante, presenta áreas de oportunidad en la gestión de errores y en la simulación de pruebas:

1. **Códigos de Error Ambiguos:** Mensajes de error como `K322` o `K067` no detallan claramente en el *response body* si la causa es un problema de formato, credenciales faltantes o permisos de cuenta.
2. **Dependencia de Flujos Secuenciales para Pruebas:** Para probar `/charge` o `/void`, el desarrollador depende de haber generado previamente un token válido en la misma sesión. Si la tokenización falla por configuración, todo el testing posterior queda bloqueado.

### Propuesta de Mejora
* Incluir en la documentación una lista de **Tokens Estáticos y Tickets Ficticios de Prueba** (ej. `test_token_approved_123`) que permitan probar el endpoint `/charge` directamente desde Postman sin depender del paso previo de tokenización.
* **Catálogo de Errores con Troubleshooting:** Crear una matriz interactiva de códigos de error donde el desarrollador pueda ingresar un código (ej. `K322`) y obtener inmediatamente la causa raíz probable y la solución sugerida.
* También se encontraron varios detalles minimos (ej. Endpoints mal escritos, ejemplos de código de otros países en la documentación de MX, errores ortograficos.)

---

## 3. Concepto de Tokenización y Ventajas de Tokenizar en el Frontend

### ¿Qué es la Tokenización?
La **Tokenización** es el proceso de reemplazar datos sensibles de tarjetas de crédito o débito (Los 16 dígitos, fecha de expiración y CVV) por un valor alfanumérico denominado **Token**. 

Este token actúa como un identificador único de la tarjeta dentro de la pasarela de pagos (Kushki), pero carece de valor intrínseco si es interceptado por un tercero fuera del contexto transaccional autorizado.

### ¿Por qué se recomienda tokenizar mediante una solución del Frontend?

1. Al capturar y tokenizar la tarjeta directamente en el navegador/app del cliente (usando el SDK de JS o Hosted Fields de Kushki), los datos financieros **viajan directamente desde el cliente hacia los servidores seguros de Kushki**.

El servidor backend del comercio nunca toca, procesa ni almacena datos de tarjeta.

2. Si la infraestructura backend del comercio llega a ser vulnerada, los atacantes únicamente encontrarían tokens inútiles y ninguna información de tarjeta expuesta.

3. **Mejor Experiencia de Usuario y Desempeño:**
   * La validación de formato (fecha de vencimiento, longitud de CVV) se realiza en tiempo real en el cliente antes de enviar la petición a los servidores de pagos.

---

## 4. ¿Qué es un Webhook?

### Concepto
Un **Webhook** es un mecanismo de comunicación asíncrona entre sistemas basado en eventos. En el contexto de pagos, es una notificación **HTTP POST** que la pasarela de pagos (Kushki) envía automáticamente hacia una URL (*Endpoint*) configurada por el comercio cuando ocurre un evento específico en su plataforma.

Las transacciones de pago no siempre responden de manera síncrona inmediata. Existen eventos asíncronos como:
* Verificaciones de **3D Secure** (autenticación bancaria que redirige al usuario).
* Pagos diferidos en efectivo o transferencias bancarias (*Cash / Payouts*).
* Cambios de estado en disputas, contracargos o devaluaciones de estado.

En lugar de que el servidor del comercio esté realizando peticiones constantes para saber si una transacción cambió de estado, el **Webhook** notifica de forma proactiva al backend en cuanto la pasarela confirma el evento.