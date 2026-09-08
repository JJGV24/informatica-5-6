import random
import time

def main():

    print("Lo otro eran simulacros.Tú eres el incendio.")
    name = input("Cual es su nombre? ")
    print(f"{name}, que bello nombre")
    time.sleep(3)
    print("Tus ojos tienen la calma,")
    time.sleep(2)
    print("tus risas, un buen compás.")
    time.sleep(2)
    print("Quisiera robarte un rato,")
    time.sleep(2)
    print("y un café de más.")
    time.sleep(2)
    print("No pido grandes promesas,")
    time.sleep(2)
    print("ni el cielo por conquistar;")
    time.sleep(2)
    print("solo un instante contigo para empezar a caminar.")
    time.sleep(2)
    respuesta = input("¿Me concedes este rato y salimos a charlar? ")
    while respuesta != "si":
        time.sleep(3)
        print("Creo que te equivocaste al decir no")
        time.sleep(3)
        print(f"Concedeme una cita contigo {name}, no te decepcionare")
        respuesta = input("Me harias el hombre mas feliz del mundo y me concederias una cita? ")

    fecha = input(f"este viernes? {name} ")
    if fecha == "no":
        time.sleep(3)
        fecha = input("sabado? ")

    print("manda tu direccion al 12345678")
    print("perfecto, te veo a las 8")







if __name__=="__main__":
    main()
