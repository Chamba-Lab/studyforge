# 🎤 Presentación de StudyForge (20 nov 2026)

Las diapositivas del evento de lanzamiento en el Discord de [Chamba Lab](https://chambalab.org), y una guía para repetir por tu cuenta la demo en vivo. Van en español porque así se presentó; el framework sigue en inglés.

## 🖥️ Las diapositivas

Abre [`slides.html`](slides.html) en el navegador, sin instalar nada:

- flechas o espacio para avanzar, `Inicio`/`Fin` para ir al principio o al final;
- `F` para pantalla completa;
- el tema ganador (diapositiva 19) y la propuesta del hilo (18) se editan con un clic.

Recorren cuatro partes: qué es StudyForge y qué te ahorra, el ejemplo de [pytest-lab](https://github.com/Chamba-Lab/pytest-lab), la elección del próximo laboratorio y su construcción en vivo. Las imágenes de [`assets/`](assets/) son capturas de las guías de pytest-lab tal como las muestra GitHub y sus diagramas Mermaid.

## 🔨 Hazlo tú: del tema al primer lab

Lo mismo que se hizo en vivo, en tu máquina. Necesitas un agente que lea [Agent Skills](https://agentskills.io), con StudyForge instalada ([cómo instalarla](../../../README.es.md#-instalación)), git y Python 3.11 o superior.

1. **Abre tu agente en una carpeta vacía** y pídele el sílabo. Este es el pedido del evento, para un camino de seguridad web:

   ```txt
   Usa StudyForge para diseñar un camino de estudio de seguridad web práctica.
   - Para qué: personas Early Career que empiezan en ciberseguridad o en desarrollo y quieren escribir código seguro.
   - Punto de partida: Python básico y nociones de HTTP y SQL; nada de seguridad.
   - Enfoque: atacar y arreglar una app vulnerable que corre en local. En cada reto, una prueba-ataque falla mientras la app es vulnerable y pasa cuando el arreglo la bloquea; las pruebas funcionales siguen en verde.
   - El bloque 1 cierra con un proyecto: endurecer una app pequeña hasta que ningún ataque de la suite funcione.
   - Sesiones de 1–2 h, dos por semana. Windows, PowerShell y Bash, Python 3.12+, sin Docker en el camino principal.
   - Contenido en español. Todo se ataca en local, nunca a terceros.
   Planifica el camino completo y deja el bloque 1 listo para construir.
   ```

   Para otro tema, la misma forma:

   ```txt
   Usa StudyForge para diseñar un camino de estudio de <tema>.
   - Para qué: <tu objetivo: un trabajo, una certificación, un proyecto>.
   - Punto de partida: <lo que ya sabes>.
   - Cada lab se verifica con <pruebas o scripts>.
   - Sesiones de <duración>, <cuántas> por semana. <Tu sistema y tus terminales>.
   - Contenido en <idioma>.
   Planifica el camino completo y deja el bloque 1 listo para construir.
   ```

   Un pedido que ya responde para qué, nivel, tiempo, entorno e idioma ahorra las preguntas del agente. Revisa el borrador que te muestre y pide cambios hasta que te convenza.
2. **Crea el repositorio:** «Crea el repositorio de estudio en esta carpeta». El agente escribe `studyforge.toml`, `AGENTS.md`, `SYLLABUS.md`, `SETUP.md` y `tools/verify.py`, y hace el primer commit. Publicarlo es decisión tuya.
3. **Construye los labs:** «Siguiente lab», o uno en particular («Construye el lab 1.2»). Cada lab sale construido, verificado y commiteado, uno a la vez.
4. **Resuélvelo y cuéntalo:** lo que digas de un lab («Esto me costó en el 1.2…») lo mejora a él, a los siguientes y, si es una lección general, a StudyForge.

> [!TIP]
> En un camino de seguridad, la prueba-ataque hace el papel de la caza de mutantes de pytest-lab, al revés: ahí tus pruebas tenían que atrapar bugs; aquí tu código tiene que resistir ataques. Se ataca solo la app del propio lab, en tu máquina.

## 🔗 Enlaces

- [StudyForge](https://github.com/Chamba-Lab/studyforge) · [README en español](../../../README.es.md)
- [pytest-lab](https://github.com/Chamba-Lab/pytest-lab), el laboratorio que muestran las diapositivas
- [Entrada del blog](https://chambalab.org/blog/studyforge/)
