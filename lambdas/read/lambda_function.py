import json
import os
import psycopg2

def lambda_handler(event, context):
    from datetime import datetime
    now = datetime.now()
    name = event['name']
    name = name.replace(" ", "")
    connection = False
    try:
        conn = psycopg2.connect(**conn_config)
        print("Connection successful")
        connection = True
    except psycopg2.OperationalError as e:
        print(f"An error occurred: {e}")
    heroes = {'DC': ['batman', 'superman', 'flash'], 'marvel': ['ironman', 'thor', 'captainamerica']}
    studio = 'this hero is not part of any franchise'
    for k,v in heroes.items():
        if name.lower() in v:
            studio = k
    data = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT * from blog_blog")
        data = cur.fetchall()
        print(data)
        cur.close()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
    return {
        'statusCode': 200,
        'body': str(now),
        'studio': studio,
        'get_blogs': data,
        'connection': connection

    }

conn_config = {
    'dbname': os.getenv('DATABASE_NAME'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'port': os.getenv('DATABASE_PORT')
}








