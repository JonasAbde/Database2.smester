import psycopg2

def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_GEfpyamT7kd4de4fIwU@pg-2f37e134-empire1266.f.aivencloud.com:19276/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()