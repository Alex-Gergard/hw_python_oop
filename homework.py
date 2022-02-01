class Training:
    """Basic class Training."""
    COEFF_CONVERSION = 1000
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight        
    def get_distance(self):
        """The value of the distance."""
        return (self.action*Training.LEN_STEP) / Training.COEFF_CONVERSION
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
        return ((18*self.get_mean_speed() - 20) 
               * self.weight) / (1000*self.duration*60)      

class SportsWalking(Training):
    """Sportswalking class."""
    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height   
    def get_spent_calories(self):        
        return (0.035*self.weight 
               + ((self.get_mean_speed()**2) // self.height)
               * 0.029 * self.weight) * 60 * self.duration

class Swimming(Training):
    """Swimming class."""
    LEN_STEP = 1.38
    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
    def get_mean_speed(self):
        return ((self.length_pool
               *self.count_pool) / Training.COEFF_CONVERSION) / self.duration       
    def get_spent_calories(self):        
        return (self.get_mean_speed()+1.1) * 2*self.weight

class InfoMessage:    
    """InfoMessage.    
    
    training_type - тип тренировки
    duration - длительность тренировки
    distance -дистанция приодоленная за тренировку
    speed - средняя скорость движения во время движения
    calories - потраченные за время тренировки килокалории
    """
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories        
    def get_message(self):
        return f'Тип тренировки: {self.training_type}; \
                Длительность: {self.duration} ч.; \
                Дистанция: {round(self.distance, 3)} км; \
                Ср. скорость: {round(self.speed, 3)} км/ч; \
                Потрачено ккал: {round(self.calories, 3)}.'

def get_start_message():
    """Output to terminal start message."""
    print('Для эмуляции получения пакетов от блока датчиков')
    print('введите параметры для опереденного типа тренировки:')
    print('Бег: количество шагов, длительность, вес тела;')
    print('Спортиная ходьба: количество шагов, длительность, вес тела, рост;')
    print('Плавание: количество гребков, длительность, блина бассейна, количество бассейнов;')

def read_package():
    get_start_message()
    

run1 = Running(9000, 1, 75)
print(f'{run1.get_spent_calories()}')

