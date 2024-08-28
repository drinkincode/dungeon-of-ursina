from stats.baseStat import BaseStat
class BaseStatHandler():
    def __init__(self, statsList, bar_x=1.20, bar_y=-0.25):
        self.stats = []
        self.stats_dict = {}
        for stat in statsList:
            self.stats_dict[stat[0]] = BaseStat(
                name=stat[0], 
                statMax=stat[1], 
                color=stat[2], 
                position=(bar_x, bar_y),
                visible=stat[3]
            )
            bar_y += 0.05

    def print_stats(self):
        print('Stats -')
        for i in range(len(self.stats)):
            self.stats[i].print_stat()
            
    def add_stat(self, name, statValue):
        newStat = BaseStat(name, statValue)
        self.stats.append(newStat)
        return True