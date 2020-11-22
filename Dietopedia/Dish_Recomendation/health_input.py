from Dish_Recomendation.health_api import *
import urllib
from Dish_Recomendation.recipe import *

json_saved = {}


def shuffle_meals(saved_json, calorie_goal, meals = ["breakfast", "lunch", "dinner"] ): 
    day_list = []
    for meal in meals:
        day_list.append(add_recipe(saved_json[meal],calorie_goal))
    return day_list


def generate_meals(calories: int):
    for meal in ["breakfast", "lunch", "dinner"]:
        url = create_url() 
        print(url)
        json = get_result(url)
        print(json)
        json_saved[meal] = json    
    return shuffle_meals(json_saved,calories)



# if __name__ == "__main__":
# ##    activity = get_activity()
# ##    print(get_multiplier(activity))
# ##    gender = get_gender()
# ##    age = get_age()
# ##    height = get_height()
# ##    weight = get_weight()
# ##    calorie_goal = get_calories(gender, age, height, weight, activity)
# ##    print("Calorie goal", calorie_goal)
# ##
#     calorie_goal = 2000
#     day_list = []
#     json_saved = {}

#     for meal in ["breakfast", "lunch", "dinner"]:
#         url = create_url() + "&q=" + meal
#         json = get_result(url)
#         json_saved[meal] = json

#     day_list = shuffle_meals(json_saved,calorie_goal)

#     total_cals = 0
#     for meal in day_list:
#         print(meal.name)
#         cals = meal['calories']
#         print(cals)
#         total_cals+=cals
#     print("Total Calories:" + str(total_cals))

#     for key,value in day_list[0].quants.items():
#         print(key, value)


#     while input("Shuffle?") == "y":
#         day_list = shuffle_meals(json_saved, calorie_goal)
#         total_cals = 0
#         for meal in day_list:
#             print(meal.name)
#             cals = meal['calories']
#             print(cals)
#             total_cals+=cals
#         print("Total Calories:" + str(total_cals))
