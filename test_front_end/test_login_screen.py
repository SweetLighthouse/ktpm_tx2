import util
import os

def login(username_text, password_text):
    # giả sử app đã bật
    # bước 0: tìm window trên taskbar, focus window.
    util.focus_window()

    # chụp ảnh
    util.screenshot('login screen')

    # bước 1: nhâp vào username
    util.type_in(os.path.join('image', 'login_screen', 'username_label.png'), username_text, 0, 50)

    # Bước 2: Nhập vào password
    util.type_in(os.path.join('image', 'login_screen', 'password_label.png'), password_text, 0, 50)

    # Bước 3: Bấm nút đăng nhập
    util.click(os.path.join('image', 'login_screen', 'login_button.png'))


    # Bước 4: Bấm nút OK
    util.click(os.path.join('image', 'login_screen', 'ok_button.png'))