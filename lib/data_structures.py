spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"]for food in spicy_foods]    
    

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food["heat_level"]>5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji_string = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji_string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji_string = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji_string}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    return int(total_heat_level / num_foods)

def create_spicy_food(spicy_foods, spicy_food):
    updated_spicy_foods = spicy_foods.copy()  # Create a copy of the original list
    updated_spicy_foods.append(spicy_food)  # Add the new spicy food to the copy
    return updated_spicy_foods