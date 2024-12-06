import util
import os

def register(username_text, password_text):
    # Giả sử app đã bật
    # Bước 0: Tìm window trên taskbar, focus window.
    util.focus_window()

    # chụp ảnh
    util.screenshot('register screen ' + username_text)

    # Bước 1: Nhập vào username
    util.type_in(os.path.join('image', 'login_screen', 'username_label.png'), username_text, 0, 50)

    # Bước 2: Nhập vào password
    util.type_in(os.path.join('image', 'login_screen', 'password_label.png'), password_text, 0, 50)

    # Bước 3: Bấm nút đăng ký
    util.click(os.path.join('image', 'login_screen', 'register_button.png'))

    # Bước 4: Bấm nút OK
    util.click(os.path.join('image', 'login_screen', 'ok_button.png'))
