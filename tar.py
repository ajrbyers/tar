import db
import tweepy

def setup():
	conn = db.connection()
	db.create_table(conn)