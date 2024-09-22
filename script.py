import webbrowser
import time
import pyautogui
import os

# Cargar los correos electrónicos de un archivo de forma segura
file_path = 'correos.txt'

if not os.path.exists(file_path):
    print(f"Error: No se encuentra el archivo {file_path}")
else:
    try:
        with open(file_path, 'r') as documento:
            correos = documento.read().splitlines()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
    
    for email in correos:
        try:
            # Abrir la página de Have I Been Pwned
            webbrowser.open_new("https://haveibeenpwned.com/")
            time.sleep(3)  # Ajustar según la velocidad de carga de la página

            # Escribir el email directamente sin usar el portapapeles
            pyautogui.write(email)
            pyautogui.press("enter")
            
            # Espera hasta que se cargue la página de resultados (se puede ajustar)
            time.sleep(5)

        except Exception as e:
            print(f"Error al procesar el correo {email}: {e}")
