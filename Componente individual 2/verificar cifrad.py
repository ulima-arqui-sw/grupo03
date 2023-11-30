# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 01:52:48 2023

@author: Frank
"""

import boto3

s3_client = boto3.client('s3', region_name='us-east-2', aws_access_key_id='AKIA34KOFUEKGNSPJ3QU', aws_secret_access_key='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')

bucket_name = 'frankbucketprueba1'
response = s3_client.get_bucket_encryption(Bucket=bucket_name)

if 'ServerSideEncryptionConfiguration' in response:
    print(f"El bucket {bucket_name} está encriptado.")
    print("Configuración de encriptación:")
    print(response['ServerSideEncryptionConfiguration'])
else:
    print(f"El bucket {bucket_name} no está encriptado o no se encontró la información de encriptación.")
