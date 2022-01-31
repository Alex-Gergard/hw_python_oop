class Training:
    """Basic class Training."""
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight
        COEFF_CONVERSION = 1000
        LEN_STEP = 0.65
    def get_distance(self):
        """The value of the distance covered during the workout."""
        return (action*LEN_STEP) / COEFF_CONVERSION
    def get_mean_speed(self):
        """Average speed value."""
        return get_distance(self) / duration
    def get_mean_speed(self):        