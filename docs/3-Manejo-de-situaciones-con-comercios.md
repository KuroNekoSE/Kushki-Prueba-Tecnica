# III. Manejo de Situaciones Críticas con Comercios e Incidentes

**Fecha:** 11/10/2026
**Objetivo:** Evaluar el criterio técnico, la comunicación en crisis y el protocolo de gestión de incidentes ante afectaciones en el procesamiento de pagos.

---

## Caso 1: Error Crítico en API con Solución Definitiva a 1 Semana (Fix de Plataforma)

### Contexto del Incidente
* **Impacto:** Alto (Afecta el procesamiento directo del comercio).
* **Estado:** Incidente identificado y reportado por el equipo de Producto/Core.
* **Tiempo de resolución definitiva (ETA):** 7 días calendario.
* **Estado del Comercio:** Altamente insatisfecho, exige resolución inmediata en la llamada.

---

### A. Estrategia de Manejo de la Llamada / Comunicación (Paso a Paso)

1. **Escucha activa y validación del impacto:**
   * Permitir que el comercio exprese la afectación sin interrupciones.
   * Reconocer explícitamente el impacto financiero y operativo que esto genera en su negocio.

2. **Transparencia con el cliente:**
   * Confirmar que el incidente ya está registrado en el sistema de gestión de Kushki y categorizado con la máxima prioridad por el equipo de ingeniería.
   * Explicar de forma clara que la solución de raíz requiere una actualización en la infraestructura central que debe pasar por pruebas de seguridad estrictas antes de desplegarse a producción. 

3. **Propuesta de Workaround / Solución Temporal (Paso Crítico):**
   * Para desbloquear al comercio **de inmediato**, se deben ofrecer alternativas de contingencia operativas mientras se despliega el *fix*:
     * **Opción A :** Cambiar temporalmente la configuración del adquirente/procesador desde la consola de Kushki para evitar la ruta afectada.
     * **Opción B (Integración alternativa):** Ofrecer la implementación de **Cajita (Formulario Embebido)**, **Smartlink / Links de Pago** o **Hosted Fields** si el fallo está acotado exclusivamente a la integración directa por API (`/charges` / `/tokens`).
     * **Opción C:** Habilitar el uso de botones de pago o algún otro feature que pueda ser de utilidad.

4. **Acuerdos y Plan de Seguimiento (SLA de Comunicación):**
   * Establecer un canal directo de seguimiento (vía Ticket / Slack Connect / Correo con copias ejecutivas).
   * Comprometer reportes de avance periódicos (ej. cada 24 horas o tras cada hito del equipo de release) aunque no haya cambiado el status.

---

### B. Información Oficial Suministrada al Comercio

Información Permitida / Aportada: 
1. Código de ticket / referencia de incidente global.
2. Explicación funcional del comportamiento del error. 
3. Plan de mitigación temporal (Workaround técnico). 
4. Cronograma de avances y fecha estimada del release (ETA). 

---

## Caso 2: Error Crítico causado por un Tercero (Procesador, Banco Emisor o Proveedor)

### Contexto del Incidente
* Falla externa (Degradación de red de adquirencia, rechazos masivos de un banco emisor, caída del algun servicio de terceros).
* **Estado del Comercio:** Molesto, atribuye la responsabilidad total a Kushki y exige solución inmediata.

---

### A. Protocolo de Actuación e Investigación

1. **Validación Técnica y Aislamiento de la Falla:**
   * Analizar los logs de la API y los códigos de respuesta del procesador/banco. 
   * Confirmar si el porcentaje de conversión cayó drásticamente para una BIN específica o para un adquirente en particular.

2. **Comunicación Táctica y Transparente:**
   * Aclarar que, aunque la falla reside en la red del procesador/banco, Kushki es su único punto de contacto y gestionará la crisis de principio a fin.
   * Mostrar métricas o extractos de respuesta del tercero (sin exponer datos sensibles) donde se demuestre que la transacción es enviada correctamente por Kushki pero rechazada/no respondida por el tercero.

3. **Acciones de Mitigación Inmediata:**
   * Si la cuenta del comercio cuenta con otros canales de adquirencia configurados o disponibles, redirigir el tráfico transaccional a un procesador alternativo de forma inmediata.
   * Desactivar o pausar temporalmente la opción de pago con la franquicia o banco afectado si genera cobros pendientes. 

4. **Escalamiento con el Proveedor / Banco:**
   * Abrir un ticket de prioridad P1 / Incidente Crítico con el área de operaciones del procesador o adquirente.
   * Mantener al comercio informado sobre el *Status Page* oficial o comunicado emitido por el proveedor/tercero.
