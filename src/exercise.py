from product import Product

def main():
    #write your code below this line
    tape_measure = Product("Tape measure")
    plaster = Product.with_location("Plaster", "home improvement section")
    tyre = Product.with_weight("Tyre", 5)

    print(tyre)

if __name__ == '__main__':
    main()
