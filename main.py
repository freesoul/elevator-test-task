# Design an elevator

class Elevator:
    """
    We asumme that when the elevator reaches a stop, the person leaves.
    We finish the first direction chosen, then we do the other one.
    """
    
    MAX_WEIGHT = 400
    NUM_FLOORS = 10
    
    def __init__(self):
        self.currentDirection = True # True up, False down
        self.currentFloor = 0
        self.nextFloorsUp = []
        self.nextFloorsDown = []
        self.weightsByFloor = {}
        
    def addPerson(self, weight:int, floor:int):
        if self.acumWeight() + weight > Elevator.MAX_WEIGHT:
            print("Weight exceeded. Could not add person")
            return False
        if floor in self.weightsByFloor:
            self.weightsByFloor[floor] += weight
        else:
            self.weightsByFloor[floor] = weight
        self.addDestination(floor)
        return True

    def acumWeight(self):
        weight = 0
        for k, v in self.weightsByFloor.items():
            weight += v
        return weight
    
    def addDestination(self, destination):
        """
        Returns False if destination already exists, True otherwise
        """

        if destination < 0 or destination > Elevator.NUM_FLOORS:
            return False

        if destination > self.currentFloor: # Want to go up
            idx = 0
            for i, floor in enumerate(self.nextFloorsUp):
                if destination == floor:
                    print("Destination already existing")
                    return False
                elif floor > destination:
                    idx = i # Index to insert to keep the list ordered increasingly.
                    break
            else:
                idx = len(self.nextFloorsUp)
            print("Destination added upwards to floor {d}".format(d=destination))
            self.nextFloorsUp = self.nextFloorsUp[:idx] + [destination] + self.nextFloorsUp[idx:]
            return True
            
        elif destination < self.currentFloor: # Want to go down. Sort of the same logic, but backwards
            for i in range(len(self.nextFloorsDown)-1, -1, -1):
                floorFromList = self.nextFloorsDown[i]
                if destination == floorFromList:
                    print("Destination already existing")
                    return False
                elif destination < floorFromList:
                    idx = i # Index to insert to keep the list ordered decreasingly.
                    break
            else:
                idx = 0
            print("Destination added downwards to floor {d}".format(d=destination))
            self.nextFloorsDown = self.nextFloorsDown[:idx] + [destination] + self.nextFloorsDown[idx:]
            return True
        return False

    def goToNext(self):
        """
        Returns True if a next stop was made. Returns False if there are no more stops.
        """
        if not self._updateDirection():
            return False
        if self.currentDirection:
            self.currentFloor = self.nextFloorsUp[0]
            self.nextFloorsUp = self.nextFloorsUp[1:]
        else:
            self.currentFloor = self.nextFloorsDown[0]
            self.nextFloorsDown = self.nextFloorsDown[1:]
        # self.currentFloor already is the new one.
        print("Going to floor %d" % self.currentFloor)
        self._removePeople(self.currentFloor)
        return True
           
        
    def _updateDirection(self):
        """
        Updates direction. 
        If nothing remaining, returns False, otherwise True.
        """
        if self.currentDirection and len(self.nextFloorsUp) == 0:
            if len(self.nextFloorsDown) == 0:
                print("All targets reached")
                return False
            else:
                print("Switching direction to Downwards")
                self.currentDirection = False
        elif self.currentDirection == False and len(self.nextFloorsDown) == 0:
            if len(self.nextFloorsUp) == 0:
                print("All target reached")
                return False
            else:
                print("Switching direction to Upwards")
                self.currentDirection = True
        return True
      
    def _removePeople(self, floor):
        if floor in self.weightsByFloor.keys():
            del self.weightsByFloor[floor]
        
      
if __name__ == "__main__":
    
    elevator = Elevator()
    elevator.addPerson(100, 2)
    elevator.goToNext()
    elevator.addPerson(100, 1)
    elevator.addPerson(100, 5)
    elevator.addPerson(50, 3)
    elevator.addPerson(50, 3)
    while elevator.goToNext():
        continue
    elevator.addPerson(500, 5)
    elevator.addPerson(400, 5)
    elevator.goToNext()
        
        
       
        
        
        
        
        
        
        
        