import requests

def descargar_csv_desde_url(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        with open(nombre_archivo, 'wb') as archivo_csv:
            archivo_csv.write(response.content)

        print(f"Descarga exitosa. Los datos se han guardado en {nombre_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")


url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
nombre_archivo = 'datos_descargados.csv'
descargar_csv_desde_url(url, nombre_archivo)
