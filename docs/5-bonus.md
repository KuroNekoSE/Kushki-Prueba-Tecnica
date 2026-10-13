## Bonus, Despliegue de Forumlario de pago en hosting publico.

**Fecha:** 11/10/2026
**Ambiente:** UAT, cuenta de México

**Objetivo:** Desplegar un formulario de tarjetas que cumpla con los siguientes objetivos.
1. Request a card token. Usar la librería Kushki.js para obtener el token en el frontend.
2. Make a charge (Debe usarse el API).
3. Mostrar el resultado de la operación en pantalla (Deben soportarse
transacciones declinadas y aprobadas).

```mermaid
   sequenceDiagram
       participant N as Navegador
       participant S as Servidor Flask
       participant K as Kushki UAT
       N->>K: requestToken (Kushki.js, llave pública)
       K-->>N: token (o error K322)
       N->>S: POST /api/charge con el token
       S->>K: POST /card/v1/charges (llave privada)
       K-->>S: respuesta del cobro
       S-->>N: approved / declined / error
```

**Problemas encontrados y acciones tomadas**
Se encontró código de rechazo "K322" al tratar de tokenizar tarjetas por medio de API, lo comuniqué con el equipo de Kushki para recibir ayuda y se documentó el error. Se dejan todos los ambientes preparados para realizar las pruebas pertinentes cuando se tenga respuesta de Kushki.

**Evidencia:** 
![Renderizado del Formulario y codigo de error "K322" ](img/Bonus.png)


**Fecha** 13/10/2026
El equipo de Kushki ayudó a activar el método de pago con tarjeta por lo cuál se repitieron las pruebas en los ambientes ya antes preparados teniendo exito en las pruebas requisitadas en el apartado de *Objetivo*

## Tarjetas de prueba utilizadas

Tarjetas oficiales del ambiente UAT de Kushki (México). En todas se usó una fecha de vencimiento futura y un CVV cualquiera.

| Escenario | Tarjeta |
|---|---|---|---|---|---|
| Aprobada | `5451951574925480` | 
| Declinada al pedir el token | `4574441215190335` |
| Declinada al cobrar | `4349003000047015` | 


**Evidencia**
![Renderizado del Formulario con procesamiento aprobado](img/PagoAprobado.png)

![Renderizado del Formulario con pago declinado por validación](img/Tokeninvalido.png.png)

![Renderizado del Formulario con pago declinado](img/Transacciondeclinada.png)

**URL probada:** https://kushki-prueba-tecnica.onrender.com