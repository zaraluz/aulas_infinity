import mysql.connector

db_config = {
    'host':'localhost',  
    'user': 'root', 
    'password':'Noclaza3@', 
    'database':'fazendas'  
}

def execute_query(query):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

query1 = """
SELECT ano, SUM(producao) AS total_producao
FROM prod_fazendas
GROUP BY ano
ORDER BY total_producao DESC
LIMIT 1
"""
max_year = execute_query(query1)

query2 = """
SELECT ano, SUM(producao) AS total_producao
FROM prod_fazendas
GROUP BY ano
ORDER BY total_producao ASC
LIMIT 1
"""
min_year = execute_query(query2)

print(f"Ano com a produção total máxima: {max_year[0][0]} com produção de {max_year[0][1]}")
print(f"Ano com a produção total mínima: {min_year[0][0]} com produção de {min_year[0][1]}")

query3 = """
SELECT cultura, SUM(producao) AS total_producao
FROM prod_fazendas
GROUP BY cultura
ORDER BY total_producao DESC
LIMIT 1
"""
max_culture = execute_query(query3)

query4 = """
SELECT cultura, SUM(producao) AS total_producao
FROM prod_fazendas
GROUP BY cultura
ORDER BY total_producao ASC
LIMIT 1
"""
min_culture = execute_query(query4)

print(f"Cultura com a maior produção total: {max_culture[0][0]} com produção de {max_culture[0][1]}")
print(f"Cultura com a menor produção total: {min_culture[0][0]} com produção de {min_culture[0][1]}")

ano_especifico = 2022  # você pode alterar o ano conforme necessário
query5 = f"""
SELECT fazendas, MAX(producao) AS max_producao
FROM prod_fazendas
WHERE ano = {ano_especifico}
GROUP BY fazendas
ORDER BY max_producao DESC
LIMIT 1
"""
max_fazenda = execute_query(query5)

query6 = f"""
SELECT fazendas, MIN(producao) AS min_producao
FROM prod_fazendas
WHERE ano = {ano_especifico}
GROUP BY fazendas
ORDER BY min_producao ASC
LIMIT 1
"""
min_fazenda = execute_query(query6)

print(f"No ano de {ano_especifico}, a fazenda com a maior produção: {max_fazenda[0][0]} com produção de {max_fazenda[0][1]}")
print(f"No ano de {ano_especifico}, a fazenda com a menor produção: {min_fazenda[0][0]} com produção de {min_fazenda[0][1]}")