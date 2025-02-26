from car import Car

class TestCar:
    def test_start (self):
        car = Car("Tesla", 2024)
        car.start()
        assert car.started is True

    def setup_method(self):
        self.car = Car("Tesla", 2024)

    def test_initial_state(self):
        assert self.car.started is False

    def test_start(self):
        self.car.start()
        assert self.car.started is True
        
