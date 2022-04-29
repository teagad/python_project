import time
import pickle
from src.globals import Globals


class Tamagochi:
    def __init__(self):
        self.hunger = 100
        self.happines = 100
        self.time = 0
        self.date = 0
        self.date_of_birth = 0

    def getinfo(self, profile, tamagochi):
        """ считавания данных с прошлого запуска """
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
                profile_data = dic[(profile, tamagochi)]
                self.date = self.coverter(profile_data[0].split()[3])
                self.hunger = int(profile_data[1])
                self.happines = int(profile_data[2])
                self.date_of_birth = int(profile_data[3])
        except Exception:
            standart_stats = (20, 20)
            self.date = self.coverter(time.ctime().split()[3])
            self.date_of_birth = self.date
            self.hunger = standart_stats[0]
            self.happines = standart_stats[1]

    def setinfo(self, profile, tamagochi, hunger=None, happines=None):
        """запись данных для следующего запуска"""
        if hunger is None:
            hunger = self.hunger
            happines = self.happines
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
            dic[(profile, tamagochi)] = [
                str(time.ctime()),
                str(hunger),
                str(happines),
                str(self.date_of_birth)
            ]
            with open('data.pickle', 'wb') as f:
                pickle.dump(dic, f)
        except Exception:
            dic = {}
            dic[(profile, tamagochi)] = [
                str(time.ctime()),
                str(hunger),
                str(happines),
                str(self.date_of_birth)
            ]
            with open('data.pickle', 'wb') as f:
                pickle.dump(dic, f)

    def coverter(self, time2):
        """для перевода hh:mm:ss в s"""
        minute = 60
        hour = 3600
        tim = [*map(int, time2.split(':'))]
        return tim[0] * hour + tim[1] * minute + tim[2]

    def to_top(self):
        """Записывать время жизни в top.txt"""
        minute = 60
        with open('top.txt', 'a') as f:
            tyme_now = self.coverter(time.ctime().split()[3])
            life_time = str((tyme_now - self.date_of_birth) / minute)
            f.write(Globals.profile + " " + life_time + "\n")
            f.close()
