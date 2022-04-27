import models
import peewee
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    result = models.Dish.select().order_by(models.Dish.price_in_cents).get()
    return result


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    vegeterian = models.Ingredient.select().where(
        models.Ingredient.is_vegeterian == True)
    for dish in vegeterian.dishes:
        List.add(dish)
        return List


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """


def add_rating_to_restaurant() -> None:
    # """After visiting a restaurant, you want to leave a rating

    # Select the first restaurant in the dataset and add a rating
    # """
    result = models.Rating.create(restaurant=1, rating=5, comment="exquisite")
    return result


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    # result = models.Restaurant.select().where(
    #     models.Restaurant.opening_time > 18.00)
    # return result


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    newDish = models.Dish.create(
        name='cheesy bites', served_at=1, price_in_cents=800.0)

    cheese = models.Ingredient.get(models.Ingredient.name == 'cheese')
    newDish.ingredients.add(cheese)
    # newDish.ingredients.add(models.Ingredient.get(
    #     models.Ingredient.name == 'cheese'))

    return newDish
