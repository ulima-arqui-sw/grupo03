# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 02:24:04 2023

@author: Frank
"""

import boto3

s3_client = boto3.client('s3', region_name='us-east-2', aws_access_key_id='AKIA34KOFUEKGNSPJ3QU', aws_secret_access_key='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')

bucket_name = 'frankbucketprueba1'

downloaded_file = 'C:/Users/Frank/Desktop/Entrega seminario II/Archivos encriptados/archivo_descargado.txt'  # Ruta donde se descargará el archivo

response = s3_client.get_object(Bucket=bucket_name, Key='prueba de encriptado.txt')
encrypted_data = response['Body'].read()

# Guarda el archivo encriptado en el sistema local
with open(downloaded_file, 'wb') as file:
    file.write(encrypted_data)

print("Archivo encriptado descargado y guardado localmente.")
