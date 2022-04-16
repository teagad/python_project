import time
import pickle


class tamagochi:
    def __init__(self):
        self.hunger = 100
        self.happines = 100
        self.time = 0
        self.date = 0

    def getinfo(self,profile, tamagochi):
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
                print(dic)
                self.date = self.coverter(dic[(profile,tamagochi)][0].split()[3])
                self.hunger = int(dic[(profile,tamagochi)][1])
                self.happines = int(dic[(profile,tamagochi)][2])
        except Exception:
            self.date = self.coverter(time.ctime().split()[3])
            self.hunger = int(20)
            self.happines = int(20)

    def setinfo(self,profile, tamagochi, hunger=None, happines=None):
        if hunger == None:
            hunger = self.hunger
            happines = self.happines
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
            dic[(profile,tamagochi)] = [str(time.ctime()), str(hunger), str(happines)]
            with open('data.pickle', 'wb') as f:
                pickle.dump(dic, f)
        except Exception:
            dic = {}
            dic[(profile,tamagochi)] = [str(time.ctime()), str(hunger), str(happines)]
            with open('data.pickle', 'wb') as f:
                pickle.dump(dic, f)

    def coverter(self, time2):
        tim = [*map(int, time2.split(':'))]
        return tim[0] * 3600 + tim[1] * 60 + tim[2]
