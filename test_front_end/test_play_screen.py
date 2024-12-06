import util
import os
import time

def test_play_screen(word_list):


    util.focus_window()

    # Sang tab chơi
    util.click(os.path.join('image', 'play_screen', 'to_play_screen_button.png'))

    # chụp ảnh
    util.screenshot('play screen')

    # Click bắt đầu
    util.click(os.path.join('image', 'play_screen', 'start_button.png'))

    # Nhập từ vựng
    for i in range(len(word_list) * 2):
        util.type_in(os.path.join('image', 'play_screen', 'check_button.png'), word_list[i % len(word_list)], 0, -40)
        util.click(os.path.join('image', 'play_screen', 'check_button.png'))
        time.sleep(1)
        util.screenshot('word ' + str(i))

    return

