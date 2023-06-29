import sqlite3 
# Conexión a la base de datos 
conn = sqlite3.connect('sistema_electrico.db') 
cursor = conn.cursor()

def obtener_mantenimientos_ineficiente(equipo_id): 
    query = "SELECT * FROM Mantenimientos" 
    cursor.execute(query) 
    mantenimientos = cursor.fetchall() 
    mantenimientos_equipo = [] 
    for mantenimiento in mantenimientos: 
        if mantenimiento[1] == equipo_id: 
            mantenimientos_equipo.append(mantenimiento) 
    return mantenimientos_equipo 
    # Llamada a la función de consulta 
    equipo_id = 1 
    mantenimientos_equipo = obtener_mantenimientos_ineficiente(equipo_id) 
    # Imprimir los resultados 
    for mantenimiento in mantenimientos_equipo: 
        print(mantenimiento) 
    # Cerrar la conexión a la base de datos 
    conn.close()
  
  
"""
    La llamada a la función obtener_mantenimientos_ineficiente y la impresión 
    de los resultados se encuentran dentro de la definición de la función, 
    lo cual provoca que no se ejecuten correctamente.
    
    Tambien se mejora la consulta para obtener un mejor resultado. 
    Para ello, se utilizo un JOIN entre las tablas "Mantenimientos" y "Equipos" 
    para obtener los mantenimientos relacionados con un equipo específico y 
    también obtener información adicional del equipo en la misma consulta.
    
    query_mejorada:
     
        SELECT M.*, E.nombre, E.tipo, E.ubicacion
        FROM Mantenimientos AS M
        INNER JOIN Equipos AS E ON M.equipo_id = E.equipo_id
        WHERE M.equipo_id = ?
    
    Código corregido:
"""
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('sistema_electrico.db')
cursor = conn.cursor()

def obtener_mantenimientos_ineficiente(equipo_id):
    query = "SELECT * FROM Mantenimientos"
    query_mejorada = f"SELECT M.*, E.nombre, E.tipo, E.ubicacion FROM Mantenimientos AS M INNER JOIN Equipos AS E ON M.equipo_id = E.equipo_id WHERE M.equipo_id = {equipo_id}"

    cursor.execute(query)
    mantenimientos = cursor.fetchall()
    mantenimientos_equipo = []
    for mantenimiento in mantenimientos:
        if mantenimiento[1] == equipo_id:
            mantenimientos_equipo.append(mantenimiento)
    return mantenimientos_equipo

# Cerrar la conexión a la base de datos
conn.close()

# Llamada a la función de consulta
equipo_id = 1
mantenimientos_equipo = obtener_mantenimientos_ineficiente(equipo_id)

# Imprimir los resultados
for mantenimiento in mantenimientos_equipo:
    print(mantenimiento)