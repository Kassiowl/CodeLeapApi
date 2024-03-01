import sqlite3
from core.entities.content import Content
from core.interfaces.ContentInterface import ContentInterface


class ContentSqlLiteImpl(ContentInterface):
    def __init__(self, db_path='db.sqlite3'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contents (
                content_id INTEGER PRIMARY KEY,
                text TEXT
            )
        ''')
        self.conn.commit()

    def send_content(self, content: Content):
        try:
            self.cursor.execute('''
                INSERT INTO code_leap_api_contentmodel (title, author, content, creation_date)
                VALUES ( ?, ?, ?, ?)
            ''', (content.title, content.author, content.content, content.created_time))
            self.conn.commit()
            return True
        except:
            return False  
        
    def edit_content(self, content: Content, content_id):
        try:
            self.cursor.execute('''
                UPDATE code_leap_api_contentmodel
                SET title = ?, content = ?
                WHERE id = ?
            ''', (content.title, content.content, content_id))
            self.conn.commit()
            return True
        except Exception as e:
            return False
    def delete_content(self, content_id):
        try:
            self.cursor.execute('''
                DELETE FROM code_leap_api_contentmodel
                WHERE id = ?
            ''', (content_id,))
            self.conn.commit()
            return True
        except:
            return False

    def get_content(self, content_id):
        try:
            self.cursor.execute('''
                SELECT * FROM code_leap_api_contentmodel
                WHERE id = ?
            ''', (content_id,))
            row = self.cursor.fetchone()
            if row:
                return Content(row[1], row[2], row[3], row[4])
            else:
                return None
        except:
            return None

    def __del__(self):
        self.conn.close()
