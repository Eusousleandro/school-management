import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)

print('A conexão com o banco de dados foi estabelecida com sucesso!'
      if connection else 'Falha ao conectar ao banco de dados.')