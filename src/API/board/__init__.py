from flask import Flask
import pages
import sys

sys.path.insert(1, "/home/pi/Frencherani/src/API/GameEngine")

import main # frencherani game engine


HOST_ADDRESS, HOST_PORT = "0.0.0.0", 8000

class FrencheraniApp:
    def __init__(self):
        self.pages = pages

        self.Game = main.Game()

    def getServer(self):
        self.server = Flask(__name__)
        self.server.register_blueprint(self.pages.blueprint)

        return self.server