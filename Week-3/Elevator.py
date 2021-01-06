# Python Class 2532
# Lesson 3 Problem 4
# Author: riatalwar (486154)
# Add an attribute passengers that is a list of strings representing the names of the people.
# (This will also require modifying the constructor method -- new elevators should start out empty of passengers.)
# Modify the __str__() method to also print the names of the passengers.
# Add methods get_on() and get_off() to allow passengers to get on and off.
# Of course, passengers can only get on and off if the doors are open!
# Make sure your methods do something appropriate if the doors are closed (for example, printing a message to that effect).
# Also make sure that get_off() does something appropriate if that person is not on the elevator.
class Elevator:
    '''Represents a simple elevator'''

    def __init__(self, startFloor, startDoorsOpen):
        '''Elevator(startFloor, startDoorsOpen) -> Elevator
        Constructs an Elevator
        startFloor: int giving the starting floor
        startDoorsOpen: bool giving the starting doors
                    (True = 'open')'''
        self.floor = startFloor
        self.doorsOpen = startDoorsOpen
        self.passengers = []

    def __str__(self):
        '''str(Elevator) -> str
        Returns a string giving the floor and state of the doors.'''
        if self.doorsOpen:
            answer = 'doors open'
        else:
            answer = 'doors closed'
        answer += ', floor ' + str(self.floor)
        answer += ', passengers '
        answer += ', '.join(self.passengers)
        return answer

    def open_doors(self):
        '''Elevator.open_doors()
        Opens the doors by setting doors attribute to True.'''
        self.doorsOpen = True # set doors to open

    def close_doors(self):
        '''Elevator.close_doors()
        Closes the doors by setting doors attribute to False.'''
        self.doorsOpen = False # set doors to closed

    def go_up(self):
        '''Elevator.go_up()
        Goes up by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor += 1              # increase floor by 1

    def go_down(self):
        '''Elevator.go_down()
        Goes down by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor -= 1              # decrease floor by 1

    def go_to_floor(self, destination):
        '''Elevator.go_to_floor(int)
        Closes doors, moves to destination, and opens doors.'''
        if self.doorsOpen:               # if doors are open
            self.close_doors()           # close 'em
        while self.floor != destination: # if not at destination
            if self.floor < destination: # if below
                self.go_up()             # go up 1 floor
            else:                        # if above
                self.go_down()           # go down 1 floor
        self.open_doors()                # open doors

    def get_on(self, passenger):
        '''Adds a passenger to the elevator'''
        if self.doorsOpen == True:
            self.passengers.append(passenger)
        else:
            print('Please open the doors.')

    def get_off(self, passenger):
        '''Removes a passenger from the elevator'''
        if passenger in self.passengers and self.doorsOpen == True:
            self.passengers.remove(passenger)
        elif passenger not in self.passengers:
            print('Passenger not found.')
        else:
            print('Please open the doors.')

e = Elevator(0, True)
print(e)
e.get_on('Ria')
print(e)
e.close_doors()
print(e)
e.go_up()
print(e)
e.open_doors()
print(e)
e.get_on('Flora')
print(e)
e.close_doors()
print(e)
e.go_up()
e.go_up()
print(e)
e.get_on('Sophie')
print(e)
e.open_doors()
print(e)
e.get_on('Sophie')
print(e)
e.close_doors()
print(e)
e.go_up()
print(e)
e.get_off('Maria')
print(e)
e.open_doors()
print(e)
e.get_off('Ria')
print(e)
