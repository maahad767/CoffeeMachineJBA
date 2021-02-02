coffee_machine = {
    'water': 400,
    'milk': 540,
    'beans': 120,
    'cups': 9,
    'cash': 550,
}

coffee_data = {
    'espresso': {
        'water': 250,
        'milk': 0,
        'beans': 16,
        'cost': 4,
    },
    'latte': {
        'water': 350,
        'milk': 75,
        'beans': 20,
        'cost': 7,
    },
    'cappuccino': {
        'water': 200,
        'milk': 100,
        'beans': 12,
        'cost': 6,
    }
}


def main():
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        command = input()
        if command == 'exit':
            break
        elif command == 'remaining':
            show_state()
        elif command == 'buy':
            buy_coffee()
        elif command == 'fill':
            fill_up_machine()
        elif command == 'take':
            take_cash()
        print()


def is_available(coffee):
    if coffee_machine['water'] < coffee_data[coffee]['water']:
        print("Sorry, not enough water!")
    elif coffee_machine['milk'] < coffee_data[coffee]['milk']:
        print("Sorry, not enough milk!")
    elif coffee_machine['beans'] < coffee_data[coffee]['beans']:
        print("Sorry, not enough coffee beans!")
    elif coffee_machine['cups'] < 1:
        print("Sorry, not enough cup!")
    else:
        return True
    return False


def sell_coffee(coffee):
    if is_available(coffee):
        print("I have enough resources, making you a coffee!")
        coffee_machine['water'] -= coffee_data[coffee]['water']
        coffee_machine['milk'] -= coffee_data[coffee]['milk']
        coffee_machine['beans'] -= coffee_data[coffee]['beans']
        coffee_machine['cups'] -= 1

        coffee_machine['cash'] += coffee_data[coffee]['cost']


def buy_coffee():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()

    if coffee_type == 'back':
        return
    else:
        coffee_type = int(coffee_type)

    if coffee_type == 1:
        sell_coffee('espresso')
    elif coffee_type == 2:
        sell_coffee('latte')
    elif coffee_type == 3:
        sell_coffee('cappuccino')


def take_cash():
    print(f"I gave you ${coffee_machine['cash']}")
    coffee_machine['cash'] = 0


def fill_up_machine():
    print('Write how many ml of water do you want to add:')
    coffee_machine['water'] += int(input(''))

    print('Write how many ml of milk do you want to add:')
    coffee_machine['milk'] += int(input())

    print('Write how many grams of coffee beans do you want to add:')
    coffee_machine['beans'] += int(input())

    print('Write how many disposable cups of coffee do you want to add:')
    coffee_machine['cups'] += int(input())


def coffee_possible():
    water_available = coffee_machine['water'] // 200
    milk_available = coffee_machine['milk'] // 50
    beans_available = coffee_machine['beans'] // 15

    return min(water_available, milk_available, beans_available)


def show_state():
    print('\nThe coffee machine has:')
    print(f"{coffee_machine['water']} of water")
    print(f"{coffee_machine['milk']} of milk")
    print(f"{coffee_machine['beans']} of coffee beans")
    print(f"{coffee_machine['cups']} of disposable cups")
    print(f"{coffee_machine['cash']} of money")


if __name__ == '__main__':
    main()
