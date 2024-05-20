from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pyodbc
from tkinter import messagebox
import subprocess
import Conn
import sys
import os


OUTPUT_PATH = Path(__file__).parent

def get_assets_path():
    # รับเส้นทางที่โปรแกรม exe อยู่
    exe_path = os.path.dirname(sys.argv[0])
    # ระบุเส้นทางสำหรับโฟลเดอร์ assets/frame0
    assets_path = os.path.join(exe_path, 'assets', 'frame0')
    return assets_path

# เรียกใช้ฟังก์ชันเพื่อรับเส้นทางของโฟลเดอร์ assets
ASSETS_PATH = get_assets_path()
print("เส้นทางสำหรับโฟลเดอร์ของรูปภาพ:", ASSETS_PATH)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Users:    
    def __init__(self, window):
        self.logged_in_username = ""
        self.window = window

    def getusername(self):
        if self.logged_in_username == "":
            sys.exit()
        return self.logged_in_username



class Login:
    # ฟังชั่นสำหรับการ Login 
    
    def login():
        # ใช้ connection string จริงของฐานข้อมูล
        connection_string = Conn.connection_string
        username = UserName.get()  # ดึง username จาก entry_UserName
        password = PassWord.get()  # ดึง password จาก entry_Password
        global logged_in_username
        cursor = None  # กำหนด cursor เป็น None ก่อนที่บล็อก try
    
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            # ปรับ query ให้ตรงกับโครงสร้างของฐานข้อมูล
            query = "SELECT * FROM Login WHERE Username = ? AND Password = ?"
            cursor.execute(query, (username, password))

            if cursor.fetchone():
                print("Login Successful")
                logged_in_username = username  # เก็บชื่อผู้ใช้ที่ทำการล็อกอิน
                user.logged_in_username = username  # เก็บชื่อผู้ใช้ที่ทำการล็อกอินในคลาส Users
                window.destroy()  # ปิดหน้าต่างหลังจากล็อกอินสำเร็จ
                
            else:
                print("Login Failed")
                messagebox.showinfo("Login Failed", "Login Failed!!")

        except pyodbc.Error as e:
            print(f"Database Error: {e}")
            # จัดการข้อผิดพลาดของฐานข้อมูล
        except Exception as e:
            print(f"Unexpected Error: {e}")
            # จัดการข้อผิดพลาดที่ไม่คาดคิด

    def Password_on_entry_click(event):
        if PassWord.get() == "enter your password":
            PassWord.delete(0, "end")  # ลบข้อความเริ่มต้นเมื่อได้รับโฟกัส

    def Password_on_focus_out(event):
        if not PassWord.get() or PassWord.select_present():
            PassWord.insert(0, "enter your password")  # เพิ่มข้อความ "Password" เมื่อลงจาก Entry โดยไม่มีข้อความ
            PassWord.config(font=("Inter", 14), fg="#C6C6C6")

    def UserName_on_entry_click(event):
        if UserName.get() == "email account or username":
            UserName.delete(0, "end")

    def UserName_on_focus_out(event):
        if not UserName.get() or UserName.select_present():
            UserName.insert(0, "email account or username")
            UserName.config(font=("Inter", 14), fg="#C6C6C6")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()
# สร้างอินสแตนซ์ของคลาส Users
user = Users(window)



window.geometry("1200x680")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    861.0,
    219.0,
    image=image_image_1
)

canvas.create_text(
    675.0,
    256.0,
    anchor="nw",
    text="this tool helps you manage our company's internal forms \nsuch as quotations, purchase orders, invoices, etc.",
    fill="#555555",
    font=("Inter", 14 * -1)
)
#ส่วนของ Username
UserNameimage = PhotoImage(
    file=relative_to_assets("UserName.png"))
UserNameimage_bg_1 = canvas.create_image(
    874.0,
    383.0,
    image=UserNameimage
)
UserName = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=0
)
UserName.place(
    x=715.0,
    y=368.0,
    width=300.0,
    height=30.0
)
# เรียกใช้ฟังก์ชันเพื่อตั้งค่าเริ่มต้น
Login.UserName_on_focus_out(None)  # ส่งพารามิเตอร์ event ในกรณีนี้เป็น None
# กำหนดเหตุการณ์เมื่อได้รับโฟกัสและเมื่อลงจาก Entry
UserName.bind("<FocusIn>", Login.UserName_on_entry_click)
UserName.bind("<FocusOut>", Login.UserName_on_focus_out)


#ส่วนขง Password 
PassWord_image = PhotoImage(
    file=relative_to_assets("PassWord.png"))
PassWord_image_bg = canvas.create_image(
    874.0,
    437.0,
    image=PassWord_image
)
PassWord = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=0
)
PassWord.place(
    x=715.0,
    y=420.0,
    width=300.0,
    height=30.0
)

# เรียกใช้ฟังก์ชันเพื่อตั้งค่าเริ่มต้น
Login.Password_on_focus_out(None)  # ส่งพารามิเตอร์ event ในกรณีนี้เป็น None
# กำหนดเหตุการณ์เมื่อได้รับโฟกัสและเมื่อลงจาก Entry
PassWord.bind("<FocusIn>", Login.Password_on_entry_click)
PassWord.bind("<FocusOut>", Login.Password_on_focus_out)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    697.0,
    383.0,
    image=image_image_2
)

Login_image = PhotoImage(file=relative_to_assets("Login.png"))

# สร้างปุ่มโดยใช้รูปภาพและคำสั่งที่ต้องการเรียกเมื่อคลิกปุ่ม
button_login = Button(
    window,
    image=Login_image,
    command=Login.login,  # เมื่อคลิกที่ปุ่มนี้จะเรียกใช้ฟังก์ชัน login
    borderwidth=0,  # กำหนดความกว้างของเส้นขอบเป็น 0 เพื่อลบขอบเทาๆ
    highlightthickness=0,  # กำหนดความกว้างของ highlight ให้เป็น 0 เพื่อลบเส้นขอบเทาๆ
)
# กำหนดตำแหน่งของปุ่มโดยใช้เมทอด place
button_login.place(x=1000.0, y=475.0)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    696.0,
    437.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1042.0,
    437.0,
    image=image_image_5
)

canvas.create_text(
    74.0,
    104.0,
    anchor="nw",
    text="generative AI for innovative technology",
    fill="#555555",
    font=("Inter Light", 10 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    174.0,
    73.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    374.0,
    402.0,
    image=image_image_7
)
window.resizable(False, False)
window.mainloop()
