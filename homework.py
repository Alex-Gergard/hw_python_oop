from asyncio.windows_events import NULL


class Training:
    """Basic class Training."""    
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self, action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight        
    def get_distance(self):
        """The value of the distance."""
        return (self.action*Training.LEN_STEP) / Training.M_IN_KM
    def get_mean_speed(self):
        """Average speed value."""
        return self.get_distance() / self.duration
    def get_spent_calories(self):
        """Calories burned."""
        return 0
    def show_training_info(self):
        """Information message object."""
        temp = __class__.__name__
        return InfoMessage(self.__class__.__name__, self.duration,  self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories())

class Running(Training):
    """Running class."""   
    def get_spent_calories(self) -> float:        
        return (((18*self.get_mean_speed() - 20)         
               * self.weight) / 1000)*self.duration*60     

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
    def get_distance(self):        
        return (self.action*Swimming.LEN_STEP) / Training.M_IN_KM    
    def get_mean_speed(self):
        return ((self.length_pool
               *self.count_pool) / Training.M_IN_KM) / self.duration       
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
    def __init__(self, training_type: str, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories        
    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; ' 
               f'Длительность: {self.duration:.3f} ч.; ' 
               f'Дистанция: {self.distance:.3f} км; '
               f'Ср. скорость: {self.speed:.3f} км/ч; '
               f'Потрачено ккал: {self.calories:.3f}.')

def read_package(type_training, param_training):
    if type_training == 'RUN':
        return Running(param_training[0], param_training[1], param_training[2])
    elif type_training == 'WLK':    
        return SportsWalking(param_training[0], param_training[1], param_training[2], param_training[3])
    elif type_training == 'SWM':    
        return Swimming(param_training[0], param_training[1], param_training[2], param_training[3], param_training[4])
    else:
        print ('Не известнный код тренировки')
        return NULL

def main(training_info) -> None:
    info = training_info.show_training_info()                
    print(info.get_message())
    
def test_prgm():
    training_1 = read_package('SWM', [720, 1, 80, 25, 40])        
    main(training_1)

test_prgm()
i = 777   
