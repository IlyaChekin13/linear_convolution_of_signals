import math
from signal import Signal
import numpy as np
import os
from datetime import datetime


info = "Введите номер команды\n \
1 - Линейная свертка дискретных сигналов\n \
2 - Алгоритм быстрого вычисления свертки сигналов на основе ДПФ\n \
3 - Ввести новые сигналы\n \
-1 - Выход"

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

def write_to_file(massage):
    with open("HISTORY.txt", "a") as f:
        f.write(massage)

def main():
    now = datetime.now()
    write_to_file("Сессия от " + now.strftime("%d/%m/%Y %H:%M:%S") + ":\n")
    os.system("clear")
    cycle_count = 0
    signal1 = False
    keep_signals = True
    usr_inp = 0
    while True:

        if usr_inp == -1:
            write_to_file("Конец сессии.\n\n")
            break
        if usr_inp == 3:
            keep_signals = True #int(input("Введите 0 - оставить текущие сигналы, 1 - ввести новые.\n"))
        else:
            keep_signals = False
        if keep_signals:
            write_to_file("Ввод новых сигналов\n")    
            print("Введите первый сигнал\nдля завершения нажмите 'ввод'")
            signal1 = list()
            while True:
                inp = input()
                if inp == "":
                    break
                signal1.append(int(inp))
            signal1 = Signal(signal1)
            write_to_file("Первый сигнал - " + str(signal1) + "\n")
            print("Введите второй сигнал\nдля завершения нажмите 'ввод'")
            signal2 = list()
            while True:
                inp = input()
                if inp == "":
                    break
                signal2.append(int(inp))
            signal2 = Signal(signal2)
            write_to_file("Второй сигнал - " + str(signal2) + "\n")
        if usr_inp == 2:
            write_to_file("Алгоритм быстрого вычисления свертки сигналов на основе ДПФ\n")
            choice = bool(int(input("Желаете выбрать базу сигнала?\n1 - да\n0 - нет\n")))
            write_to_file(f"Выбор базы сигнала - {choice} \n")
            old_base = signal1.base
            signal1.set_up_signal(signal2.base, choose=choice)
            signal2.set_up_signal(old_base, choose=choice)
            write_to_file(f"База сигналов равна {len(signal1)} \n")
            dft_1 = signal1.discrete_Fourier_transform()
            dft_2 = signal2.discrete_Fourier_transform()
            signal3 = inverse_discrete_Fourier_transform(mult(dft_1, dft_2), signal1.base)
            print(signal3)
            write_to_file(f"Результат {signal3} \n")
        if usr_inp == 1:
            print("Линейная свертка дискретных сигналов")
            write_to_file("Линейная свертка дискретных сигналов \n")
            result = np.convolve(list(signal1), list(signal2))
            print(result)
            write_to_file(f"Результат {str(result)} \n")
        print(info)
        usr_inp = int(input())
        cycle_count += 1


if __name__ == "__main__":
    main()