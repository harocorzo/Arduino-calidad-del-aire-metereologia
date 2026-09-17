import pandas as pd
import matplotlib.pyplot as plt

# Nombre de tu nuevo archivo
print("dame el mes y el dia MMDD del archivo")
dia=int(input("MMDD")
archivo = dia+"datos_mq135.csv" 
archivo_csv = archivo
# archivo_csv = 'datos_mq135.csv'

try:
    # 1. Cargar los datos del archivo CSV
    datos = pd.read_csv(archivo_csv)

    # Limpiar líneas duplicadas del encabezado 'Tiempo' que causan el error
    datos = datos[datos['Tiempo'] != 'Tiempo'].copy()

    # Convertir 'Valor_Analogico' a tipo numérico por si quedó texto
    datos['Valor_Analogico'] = pd.to_numeric(datos['Valor_Analogico'], errors='coerce')

    # Convertir la columna 'Tiempo' a fecha y hora ignorando errores de formato
    datos['Tiempo'] = pd.to_datetime(datos['Tiempo'], errors='coerce')

    # Eliminar filas con valores nulos o corruptos
    datos.dropna(inplace=True)

    # 2. Configurar la ventana y la gráfica
    plt.figure(figsize=(12, 6))
    
    # Dibujar la curva de lecturas analógicas del sensor
    plt.plot(datos['Tiempo'], datos['Valor_Analogico'], color='#1f77b4', linewidth=1, label='Lectura MQ135 (ADC)')
    
    # Línea horizontal de referencia / umbral
    plt.axhline(y=400, color='r', linestyle='--', linewidth=1.2, label='Umbral de referencia (400)')

    # 3. Títulos y etiquetas de los ejes
    plt.title('Calidad del Aire - Registro MQ135 (' + archivo_csv + ')', fontsize=14, fontweight='bold')
    plt.xlabel('Hora de Medición', fontsize=12)
    plt.ylabel('Valor Analógico (0 - 1023)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right')
    
    # Formatear el eje X para las fechas y horas
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

    # 4. Guardar la gráfica como imagen y mostrarla
    nombre_imagen = archivo_csv.replace('.csv', '.png')
    plt.savefig(nombre_imagen, dpi=300)
    print("¡Gráfica generada exitosamente y guardada como '" + nombre_imagen + "'!")
    plt.show()

except Exception as e:
    print("Error al generar la gráfica: " + str(e))
