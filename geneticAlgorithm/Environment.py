import constants as c

class ENVIRONMENT:

    def __init__(self,id):
        self.ID = id
        self.l = c.L
        self.w = c.L
        self.h = c.L
        if (self.ID == 0):
            self.Place_Light_Source_To_The_Front()
        elif (self.ID == 1):
            self.Place_Light_Source_To_The_Right()
        elif (self.ID == 2):
            self.Place_Light_Source_To_The_Back()
        else:
            self.Place_Light_Source_To_The_Left()

    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = 30*c.L
        self.z = c.L/2

    def Place_Light_Source_To_The_Right(self):
        self.x = 30*c.L
        self.y = 0
        self.z = c.L/2

    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = -30*c.L
        self.z = c.L/2

    def Place_Light_Source_To_The_Left(self):
        self.x = -30*c.L
        self.y = 0
        self.z = c.L/2

    def Send_To(self, sim):
        lightSource = sim.send_box(position=(self.x,self.y,self.z), sides=(self.l,self.w,self.h))
        sim.add_light_to_body(body_id=lightSource)