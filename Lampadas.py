import random
import time

def setup_lamps():
    lamps = [1, 2, 3]
    random.shuffle(lamps)
    return lamps

def check_lamps(lamps, state):
    if state == 1:
        for i in range(3):
            if lamps[i] == 2:
                return f"Lâmpada {i + 1} está acesa (controlada pelo Interruptor 2)"
    elif state == 2:
        for i in range(3):
            if lamps[i] == 1:
                return f"Lâmpada {i + 1} está apagada e quente (controlada pelo Interruptor 1)"
    else:
        for i in range(3):
            if lamps[i] == 3:
                return f"Lâmpada {i + 1} está apagada e fria (controlada pelo Interruptor 3)"
    return "Não foi possível determinar a lâmpada."

def main():
    lamps = setup_lamps()
    print(f"Configuração das lâmpadas: {lamps}")
    print("Ligando o Interruptor 1...")
    time.sleep(2)
    print("Desligando o Interruptor 1 e ligando o Interruptor 2...")
    time.sleep(1)
    print("Visitando a primeira sala (lâmpada acesa ou apagada e quente):")
    print(check_lamps(lamps, 1))
    print("Visitando a segunda sala (lâmpada apagada e quente ou fria):")
    print(check_lamps(lamps, 2))

    for i in range(3):
        if lamps[i] != 1 and lamps[i] != 2:
            print(f"Lâmpada {i + 1} está apagada e fria (controlada pelo Interruptor 3)")
            break

if __name__ == "__main__":
    main()
