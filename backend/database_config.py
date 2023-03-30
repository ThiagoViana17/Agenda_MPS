import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': 3306,
  'database': 'agenda'
}

conn = mysql.connector.connect(**config)

# Exporta a conexão como uma variável
__all__ = ['conn']
