
def main():
# 1 = 184.01 colombia
# 1 =  peruanos
# 1 =  brazil

    colombia = float(input("Colombian pesos: "))
    peru = float(input("Peruvian Soles: "))
    brazil = float(input("Brazilian Reais: "))

    pesos = (colombia * 184.01) + (peru * 0.20) + (brazil * 0.31)
    pesos = round(pesos, 2)

    dollar = (pesos / 17.07)
    dollar = round(dollar, 2)

    print("Mexican pesos: ", pesos)
    print("US dollars: ", dollar)




if __name__ == "__main__":
    main()
