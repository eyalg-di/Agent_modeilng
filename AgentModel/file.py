from scanner import Scanner


class File:
    def __init__(self, filePath) -> None:
        self.path = filePath

    def create(self):
        self.path

    def delete(self, filePath):
        pass

    def write(self):
        pass

    def read():
        pass

    def move(self):
        pass

    def quarantine(self):
        pass

    def scan(self):
        fileScanner = Scanner(self)
        result = fileScanner.scan()
        return result
