class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        if not hasattr(self,'hp'):
            self.hp = 0
        if not hasattr(self,'ap'):
            self.ap = 0
        self.speed = 2
        self.isalive = True
    
    def damage(self,ap):
        self.hp = self.hp - ap
        if self.hp < 0:
            self.isalive = False
    
    def attack(self,other):
        other.hp = other.hp - self.ap
        if other.hp < 0:
            other.isalive = False
    
    def move(self, dt, direction):
        if direction == 'L':
            self.dx = -1
        if direction == 'R':
            self.dx = 1
        if direction == 'U':
            self.dy = -1
        if direction == 'D':
            self.dy = 1
        self.y += self.speed * dt * self.dy
        self.x += self.speed * dt * self.dx
    
    def set_speed(self, speed):
        self.speed = speed    

class Player(Entity):
    def __init__(self, x, y, hp, ap):
        self.hp = hp
        self.ap = ap
        
        super().__init__(x, y)
   

class Enemy(Entity):
    def __init__(self, x, y, hp, ap):
        self.hp = hp
        self.ap = ap
        super().__init__(x, y)
        


