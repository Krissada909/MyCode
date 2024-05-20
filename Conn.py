import pyodbc

# รูปแบบของ connection string สำหรับ SQL Server
server = 'N2N-DEV2023\SQLEXPRESS2019'
#N2N-DEV2023\SQLEXPRESS2019
database = 'Basic'
username = 'sa'
password = 'sa'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# เชื่อมต่อกับฐานข้อมูล SQL Server
connection = pyodbc.connect(connection_string)

# ตรวจสอบว่าการเชื่อมต่อสำเร็จหรือไม่
if connection:
    print("เชื่อมต่อกับฐานข้อมูลสำเร็จ.")
else:
    print("ล้มเหลวในการเชื่อมต่อกับฐานข้อมูล.")

# ปิดการเชื่อมต่อเมื่อเสร็จสิ้น
connection.close()
