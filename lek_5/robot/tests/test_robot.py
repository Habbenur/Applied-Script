from robot import Robot
import pytest


class TestRobot:

    def setup_method(self): #övning4
        self.robot = Robot ("kalle", 50) #övning4
        
    def test_start (self):
        robot1 = Robot("kalle", 15)
        robot1.start()
        assert robot1.started is True
        assert robot1.battery == 50
       # self.robot.start() #övning4
       # assert self.robot.battery == 50 #övning4
#övning2
    def test_charge(self):
        robot1 = Robot("kalle", 50)
        robot1.charge()
        assert robot1.battery == 100

#övning3
    def test_move(self):
        robot1= Robot("kalle", 50)
        robot1.move(4) #4 i detta fall är meter som den går
        assert robot1.battery == 10 # 10 i detta fall är batteriet som är kvar efter den gått

#övning5
    def test_introduce(self):
        robot1= Robot("kalle", 50)
        self.robot.introduce()
        assert self.robot.greating == "Hello! I am kalle."

#övning7:

    def test_move2(self):
        with pytest.raises(ValueError, match="Ett fel inträffade!"):
            self.robot.move2(-5)

#övning9:
    def test_multiple_robots(self):
    #"""Kontrollerar att alla Robot-objekt i listan har batteri = 100."""
        robots = [Robot("Alpha", 100), Robot("Beta", 100), Robot("Gamma", 100)]
        for robot in robots:
            assert robot.battery == 100