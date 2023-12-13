import os

class hosters:
    def __init__(self):
        self.cwd = os.getcwd()

    def getModelDir(self):
        dir = os.path.join(self.cwd, "model")
        os.makedirs(dir, exist_ok=True)
        return dir

    def getDumpDir(self):
        dir = os.path.join(self.cwd, "dump")
        os.makedirs(dir, exist_ok=True)
        return dir

    def getReportDir(self):
        dir = os.path.join(self.cwd, "report")
        os.makedirs(dir, exist_ok=True)
        return dir
