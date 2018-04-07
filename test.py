class hx:
    scale = 0
    def __init__(self, r,c):
        self.scale = r*c

sensor = hx(10,10)
print(sensor)