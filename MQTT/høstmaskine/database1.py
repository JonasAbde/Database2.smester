import psycopg2


def insert(key,value):
	conn = psycopg2.connect(host="localhost",dbname="environment",user="postgres",password="postgres")
	cur = conn.cursor()
	print("insert into measurements(textkey,measurement,registereded_time) values('%s','%s',now());" %(key,value))
	cur.execute("insert into measurements(textkey,measurement,registereded_time) values('%s','%s',now());" %(key,value))
	conn.commit()
	cur.close()
	conn.close()
