with open('recipe.txt', 'rt', encoding='utf') as file:
    cook_book = {}
    for i in file:
        dish_name = i.strip()
        amount_of_ingredients = int(file.readline())
        ingredients = []
        for _ in range(amount_of_ingredients):
            a = file.readline().strip().split(' | ')
            ingredient, quantity, measure = a
            ingredients.append({'ingredient_name': ingredient,
                                'quantity': quantity,
                                'measure': measure})
        cook_book[dish_name] = ingredients
        file.readline()
        recipe = {'Dish_name': dish_name,
                  'amount': amount_of_ingredients,
                  'ingredients': ingredients}


    def get_shop_list_by_dishes(dishes_name, amount):

        shop_list = {}
        dict_of_amount = {}

        for dish in dishes_name:
            if dish in cook_book:
                for ingredient_1 in cook_book[dish]:
                    g = int(ingredient_1['quantity']) * amount
                    ingredient_1['quantity'] = g
                    dict_of_amount['measure'] = ingredient_1['measure']
                    dict_of_amount['quantity'] = ingredient_1['quantity']
                    shop_list[ingredient_1['ingredient_name']] = dict_of_amount
            else:
                print('Блюда нет в меню')
        return shop_list


print(cook_book)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
