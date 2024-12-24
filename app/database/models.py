from datetime import datetime
import sqlite3
import json

class Design:
    def __init__(self, db_path='design.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS designs
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             prompt TEXT NOT NULL,
             image_url TEXT NOT NULL,
             status TEXT NOT NULL DEFAULT 'generated',
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        ''')
        conn.commit()
        conn.close()

    def create_design(self, prompt, image_url):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            INSERT INTO designs (prompt, image_url)
            VALUES (?, ?)
        ''', (prompt, image_url))
        design_id = c.lastrowid
        conn.commit()
        conn.close()
        return design_id

    def get_design(self, design_id):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM designs WHERE id = ?', (design_id,))
        design = c.fetchone()
        conn.close()
        return design