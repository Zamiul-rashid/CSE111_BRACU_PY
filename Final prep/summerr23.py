class Workspace:
    def __init__(self, workspaceName, type):
        self.workspaceName = workspaceName
        self.type = type
        self.channels = {}
    def checkChannelExistence(self, channelName):
        if channelName in self.channels:
            return True
        return False
    def __str__(self):
        return f"Name: {self.workspaceName}\nType:{self.type}\n"
