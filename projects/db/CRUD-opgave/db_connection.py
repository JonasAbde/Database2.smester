import psycopg2

def connect():
    return psycopg2.connect(
        dbname='sensordata',
        user='avnadmin',
        host='pg-2f37e134-empire1266.f.aivencloud.com',
        password='AVNS_GEfpyamT7kd4de4fIwU',
        port='19276'
    )
