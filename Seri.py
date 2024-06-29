def simulation(r,x): 
    assert x < 1
    return r*x*(1 - x)

def main():
    while True:
        rate = float(input("What is the rate of growth? "))
        initialPopulation = float(input("What is the first population? "))

        ans = simulation(rate, initialPopulation)
        for i in range(100):
            print(ans)
            ans = simulation(rate, initialPopulation)


if __name__ == "__main__":
    main()