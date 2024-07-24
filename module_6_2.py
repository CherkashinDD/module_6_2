class Vehicle:
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ["Белый", "Чёрный", "Зелёный", "Красный", "Синий"]

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color: str):
        self.new_color = new_color
        for color in self.__COLOR_VARIANTS:
            if color.lower() == self.new_color.lower():
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Toyota Motors Corporation', 'Toyota Mark II', 500, 'Синий')
vehicle1.print_info()
print()
vehicle1.set_color("Розовый")
vehicle1.set_color("Зелёный")
vehicle1.owner = "Павлюк Анталий Григорьевич"
print()
vehicle1.print_info()
