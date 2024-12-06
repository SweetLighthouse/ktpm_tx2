import util
import os
import time

def test_word_management_screen():
    util.focus_window()

    # Sang tab từ vựng cá nhân
    util.click(os.path.join('image', 'word_management_screen', 'to_work_management_button.png'))

    # Click từ đầu tiên
    util.click(os.path.join('image', 'word_management_screen', 'to_work_management_button.png'), 0, 40)

    # Click nghe
    util.click(os.path.join('image', 'word_management_screen', 'read_button.png'))
    time.sleep(3)

    # Click xoá
    util.click(os.path.join('image', 'word_management_screen', 'delete_button.png'))
    util.click(os.path.join('image', 'word_management_screen', 'ok_button.png'))

    # # Click nhắc nhở học từ vựng
    # util.click(os.path.join('image', 'word_management_screen', 'notification_button.png'))

    # # Bấm nhầm, hủy
    # util.click(os.path.join('image', 'word_management_screen', 'cancel_button.png'))
    return
