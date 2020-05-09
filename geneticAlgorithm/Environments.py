from Environment import ENVIRONMENT
import constants as c

class ENVIRONMENTS:

    def __init__(self):
        self.envs = {}
        for e in range(c.numEvns):
            self.envs[e] = ENVIRONMENT(e)