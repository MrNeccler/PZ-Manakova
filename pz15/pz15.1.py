import sqlite3
from datetime import datetime

class InsuranceDB:
    def __init__(self, db_name='insurance.db'):
        """Инициализация базы данных"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
        
    def _create_tables(self):
        """Создание таблицы Договор"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Договор (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            дата_заключения TEXT NOT NULL,
            страховая_сумма REAL NOT NULL,
            вид_страхования TEXT NOT NULL,
            тарифная_ставка REAL NOT NULL,
            филиал TEXT NOT NULL
        )
        ''')
        self.conn.commit()
    
    def add_contract(self, date, sum, insurance_type, rate, branch):
        """Добавление нового договора"""
        self.cursor.execute('''
        INSERT INTO Договор (дата_заключения, страховая_сумма, вид_страхования, тарифная_ставка, филиал)
        VALUES (?, ?, ?, ?, ?)
        ''', (date, sum, insurance_type, rate, branch))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_contracts(self):
        """Получение всех договоров"""
        self.cursor.execute('SELECT * FROM Договор')
        return self.cursor.fetchall()
    
    def get_contracts_by_branch(self, branch):
        """Получение договоров по филиалу"""
        self.cursor.execute('SELECT * FROM Договор WHERE филиал = ?', (branch,))
        return self.cursor.fetchall()
    
    def get_total_sum_by_type(self, insurance_type):
        """Получение общей страховой суммы по виду страхования"""
        self.cursor.execute('SELECT SUM(страховая_сумма) FROM Договор WHERE вид_страхования = ?', (insurance_type,))
        return self.cursor.fetchone()[0]
    
    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()

# Пример использования
if __name__ == '__main__':
    db = InsuranceDB()
    
    # Добавление тестовых данных
    db.add_contract('2023-01-15', 500000, 'Автострахование', 2.5, 'Центральный')
    db.add_contract('2023-02-20', 1000000, 'Жизнь', 1.8, 'Северный')
    db.add_contract('2023-03-10', 750000, 'Имущество', 3.2, 'Центральный')
    
    # Получение всех договоров
    print("Все договоры:")
    for contract in db.get_all_contracts():
        print(contract)
    
    # Получение договоров по филиалу
    print("\nДоговоры Центрального филиала:")
    for contract in db.get_contracts_by_branch('Центральный'):
        print(contract)
    
    # Получение общей страховой суммы по виду страхования
    total = db.get_total_sum_by_type('Автострахование')
    print(f"\nОбщая страховая сумма по автострахованию: {total} руб.")
    
    db.close()
