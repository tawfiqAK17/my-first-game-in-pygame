from trick import Trick
class Settings():
    def __init__(self, screen):
            # defaults values
            self.fps = 60
            self.in_menu = True
            self.ball_size = 25
            self.tricks = [
                  Trick('ball speed x5', 20, screen, True),
                  Trick('increase your length', 25, screen),
                  Trick( 'decrease your enemy length', 30,  screen,),
                  Trick( 'add more space to your inventory', 25, screen,),
                  Trick('reverse the ball direction', 10, screen),
                  Trick('reverse your enemy controle', 30, screen),
                  Trick('reset your default values', 25, screen)
                  ]
            
