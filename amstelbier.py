import Tkinter
import random
import math

random.seed(0)

perceel = []

window = Tkinter.Tk()

houses = []


window.title("Houses")

window.geometry("750x800")

# size of the map
widthmap = 600
heightmap = 640

# size of the small house
height1 = 32
width1 = 32
free1 = 8
color1 = "yellow"

#size of the bungalow
height2 = 30
width2 = 40
free2 = 12
color2 = "purple"

# size of the maison
height3 = 44
width3 = 42
free3 = 24
color3 = "red"

Canvas = Tkinter.Canvas(window, width = 600, height = 640)

class position:
    def __init__(self):
        self.random()
        # self.x2 = self.x1 + self.width
        # self.y2 = self.y2 + self.height


    def random(self):
        self.x1 = random.randint(0, widthmap)
        self.y1 = random.randint(0, heightmap)
        

        return self.x1, self.y1

class House:
    def __init__ (self, width, height, free, pos, color, name, value, growth):
        self.pos = pos
        self.width = width
        self.height = height
        self.free = free
        self.color = color
        self.name = name
        #self.mindistance = mindistance
        self.value = value
        self.growth = growth
        
        

    def getY1(self):
        return self.pos.y1

    def getY2(self):
        return self.pos.y1 + self.height

    def getX1(self):
        return self.pos.x1

    def getX2(self):
        return self.pos.x1 + self.width       

    def createHouse(self):
        Canvas.create_rectangle(self.pos.x1 - self.free,\
            self.pos.y1 - self.free, self.pos.x1 + self.width + self.free, self.pos.y1 + self.height + self.free, fill=self.color, stipple="gray12")
        Canvas.create_rectangle(self.pos.x1, self.pos.y1, self.pos.x1 + self.width, self.pos.y1 + self.height, fill=self.color)
        Canvas.create_text(self.pos.x1, self.pos.y1, font="Purisa", text= self.name)
        

    def overlapCheck(self, houses):
        
        for house in houses:
   
            if (house.pos.x1 + self.width + self.free) > self.pos.x1 > (house.pos.x1 - self.width - self.free)\
                and (house.pos.y1 + self.height + self.free) > self.pos.y1 > (house.pos.y1 - self.height - self.free):            
             
                return True
            
        return False
            
    
    def distance(self, houses):
        
        distances = []
                
        for house in houses:
            
            
            #checks if created house is on the horizontal space of the existing house
            if self.pos.y1 <= house.pos.y1 <= (self.pos.y1 + self.height) or\
                self.pos.y1 <= house.pos.y1 + house.height <= (self.pos.y1 + self.height) :
                
                if(house.pos.x1 < self.pos.x1): 
                    distance = abs(self.pos.x1 - (house.pos.x1 + house.width))
                    distances.append(distance)
                    # print "left: " + str(distance)
                elif (self.pos.x1 + self.width) < house.pos.x1:
                    distance = abs(house.pos.x1 - (self.pos.x1 + self.width))    
                    distances.append(distance)
                    # print "right: " +  str(distance)
            
            # checks if created house is on the vertical space of the existing house
            if self.pos.x1 <= house.pos.x1 <= (self.pos.x1 + self.width) or \
               self.pos.x1 <= (house.pos.x1 + house.width) <= (self.pos.x1 + self.width):

                if(house.pos.y1 + house.height) < self.pos.y1:
                    distance = abs(self.pos.y1 -(house.pos.y1 + house.height))
                    distances.append(distance)
                    # print "top: " + str(distance)
                elif house.pos.y1 > (self.pos.y1 + self.height):
                    distance = abs(house.pos.y1 - (self.pos.y1 + self.height))
                    distances.append(distance)
                    # print "below: " + str(distance)
              
            # schuine afstand boven        
            if (house.pos.y1 + house.height) < self.pos.y1:
                if house.pos.x1 > (self.pos.x1 + self.width):
                    distance = math.sqrt((house.pos.x1 - (self.pos.x1 + self.width))**2 + (self.pos.y1 - (house.pos.y1 + house.height))**2)
                    distances.append(distance)
                    # print "righttop: " + str(distance)
                elif (house.pos.x1 + house.width) < self.pos.x1:
                    distance = math.sqrt((self.pos.x1 - (house.pos.x1 + house.width))**2 + (self.pos.y1 - (house.pos.y1 + house.height))**2)
                    distances.append(distance)
                    # print "lefttop: " + str(distance)
             
           # schuine afstand beneden        
            if (self.pos.y1 + self.height) < house.pos.y1:
                #rechtsonder
                if house.pos.x1 > (self.pos.x1 + self.width):
                    distance = math.sqrt((house.pos.x1 - (self.pos.x1 + self.width))**2 + (self.pos.y1 - (house.pos.y1 + house.height))**2)
                    distances.append(distance)
                    # print "rightunder: " + str(distance)
                elif (house.pos.x1 + house.width) < self.pos.x1:
                    distance = math.sqrt((self.pos.x1 - (house.pos.x1 + house.width))**2 + (self.pos.y1 - (house.pos.y1 + house.height))**2)
                    distances.append(distance)
                    # print "leftunder: " + str(distance)
                    
             #borderleft
        distanceLeft = self.pos.x1
        distanceRight = 600 - (self.pos.x1 + self.width)
        distanceTop = self.pos.y1
        distanceBottom = 640 - (self.pos.y1 + self.height)
        
        # print "BL: " + str(distanceLeft)
        # print "BR: " + str(distanceRight)
        # print "BT: " + str(distanceTop)
        # print "BB: " + str(distanceBottom)
              
        distances.append(distanceLeft)
        distances.append(distanceRight)
        distances.append(distanceTop)
        distances.append(distanceBottom)            

        min(distances)            
        return min(distances)
        #self.mindistance = min(distances)    
        
       
              
    def getValue(self, houses):
        return self.value + self.value * (self.growth * ((self.distance(houses) - self.free)*0.25)) 
        
        #print self.extraValue
        #self.extraValue = extraValue                          
           
            

    def boarderCheck(self):

        if ((self.pos.x1 - self.free) < 0\
            or (self.pos.x1 + self.width + self.free) > widthmap\
            or (self.pos.y1 - self.free) < 0 or (self.pos.y1 + self.height + self.free) > heightmap):
            
            return True
                    
        return False 



