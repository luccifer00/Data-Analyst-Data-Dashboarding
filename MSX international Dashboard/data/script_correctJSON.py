import json
import csv

# Cargar el JSON
with open('clientes.json', 'r') as f:
    data = json.load(f)

# Extraer los encabezados y las filas de datos
headers = data[0]
rows = data[1:]

# Guardar en un archivo CSV
with open('clientes_cleaned.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # Escribir los encabezados
    writer.writerows(rows)    # Escribir las filas de datos


