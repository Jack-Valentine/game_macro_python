import runmacro.common.mouseclick as MouseClick
import time

class ScrollQuest:
    def __init__(self):
        self.mouse_position = [
            [-1745, 979],
            [- 1288, 852],
            [- 689, 1399],
            [- 794, 1265],
            [- 738, 1396],
            [- 1195, 1273]
        ]
        self.succesc_position = [-956, 1403]
        self.quest_count = 6
        self.current_count = 0

    def scroll_quest(self):
        mouse_positions = self.mouse_position
        succesc_position = self.succesc_position

        for position in mouse_positions:
            MouseClick.MouseClick(position[0], position[1]).mouse_click()
            time.sleep(4)

        for i in range(0, 150):
            MouseClick.MouseClick(succesc_position[0], succesc_position[1]).mouse_click()
            time.sleep(3)
        print ('Success Scroll Quest')
        MouseClick.MouseClick(succesc_position[0], succesc_position[1]).mouse_click()
        self.current_count += 1
        if self.current_count < self.quest_count:
            self.scroll_quest()


cal1 = ScrollQuest()
cal1.scroll_quest()
