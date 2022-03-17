from os import sep
import boto3
import pandas as pd


s3_client = boto3.client('s3')

#s3_client.download_file("datalake-educosta-igti-edc", "data/ITENS_PROVA_2019.csv", "data/ITENS_PROVA_2019.csv")
#s3_client.download_file("datalake-educosta-igti-edc", "data/MICRODADOS_ENEM_2019.csv", "data/MICRODADOS_ENEM_2019.csv")
#s3_client.download_file("datalake-educosta-igti-edc", "dms/public/login_ast/LOAD00000001.csv", "dms/public/login_ast/LOAD00000001.csv")


#df = pd.read_csv("data/ITENS_PROVA_2019.csv",sep=";", encoding='latin1')
#dados = pd.read_csv("data/MICRODADOS_ENEM_2019.csv",sep=";",encoding='latin1')
#print(df)
#df.loc[(df['SG_AREA']=='LC')]
#print(df.loc[(df['SG_AREA']=='LC')])
#print(dados)
#print(dados.loc[(dados['NO_MUNICIPIO_NASCIMENTO']=='Recife')&(dados['NO_MUNICIPIO_PROVA']=='Recife')])
#print(dados.loc[(dados['NO_MUNICIPIO_RESIDENCIA']=='Belo horizonte')&(dados['NO_MUNICIPIO_PROVA']=='Recife')])


#df = pd.read_csv("dms/public/login_ast/LOAD00000001.csv",sep=",",encoding='latin1')
#print(df)

s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv",  "datalake-educosta-igti-edc", "raw-data/enem/MICRODADOS_ENEM_2020.csv")