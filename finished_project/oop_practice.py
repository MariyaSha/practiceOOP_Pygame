import pygame
import random
import os

# optional: place pygame window at fixed location
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

# parent class
class Vehicle:
    def __init__(self, colour="red", x=400, y=400):
        # parent attributes
        self.img_path = "sedan_" + colour + ".png"
        self.location = x, y
        self.draw()
    
    def draw(self):
        # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location

# child class of vehicle
class Truck(Vehicle):
    def __init__(self, x, y, kind="truck_tractor"):
        # initialize parent
        super().__init__()
        # override parent attributes
        self.img_path = kind + ".png"
        self.location = x, y
        # call inherited method
        self.draw()

# child class of vehicle
class Police(Vehicle):
    def __init__(self, x, y):
        # initialize parent
        super().__init__()
        # override parent attributes
        self.img_path = "police_car.png"
        self.location = x, y
        # call inherited method
        self.draw()

# pygame settings
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

# list to store car objects
cars = []

# generate 10 car objects
for i in range(10):
    # location settings
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    # choose a class of vehicles
    vehicle_class = random.choice(["sedan", "truck", "police"])
    
    # if the chosen class is sedan
    if vehicle_class == "sedan":
        # choose a random colour and store a sedan object in cars
        c = random.choice(["red", "green", "blue"])
        cars.append(Vehicle(c, x, y))
    # if the chosen class is truck
    elif vehicle_class == "truck":
        # choose a random kind and store a truck object in cars
        k = random.choice(["truck_tractor", "box_truck"])
        cars.append(Truck(x, y, k))
    # if the chosen class is a police vehicle
    elif vehicle_class == "police":
        # store a police vehicle in cars
        cars.append(Police(x, y))

# set background colour  
screen.fill("white")
# place image on the screen
for car in cars:
    screen.blit(car.img, car.img_location)

# start game loop
while running:
    # if we click on the "exit" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

