class a:
    def __init__(self):
        pass
    def b(self):
        print('dsfas')
    def c(self):
        self.b()
        print('3412')

if __name__ == '__main__':
    aa = a()
    #aa.b()
    aa.c()