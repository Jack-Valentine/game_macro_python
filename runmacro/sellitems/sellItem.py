import runmacro.common.mouseclick as MouseClick
import time

class SellItems:
    def __init__(self):
        self.mouse_position = [
            [-484, 572],
            [- 530, 1495],
            [- 201, 1487],
            [- 735, 1240],
            [- 735, 1240],
            [- 117, 573],
        ]
    def sell_item(self):
        mouse_positions = self.mouse_position
        for position in mouse_positions:
            MouseClick.MouseClick(position[0], position[1]).mouse_click()
            time.sleep(4)


cal1 = SellItems()
cal1.sell_item()
