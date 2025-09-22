# detectBW

**detectBW** es una herramienta pequeña para detectar dispositivos Bluetooth y redes Wi‑Fi cercanas. Está pensada para **auditorías de red autorizadas y pruebas de laboratorio**.

> ⚠️ **Advertencia:** Este proyecto puede facilitar actividades de monitoreo inalámbrico. Úsalo **solo** en entornos donde tengas permiso explícito (tu propia red o con autorización). El autor no se responsabiliza por el uso indebido.

## Características
- Escaneo de dispositivos Bluetooth (usa `bleak`).
- Escaneo de redes Wi‑Fi en Windows mediante `netsh` (comando nativo de Windows).
- Salida por consola con nombre (si está disponible) y dirección MAC / BSSID.

## Requisitos
- Python 3.8+
- Adaptador Bluetooth activado y permisos para utilizarlo.
- En Windows: `netsh` disponible (incluido en Windows). Para ver redes Wi‑Fi desde Linux o macOS necesitarás adaptar el script (ej. `iwlist`, `nmcli`, o `airport`).

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/6Edgar9/detectBW.git
cd detectBW
```

2. (Opcional) Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script principal:
```bash
python detectBW.py
```

- El script intentará escanear dispositivos Bluetooth mediante `bleak` y luego escanear redes Wi‑Fi usando `netsh` (Windows).
- Si ejecutas en Linux/macOS, la parte de `detect_wifi_devices()` no funcionará tal cual; necesitarás adaptar el comando al sistema (por ejemplo `iwlist` o `nmcli` en Linux, y `airport` en macOS).

## Notas técnicas

- `bleak` usa backends nativos para Bluetooth en cada plataforma. Asegúrate de tener el adaptador BT habilitado y permisos (en algunos sistemas puede requerirse ejecución con privilegios).
- El escaneo Wi‑Fi actual utiliza `subprocess` para invocar `netsh` y parsear su salida con expresiones regulares. La exactitud depende del formato de salida del comando en la versión de Windows donde se ejecute.

## Buenas prácticas y consideraciones legales

- Solo realiza escaneos en redes y dispositivos sobre los que tengas autorización. Realizar escaneos sin permiso puede ser ilegal en muchas jurisdicciones.
- Evita almacenar información sensible recopilada sin consentimiento.
- Para auditorías profesionales considera herramientas especializadas y un plan de pruebas con alcance y autorización por escrito.

## Posibles mejoras

- Añadir soporte multiplataforma para escaneo Wi‑Fi (detección automática del sistema operativo).
- Exportar resultados a JSON o CSV con marca temporal.
- Añadir opciones de línea de comandos (`--no-wifi`, `--output results.json`, `--timeout 10`).
- Manejo de errores y logs con niveles (info/warn/error).

---

#### Dios, Assembly y la Patria
#### Edrem

Desarrollado con fines académicos y de práctica en Python.
