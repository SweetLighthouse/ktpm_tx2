import util
import os

def test_logout_screen():

    # chụp ảnh
    util.screenshot('logout screen')

    util.click(os.path.join('image', 'logout_screen', 'account_button.png'))
    util.click(os.path.join('image', 'logout_screen', 'logout_button.png'), 0, 10)
    return