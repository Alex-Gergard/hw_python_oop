class Training:
    """Basic class Training."""
    COEFF_CONVERSION = 1000
    LEN_STEP = 0.65
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight        
    def get_distance(self):
        """The value of the distance."""
        return (self.action*LEN_STEP) / COEFF_CONVERSION
    def get_mean_speed(self):
        """Average speed value."""
        return self.get_distance() / self.duration
    def get_spent_calories(self):
        """Calories burned."""
        return 0
    def show_training_info(self):
        """Information message object."""
        return 0

class Running(Training):
    """Running class."""   
    def get_spent_calories(self):        
        return ((18*self.get_mean_speed() - 20) * self.weight) / (1000*self.duration*60)      

class SportsWalking(Training):
    """Sportswalking class."""
    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height   
    def get_spent_calories(self):        
        return (0.035*self.weight + (2*self.get_mean_speed() / self.height) * 0.029 * self.weight) *60*self.duration

class Swimming(Training):
    """Swimming class."""
    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool   
    def get_spent_calories(self):        
        return 