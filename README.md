# QA-IA-Video-Platform
# 1. Introducción
El objetivo de este plan de pruebas es asegurar la calidad y el correcto funcionamiento de los algoritmos de inteligencia artificial diseñados para corregir automáticamente los eventos de inicio/fin en la guía electrónica de programación (EPG) de una plataforma de video. Este plan abarca tanto **pruebas funcionales como no funcionales**.

# 2. Alcance
- Pruebas Funcionales: Verificación de la corrección de los eventos de inicio/fin en la EPG.
- Pruebas No Funcionales: Evaluación del rendimiento, escalabilidad, usabilidad y seguridad del sistema.

# 3. Herramientas y Tecnologías
Herramientas de Automatización de Pruebas: Selenium, JUnit/TestNG, PyTest.
Herramientas de Gestión de Configuraciones: Git, Docker.
Herramientas de CI/CD: Jenkins, GitHub Actions.
Entorno de Desarrollo: Python, TensorFlow/PyTorch para IA.
Gestión de Proyectos: Jira, Confluence.

# 4. Estrategia de Pruebas
## 4.1. Pruebas Funcionales
### 4.1.1. Casos de Prueba Funcionales
**Verificación de la Corrección de Eventos de Inicio/Fin:**
Descripción: Validar que el algoritmo corrige correctamente los eventos de inicio/fin en la EPG.
Entradas: Lista de eventos programados y eventos reales.
Acciones: Comparar las correcciones sugeridas por el algoritmo con los eventos reales.
Resultados Esperados: Las correcciones deben coincidir con los eventos reales.

**Manejo de Eventos Simultáneos:**
Descripción: Verificar que el algoritmo maneje correctamente eventos que ocurren simultáneamente en diferentes canales.
Entradas: Lista de eventos simultáneos.
Acciones: Evaluar las correcciones propuestas para cada canal.
Resultados Esperados: Las correcciones deben ser precisas para todos los canales.

**Ajuste de Eventos Repetitivos:**
Descripción: Validar que el algoritmo ajusta correctamente eventos que se repiten en un intervalo regular.
Entradas: Lista de eventos repetitivos.
Acciones: Comparar las correcciones con los intervalos repetitivos esperados.
Resultados Esperados: Las correcciones deben mantener la regularidad de los eventos.

### 4.1.2. Escenarios de Prueba
**Escenario de Prueba 1:**
Descripción: Corrección de un evento que empieza tarde.
Entradas: Evento programado a las 18:00, evento real empieza a las 18:15.
Acciones: Ejecutar el algoritmo y verificar la corrección.
Resultados Esperados: El evento debe ser ajustado para empezar a las 18:15.

**Escenario de Prueba 2:**
Descripción: Corrección de un evento que termina temprano.
Entradas: Evento programado a las 19:00, evento real termina a las 18:50.
Acciones: Ejecutar el algoritmo y verificar la corrección.
Resultados Esperados: El evento debe ser ajustado para terminar a las 18:50.

**Escenario de Prueba 3:**
Descripción: Corrección de múltiples eventos en diferentes canales.
Entradas: Lista de eventos en varios canales.
Acciones: Ejecutar el algoritmo y verificar las correcciones.
Resultados Esperados: Todos los eventos deben ser corregidos adecuadamente en cada canal.

## 4.2. Pruebas No Funcionales
### 4.2.1. Pruebas de Rendimiento
**Carga de Eventos:**
Descripción: Evaluar el rendimiento del algoritmo bajo una carga alta de eventos.
Acciones: Ejecutar el algoritmo con una gran cantidad de eventos simultáneos.
Resultados Esperados: El algoritmo debe corregir los eventos dentro de un tiempo aceptable.

**Escalabilidad:**
Descripción: Verificar la capacidad del algoritmo para escalar con el aumento de datos.
Acciones: Aumentar gradualmente el número de eventos y medir el rendimiento.
Resultados Esperados: El algoritmo debe escalar linealmente con un rendimiento aceptable.

### 4.2.2. Pruebas de Usabilidad
**Interfaz de Usuario:**
Descripción: Evaluar la facilidad de uso de la interfaz de usuario para verificar y corregir eventos.
Acciones: Realizar pruebas con usuarios finales.
Resultados Esperados: Los usuarios deben encontrar la interfaz intuitiva y fácil de usar.

### 4.2.3. Pruebas de Seguridad
**Integridad de los Datos:**
Descripción: Asegurar que los datos de los eventos no se pierdan o corrompan durante la corrección.
Acciones: Ejecutar pruebas de corrección y verificar la integridad de los datos.
Resultados Esperados: Los datos deben mantenerse íntegros y sin corrupción.

# 5. Plan de Ejecución de Pruebas
## 5.1. Cronograma
Semana 1-2: Configuración del entorno de pruebas y herramientas.
Semana 3-4: Diseño y desarrollo de casos de prueba automatizados.
Semana 5-6: Ejecución de pruebas funcionales.
Semana 7-8: Ejecución de pruebas no funcionales.
Semana 9: Revisión de resultados y ajustes necesarios.
## 5.2. Responsabilidades
QA Lead: Coordinación general, planificación y revisión.
QA Engineers: Diseño, desarrollo y ejecución de casos de prueba.
Desarrolladores: Asistencia en la configuración del entorno y corrección de errores.
Usuarios Finales: Pruebas de usabilidad y retroalimentación.

# 6. Reporte y Seguimiento de Defectos
Utilización de Jira para reportar, seguir y gestionar defectos.
Revisión diaria de defectos y planificación de correcciones.
Reportes semanales al equipo de desarrollo y stakeholders.

# 7. Conclusiones
Este plan de pruebas está diseñado para garantizar una cobertura exhaustiva y efectiva de las funcionalidades de corrección de eventos de inicio/fin en la EPG de la plataforma de video, utilizando un enfoque sistemático y herramientas de pruebas automatizadas.
