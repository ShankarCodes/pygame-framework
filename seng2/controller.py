import pygame

class EventHandler:
    def __init__(self):
        pass
    

class KeyBoardEventHandler(EventHandler):
    def __init__(self):
        self.kdhandle = dict()
        self.kuhandle = dict()
        pass
    def setkd(self, event_key, action):
        self.kdhandle[event_key] = action
    def setku(self, event_key, action):
        self.kuhandle[event_key] = action
        