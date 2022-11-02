import math 


def FinalBase(signal1: list, signal2: list) -> int:
    "Choose the new base of signals"
    min_base = len(signal1) + len(signal2) - 1
    base = int(input(f"Выберете базу сигнала не меньше чем {min_base}.\n>"))
    if base < min_base:
        print(f"База сигнала должна быть не меньше {min_base}!")
        return FinalBase(signal1, signal2)
    else:
        return base


def DPF(signal: list, base: int) -> list:
    "Returns spectral coefficient"
    spectral_coefficients = list()
    signal = signal + [0 for _ in range(base - len(signal))]

    for k in range(base):
        coef = 0
        for n in range(base - 1):
            coef += signal[n] * (math.cos(((2 * math.pi * k * n) / base)) - math.sin(((2 * math.pi * k * n) / base)) * 1j)
        
        spectral_coefficients.append(coef)
    
    return spectral_coefficients


def ODPF(signal: list, base: int) -> list:
    "Returns linear convolution of signals! Ура!"
    linear_convolution = list()
    for k in range(base):
        coef = 0
        for n in range(base):
            coef += signal[n] * (math.cos(((2 * math.pi * k * n) / base)) + math.sin(((2 * math.pi * k * n) / base)) * 1j)

        linear_convolution.append(coef / base)

    return(linear_convolution)

def mult(dpf_1, dpf_2):
    signal = list()
    for i in range(len(dpf_1)):
        signal.append(dpf_1[i] * dpf_2[i])
    
    return signal 


def main():
    signal1 = list()
    signal2 = list()
    with open("HISTORY.txt", 'w') as f:
        f.write("")

    print("Введите первый сигнал")

    while True:
        user_input = input('>')
        if user_input == "":
            break
        signal1.append(int(user_input))
    print("Введите второй сигнал>")

    while True:
        user_input = input('>')
        if user_input == "":
            break
        signal2.append(int(user_input))

    base = FinalBase(signal1, signal2)
     
    dpf_1 = DPF(signal1, base)
    dpf_2 = DPF(signal2, base)

    signal3 = mult(dpf_1, dpf_2)

    final = ODPF(signal3, base)

    for i, coef in enumerate(dpf_1):
        print(f"K{i} = {coef}\n")

    for i, coef in enumerate(dpf_2):
        print(f"K{i} = {coef}\n")

    print("S3 = S1 * S2\n")

    for i, el in enumerate(signal3):
        print(f"S3({i}) = {el}\n")

    print("Окончательный результат:")

    for i, el in enumerate(final):
            print(f"{i} = {el}\n")

    with open("HISTORY.txt", 'a') as f:
        
        f.write(f"Первый сигнал = {signal1}\nВторой сигнал = {signal2}\nБаза сигналов = {base}\n")
        f.write("Первый сигнал\n")
        for i, coef in enumerate(dpf_1):
            f.write(f"K{i} = {coef}\n")
        f.write("Второй сигнал\n")
        for i, coef in enumerate(dpf_2):
            f.write(f"K{i} = {coef}\n")

        f.write("S3 = S1 * S2\n")

        for i, el in enumerate(signal3):
            f.write(f"S3({i}) = {el}\n")
        
        f.write("Окончательный результат после ОДПФ\n")

        for i, el in enumerate(final):
            f.write(f"{i} = {el}\n")

if __name__ == "__main__":
    main()
