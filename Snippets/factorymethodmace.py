""".
In class-based programming, the factory method pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created. This is done by creating objects by calling a factory method—either specified in an interface and implemented by child classes, or implemented in a base class and optionally overridden by derived classes—rather than by calling a constructor.

similar to one in the book Design Patterns.

The MazeGame uses Rooms but it puts the responsibility of creating Rooms to its subclasses which create the concrete classes. The regular game mode could use this template method:
"""
from abc import ABC, abstractmethod

# Mother of all MazeGame subclasses is a ABC (Abstract Base class)
class MazeGame(ABC):

    def __init__(self):  # MazeGame constructor (template method)
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self):  # refers to the make_room factory method
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self):
        print('Playing using "{}"'.format(self.rooms[0]))

    # factory method that encapsulates the creation of rooms such that other rooms can be used in a subclass.
    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")

""".
In the above snippet, the MazeGame constructor is a template method that makes some common logic. It refers to the make_room factory method that encapsulates the creation of rooms such that other rooms can be used in a subclass.

To implement the other game mode that has magic rooms, it suffices to override the make_room method:
"""


class MagicMazeGame(MazeGame):

    def make_room(self):
        return MagicRoom()


class OrdinaryMazeGame(MazeGame):

    def make_room(self):
        return OrdinaryRoom()


class SimonsMazeGame(MazeGame):
    # def make_room(self):
    #     return SimonsRoom()
    pass


class Room(ABC):
    def __init__(self):
        self.connected_rooms = []

    def connect(self, room):
        self.connected_rooms.append(room)


class MagicRoom(Room):
    def __str__(self):
        return "Magic room"


class OrdinaryRoom(Room):
    def __str__(self):
        return "Ordinary room"


class SimonsRoom(Room):
    def __str__(self):
        return "Simons room"


ordinaryGame = OrdinaryMazeGame()
ordinaryGame.play()

magicGame = MagicMazeGame()
magicGame.play()
try:
    simonsGame = SimonsMazeGame()
    simonsGame.play()
except NotImplementedError as e:
    print(e)
except Exception as e:
    print(e)
