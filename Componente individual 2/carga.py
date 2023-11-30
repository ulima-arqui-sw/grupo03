# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 03:21:05 2023

@author: Frank
"""

import boto3

# Configuración de credenciales de AWS y región
s3_client = boto3.client('s3', region_name='us-east-2', aws_access_key_id='AKIA34KOFUEKGNSPJ3QU', aws_secret_access_key='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')


# Nombre del bucket y archivo local que deseas subir
bucket_name = 'frankbucketprueba1'
file_path = 'C:/Users/Frank/Desktop/Entrega seminario II/fun1.txt'  # Ruta local del archivo que quieres subir
object_key = 'fun1.txt'  # Ruta del objeto en el bucket

# Sube el archivo al bucket
s3_client.upload_file(file_path, bucket_name, object_key)

print(f"Archivo {file_path} subido exitosamente al bucket {bucket_name} como {object_key}")