# def getValueMap(houses):
#     totalValue = 0
#     for house in houses:
#         totalValue += House.getValue(houses)
    

            
            
def runSimulation(widthmap,heightmap):
    
    k= 0
    while len(houses) < 12:
        
        pos = position()
        
        house = House(width1, height1, free1, pos, color1, len(houses), 285000, 0.03)   
                          
        if house.overlapCheck(houses) or house.boarderCheck():
           j=1 
        
        else:
            house.createHouse()
            houses.append(house)
            #house.distance(houses)
#        
#    for house in houses:
#        print "house" + str(k)
#        house.distance(houses)    
#        k+= 1
        
    i = 0
    while len(houses) < 17:
        
        pos = position()
        
        smallHouse = House(width2, height2, free2, pos, color2, len(houses), 399000, 0.04)
        # houseloc = house.pos, house

        if smallHouse.overlapCheck(houses) or smallHouse.boarderCheck():
            j = 1
        
        else:
            smallHouse.createHouse()
            houses.append(smallHouse)
            #smallHouse.distance(houses)  
            # houseLoc.append(house.pos, house))

    while len(houses) < 20:
        
        pos = position()
        
        bigHouse = House(width3, height3, free3, pos, color3, len(houses), 610000, 0.06)
        # houseloc = house.pos, house

        if bigHouse.overlapCheck(houses) or bigHouse.boarderCheck():
            j = 1
        
        else:
            bigHouse.createHouse()
            houses.append(bigHouse)
            #bigHouse.distance(houses)  
            # houseLoc.append(house.pos, house))
                
    totalValue = 0             
    for element in houses:
        print "house" + str(i)
        #element.distance(houses)
        print element.getValue(houses)
        totalValue += element.getValue(houses)
        i += 1 

    print totalValue

   
    
runSimulation(10, 10)

y11 = 1
y22 = 1
for x in range (widthmap / 5):
    Canvas.create_line(0, y11, widthmap, y22, fill = "black")
    y11 = y11 + (widthmap / 10)
    y22 = y22 + (widthmap / 10)
    
    

x11 = 1
x22 = 1
for x in range (widthmap / 5):
    Canvas.create_line(x11, 0, x22, heightmap, fill = "black")
    x11 = x11 + (widthmap / 10)
    x22 = x22 + (widthmap / 10)

Canvas.pack()
#Canvas.after(1000, )
window.mainloop()










    
