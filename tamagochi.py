import time


class tamagochi:
    def __init__(self):
        self.hunger = 100
        self.happines = 100
        self.time = 0
        self.date = 0

    def getinfo(self):
        with open('data.txt') as f:
            lines = f.readlines()
        self.date = self.coverter(lines[0].split()[3])
        self.hunger = int(lines[1][:-1])
        self.happines = int(lines[2])
        f.close()

    def setinfo(self, hunger=None, happines=None):
        if not hunger and not happines:
            hunger = self.hunger
            happines = self.happines
        with open('data.txt', 'w') as f:
            f.write(str(time.ctime()) + '\n')
            f.write(str(hunger) + '\n')
            f.write(str(happines))
        f.close()

    def coverter(self, time2):
        tim = [*map(int, time2.split(':'))]
        return tim[0] * 3600 + tim[1] * 60 + tim[2]
