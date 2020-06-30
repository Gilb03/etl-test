import requests
import psycopg2 


with requests.get("http://127.0.0.1:5000/very_large_request/10") as r:
    print(r.text)
                  