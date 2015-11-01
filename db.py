import sqlite3, settings

def connection():
	conn = sqlite3.connect(settings.DB_PATH)
	return conn

def create_table(conn):
	sql = '''
	CREATE TABLE `tweets` (
		`id`    INTEGER PRIMARY KEY AUTOINCREMENT,
		`tweet_id`  TEXT,
		`replied`   INTEGER
	);
	'''
	cur = conn.cursor()    
	cur.execute(sql)

def insert_tweet(conn, tweet_id, replied=0):
	sql = '''
	INSERT INTO tweets (tweet_id, replied) VALUES("%s", %s)
	''' % (tweet_id, replied)

	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()

def update_tweet_replied(conn, pk, replied=1):
	sql = '''
	UPDATE tweets SET replied = %s WHERE id = %s
	''' % (replied, pk)

	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()

