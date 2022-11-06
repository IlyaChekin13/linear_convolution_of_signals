import math


class Signal(list):

    def __init__(self, iterable):
        super().__init__(item for item in iterable)
        self.base = self.__len__()

    def discrete_Fourier_transform(self):
        """Makes discrete Fourier transformation,
        returns spectral cofficients"""
        
        self.spectral_coefficients = list()
        
        for k in range(self.base):
            coef = 0
            for n in range(self.base - 1):
                coef += self[n] * (math.cos(((2 * math.pi * k * n) / self.base)) - math.sin(((2 * math.pi * k * n) / self.base)) * 1j)        
            self.spectral_coefficients.append(coef)
    
        return self.spectral_coefficients
        
    def set_up_signal(self, other_signal_base, choose=False):
        """Set the base for linear convolution and pads the signal with zeros by the rule 'base = base_1 + base_2 - 1'"""
        new_base = self.base + other_signal_base - 1
        if choose:
            usr_base = int(input(f'Выберете новую базу не меньше чем {new_base}\n>'))
            if usr_base >= new_base:
                self.base = usr_base
            else:
                print(f'База сигнала должна быть не меньше чем {new_base}')
                self.set_up_signal(choose=True)
        else:
            print(f'База сигнала равна {new_base}')
            self.base = new_base

        for i in range(self.base - self.__len__()):
            self.append(0)
        #self = self + [0 for _ in range(self.base - self.__len__())]
        

#linear convolution

