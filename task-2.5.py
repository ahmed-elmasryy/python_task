from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name, battery_level):
        self._name = name
        self._battery_level = battery_level

    @abstractmethod
    def move(self):
        pass

    def status(self):
        return f"{self._name}, Battery Level: {self._battery_level}%"

    @property
    def battery_level(self):
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self._battery_level = value

class GroundRobot(Robot):
    def __init__(self, name, battery_level, wheels):
        super().__init__(name, battery_level)
        self._wheels = wheels

    def move(self):
        return f"{self._name} is moving on {self._wheels} wheels."

class AerialRobot(Robot):
    def __init__(self, name, battery_level, rotors):
        super().__init__(name, battery_level)
        self._rotors = rotors

    def move(self):
        return f"{self._name} is flying with {self._rotors} rotors."

class FleetManagement:
    def __init__(self):
        self.fleet = []

    def add_robot(self, robot):
        self.fleet.append(robot)

    def move_all(self):
        for robot in self.fleet:
            print(robot.move())

    def status_all(self):
        for robot in self.fleet:
            print(robot.status())

# exampleTest
ground_robot = GroundRobot("GroundBot", 90, 4)
aerial_robot = AerialRobot("AirBot", 85, 6)

fleet = FleetManagement()
fleet.add_robot(ground_robot)
fleet.add_robot(aerial_robot)

print("Moving all robots:")
fleet.move_all()

print("\nStatus of all robots:")
fleet.status_all()
