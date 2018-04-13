import os



def init_position():
    set_position(118.910032 , 31.900955)

def set_position(x,y):
    # os.system('adb emu geo fix ' + str(x) + ' ' + str(y))
    os.system('adb -s 988995454730455437 emu geo fix 118.910032 31.900955')
    # os.system('adb geo fix 118.910032 31.900955')



init_position()
