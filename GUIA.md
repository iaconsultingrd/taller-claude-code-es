# Guía del facilitador

## Agenda (2 horas)

| Tiempo | Bloque |
| - | - |
| 0:00 – 0:15 | Bienvenida: qué es un agente de código y en qué se diferencia de un chat |
| 0:15 – 0:30 | Instalación e inicio de sesión |
| 0:30 – 1:30 | Ejercicios 1 al 5 (en parejas) |
| 1:30 – 1:50 | Demo libre: los asistentes muestran lo que construyeron |
| 1:50 – 2:00 | Buenas prácticas, uso responsable y cierre |

## Antes del taller

- Pide a los asistentes que instalen Claude Code y prueben `claude --version` desde casa.
- Ten Wi-Fi estable y un plan B (algunos pueden trabajar en parejas).
- Prueba todos los ejercicios tú mismo el día anterior.

## Instalación

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Verificar
claude --version
```

Al ejecutar `claude` por primera vez, se abre el navegador para iniciar sesión.

## Comandos que todos deben conocer

| Comando | Para qué sirve |
| - | - |
| `claude` | Iniciar una sesión en la carpeta actual |
| `claude -c` | Continuar la conversación más reciente |
| `/help` | Ver los comandos disponibles |
| `/init` | Crear un `CLAUDE.md` con el contexto del proyecto |
| `/clear` | Limpiar la conversación |
| `Shift+Tab` | Cambiar el modo de permisos |

---

## Ejercicio 1 — Entender un proyecto ajeno (10 min)

Entra a `proyecto-inicial/` y ejecuta `claude`. Pregunta:

```text
¿Qué hace este proyecto? Explícamelo como si fuera mi primer día en el equipo.
```

**Objetivo:** ver que Claude lee los archivos por su cuenta; no hace falta copiar y pegar código.

## Ejercicio 2 — Encontrar y corregir un error (15 min)

```text
Ejecuta los tests. Si alguno falla, encuentra la causa, explícamela y corrígela.
```

**Pista para el facilitador:** `desglosar_itbis` usa una fórmula incorrecta. Antes de aceptar el cambio, pide a los asistentes que lean la explicación de Claude y digan si la entienden. La idea es aprender, no solo aceptar.

## Ejercicio 3 — Dar contexto con CLAUDE.md (10 min)

```text
/init
```

Abre el `CLAUDE.md` generado y agrega una regla, por ejemplo:

```markdown
- Escribe los mensajes de error y comentarios en español.
- Todos los montos se redondean a 2 decimales.
```

**Objetivo:** mostrar que el contexto del proyecto cambia cómo trabaja Claude.

## Ejercicio 4 — Agregar una funcionalidad con tests (15 min)

```text
Agrega una función que valide si un RNC dominicano tiene un formato y dígito
verificador válidos. Investiga primero el algoritmo, explícamelo, y escribe
los tests antes de la implementación.
```

**Objetivo:** pedir un plan antes del código y trabajar con tests primero.

## Ejercicio 5 — Git conversacional (10 min)

```text
¿Qué archivos he cambiado? Haz un commit con un mensaje descriptivo en español.
```

---

## Cierre: buenas prácticas y uso responsable

- **Sé específico.** "Corrige la fórmula de `desglosar_itbis`" funciona mejor que "arregla el bug".
- **Revisa todo antes de aceptar.** Tú eres responsable del código que se sube.
- **No compartas secretos.** Nunca pegues contraseñas, tokens ni datos personales de clientes.
- **Divide tareas grandes** en pasos pequeños y verificables.
- **Sigue aprendiendo:** https://academy.claude.com
