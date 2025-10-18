def main():
    while True:
        
        try:
            mass = int(input("Mass: "))    
            break
        except ValueError:
            continue

    print(energy(mass))
def energy(mass):
    c = 300000000
    return mass * (c * c)


if __name__ == "__main__":
    main()

