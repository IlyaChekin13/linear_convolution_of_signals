import math
from signal import Signal
import numpy as np
import os

def inverse_discrete_Fourier_transform(signal: list, base: int) -> list:
    "Returns linear convolution of signals! Ура!"
    linear_convolution = list()
    for k in range(base):
        coef = 0
        for n in range(base):
            coef += signal[n] * (math.cos(((2 * math.pi * k * n) / base)) + math.sin(((2 * math.pi * k * n) / base)) * 1j)

        linear_convolution.append(coef / base)

    return linear_convolution

def mult(dpf_1, dpf_2):
    """Multiply DFTs of signal's values"""
    dpf_3 = list()
    for i in range(len(dpf_1)):
        dpf_3.append(dpf_1[i] * dpf_2[i])
    
    return dpf_3 

def main():
    os.system("clear")
    while True:
        print("Введите номер команды\n \
1 - Линейная свертка дискретных сигналов\n \
2 - Алгоритм быстрого вычисления свертки сигналов на основе ДПФ\n \
-1 - Выход")
        usr_inp = int(input())
        if usr_inp == -1:
            break
        print("Введите первый сигнал\nдля завершения нажмите 'ввод'")
        signal1 = list()
        while True:
            inp = input()
            if inp == "":
                break
            signal1.append(int(inp))
        signal1 = Signal(signal1)
        print("Введите второй сигнал\nдля завершения нажмите 'ввод'")
        signal2 = list()
        while True:
            inp = input()
            if inp == "":
                break
            signal2.append(int(inp))
        signal2 = Signal(signal2)
        if usr_inp == -1:
            break
        elif usr_inp == 2:
            choice = bool(int(input("Желаете выбрать базу сигнала?\n1 - да\n0 - нет")))
            old_base = signal1.base
            signal1.set_up_signal(signal2.base, choose=choice)
            signal2.set_up_signal(old_base, choose=choice)
            dft_1 = signal1.discrete_Fourier_transform()
            dft_2 = signal2.discrete_Fourier_transform()
            signal3 = inverse_discrete_Fourier_transform(mult(dft_1, dft_2), signal1.base)
            print(signal3)
        elif usr_inp == 1:
            print(np.convolve(list(signal1), list(signal2)))


if __name__ == "__main__":
    main()