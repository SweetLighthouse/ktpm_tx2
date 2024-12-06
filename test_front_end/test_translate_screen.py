import util
import os
import time

def test_translate_screen(word_to_translate):
    util.focus_window()
    # Nhập từ vào ô English
    util.type_in(os.path.join('image', 'translate_screen', 'input_label.png'), word_to_translate, 0, 50)

    # Dịch
    util.click(os.path.join('image', 'translate_screen', 'translate_button.png'))
    time.sleep(2)

    # Nghe
    util.click(os.path.join('image', 'translate_screen', 'read_word_button.png'))
    time.sleep(5)

    # Lưu từ
    util.click(os.path.join('image', 'translate_screen', 'save_button.png'))
    util.click(os.path.join('image', 'translate_screen', 'ok_button.png'))

    # chụp ảnh
    util.screenshot('tranlate screen ' + word_to_translate)
    return
