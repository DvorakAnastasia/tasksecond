from pprint import pprint


with open('menu.txt', encoding='utf-8') as file:
    cook_book = {}
    ingredients = {}
    for line in file:
        dish = line.strip()
        quantity_ingr = file.readline().strip()
        dish_list = []
        for ingr in range(int(quantity_ingr)):
            ingredient = file.readline().strip().split('|')
            ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
            dish_list.append(ingredients)
        cook_book[dish] = dish_list
        file.readline()
print(cook_book)


def get_shop_list_by_dishes():
    shopping_list = {}
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите список блюд (через запятую): ').split(', ')
    for element in dishes:
        if element in cook_book:
            food = cook_book[element]
            for ingred in food:
                name = ingred['ingredient_name']
                if name in shopping_list:
                    shopping_list[name]['quantity'] += int(ingred['quantity']) * person_count
                else:
                    shopping_list[name] = {'measure': ingred['measure'],
            'quantity': int(ingred['quantity']) * person_count}
        else:
            print('Такого блюда нет')
    print(f"Для приготовления блюд на {person_count} человек  нам необходимо купить:")
    pprint(shopping_list)

get_shop_list_by_dishes()
