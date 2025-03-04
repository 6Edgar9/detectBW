import asyncio
import subprocess
import re
from bleak import BleakScanner

async def detect_bluetooth_devices():
    print("Escaneando dispositivos Bluetooth...")
    devices = await BleakScanner.discover()
    if devices:
        print(f"Se encontraron {len(devices)} dispositivos Bluetooth:")
        for device in devices:
            # Si el nombre del dispositivo es None, lo reemplazamos con "Desconocido"
            name = device.name if device.name else "Desconocido"
            print(f"Dispositivo: {name} - Dirección MAC: {device.address} (Bluetooth)")
    else:
        print("No se encontraron dispositivos Bluetooth.")

def detect_wifi_devices():
    print("Escaneando redes Wi-Fi...")
    try:
        # Ejecuta el comando netsh para obtener redes Wi-Fi
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
        output = result.stdout

        # Busca SSIDs y BSSIDs en la salida
        ssids = re.findall(r"SSID\s+\d+\s+:\s+(.+)", output)
        bssids = re.findall(r"BSSID\s+\d+\s+:\s+(.+)", output)

        if ssids:
            print(f"Se encontraron {len(ssids)} redes Wi-Fi:")
            for ssid, bssid in zip(ssids, bssids):
                print(f"Red Wi-Fi: SSID: {ssid}, BSSID: {bssid} (Wi-Fi)")
        else:
            print("No se encontraron redes Wi-Fi.")
    except Exception as e:
        print(f"Error al escanear redes Wi-Fi: {e}")

def main():
    print("Iniciando escaneo de dispositivos cercanos...")
    asyncio.run(detect_bluetooth_devices())
    print("\n")
    detect_wifi_devices()

if __name__ == "__main__":
    main()