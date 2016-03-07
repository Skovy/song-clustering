import psycopg2

class Database:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect()
        self.create_table()

    def connect(self):
        try:
            self.conn = psycopg2.connect("dbname='spotifyechonest' user='owner' host='localhost' password='h4ck3r'")
            self.cur = self.conn.cursor()
        except:
            print "Unable to connect to the database."



    def close():
        self.cur.close()
        self.conn.close()
