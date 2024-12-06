import random
import string

username_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
password_text = "@12#$%65"

def main():
    # đăng ký
    import test_register_screen
    test_register_screen.register(username_text, password_text)
    print("register success.")


    # đăng nhập
    import test_login_screen
    test_login_screen.login(username_text, password_text)
    print("login success.")

    # thao tác trên màn hình dịch
    import test_translate_screen
    test_translate_screen.test_translate_screen("economy")
    test_translate_screen.test_translate_screen("follow")
    test_translate_screen.test_translate_screen("friend")
    print("translate word success.")


    # xem từ vựng
    import test_word_management_screen
    test_word_management_screen.test_word_management_screen()
    print("word management success.")


    # chơi
    import test_play_screen
    test_play_screen.test_play_screen(["đi theo sau, tiếp theo", "người bạn"])
    print("play success.")


    # đăng xuất
    import test_logout_screen
    test_logout_screen.test_logout_screen()
    print("logout success.")

if __name__ == "__main__":
    main()