mport sqlite3 as sq

info_users = [
    (12, 'Lenovo', 'Мастерская «Синий Экран Смерти»', 2900.0, '05-05-2026 11:40', 'ВИРУС-ИЗ-ДЕВЯНОСТЫХ', 10, 14200.0),
    (13, 'Lenovo', 'АО «Канифоль и Слёзы»', 4350.0, '17-05-2026 09:15', 'ОТВАЛ-ЧИПА-2026', 10, 28900.0),
    (14, 'Lenovo', 'ООО «Термопаста Высохла»', 1650.0, '22-05-2026 16:05', 'КУЛЕР-ИЗДЫХАЕТ', 10, 8100.0),
    (15, 'Lenovo', 'Артель «Забытый Болтик»', 3100.0, '11-05-2026 13:25', 'КОРПУС-НА-СОПЛЯХ', 10, 19500.0),
   (16, 'Lenovo', 'НИИ «Кабель на Изоленте»', 2250.0, '26-05-2026 10:50', 'ЗАРЯДКА-ПОД-УГЛОМ', 10, 12600.0),
    (17, 'Lenovo', 'Кооператив «Скрутка и Скотч»', 3950.0, '07-05-2026 17:35', 'ПЕТЛИ-ХРУСТНУЛИ', 10, 24800.0),
    (18, 'Lenovo', 'Завод Одноразовой Пайки №4', 4950.0, '29-05-2026 15:20', 'ДЫМ-ПОШЕЛ-УРА', 10, 33300.0),
    (19, 'Lenovo', 'Фабрика Электро-Шока', 1300.0, '15-05-2026 12:10', 'БАТАРЕЯ-ВЗДУЛАСЬ', 10, 6500.0),
   (21, 'Lenovo', 'Центр «Залито Кофеем»', 3600.0, '24-05-2026 18:55', 'КЛАВА-БОЛЬШЕ-НЕ-ПЕШЕТ', 10, 21000.0)
]



con = sq.connect('telemaster.db')
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS tv_remont (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mark TEXT NOT NULL, 
    zavod TEXT NOT NULL,
    price REAL NOT NULL,
    remont_date TEXT NOT NULL,
    document TEXT NOT NULL,
    master_id INTEGER NOT NULL,
    total_price REAL NOT NULL
)""")

cur.executemany("INSERT INTO tv_remont VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_users)

con.commit()

cur.execute("SELECT * FROM tv_remont")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\n" * 3)


cur.execute("SELECT * FROM tv_remont where price BETWEEN 1000 AND 2000")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\n" * 3)

cur.execute("SELECT order_id, remont_date FROM tv_remont ORDER BY order_id DESC")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\n" * 3)

cur.execute("SELECT zavod FROM tv_remont where price < 3000")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("UPDATE tv_remont SET total_price = total_price + 1000 WHERE total_price < 14000")
cur.execute("UPDATE tv_remont SET price = price + 1000 WHERE price < 4000")
cur.execute("UPDATE tv_remont SET price = price - 100 WHERE price >= 4000")

cur.execute("DELETE FROM tv_remont WHERE price < 2000")
cur.execute("DELETE FROM tv_remont WHERE total_price < 10000")
cur.execute("DELETE FROM tv_remont WHERE total_price < 16000")

cur.execute("SELECT * FROM tv_remont")
rows = cur.fetchall()
for row in rows:
    print(row)


con.close()
