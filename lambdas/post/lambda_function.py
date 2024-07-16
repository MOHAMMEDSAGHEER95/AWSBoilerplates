import json
import os

import psycopg2


def lambda_handler(event, context):
    conn_config = {
        'dbname': os.getenv('DATABASE_NAME'),
        'user': os.getenv('DATABASE_USER'),
        'password': os.getenv('DATABASE_PASSWORD'),
        'host': os.getenv('DATABASE_HOST'),
        'port': os.getenv('DATABASE_PORT')
    }

    request_body = {}

    try:
        conn = psycopg2.connect(**conn_config)
        cur = conn.cursor()
        request_body = event.get('body', '')
        title = request_body.get('title')
        body = request_body.get('body')
        cur.execute("INSERT INTO blog_blog (title, body) VALUES (%s, %s)", (title, body))
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }
    finally:
        print("hello")

    return {
        'statusCode': 200,
        'body': json.dumps(request_body)
    }