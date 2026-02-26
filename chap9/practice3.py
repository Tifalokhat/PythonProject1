class Instrument():
    def make_sound(self):
        pass
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')
class Piano(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在弹奏')

def play(obj):
    obj.make_sound()

er=Erhu()
piano=Piano()
vio=Violin()

play(er)
play(piano)
play(vio)

