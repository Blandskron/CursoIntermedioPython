import re

# Lista de correos electrónicos de ejemplo
correos = ["usuario1@example.com", "usuario2@gmail.com", "usuario3@example"]

# Patrón para validar direcciones de correo electrónico
patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Validación de cada correo electrónico en la lista
for correo in correos:
    if re.match(patron_correo, correo):
        print(f"{correo} es una dirección de correo válida.")
    else:
        print(f"{correo} no es una dirección de correo válida.")
