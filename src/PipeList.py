from src.Utils import Pipe

class PipeList():

    def __init__(self):
        self.list = [Pipe()]
        self.count = 0

    def add_pipe(self):
        self.list.append(Pipe())

    def reset_pos(self):
        self.__init__()

    def move(self):
        for elem in self.list:
            elem.move()