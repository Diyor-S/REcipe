from django.shortcuts import render
from .models import *


def main_page_view(request):
    recipe_categories = Recipe_Category.objects.all()
    recipes = Recipes.objects.all()

    context = {
        "title": "Main page",
        "categories": recipe_categories,
        "recipes": recipes
    }

    return render(request, "recipes/main_page.html", context)



def category_page_view(request, category_id):
    recipes = Recipes.objects.filter(category=category_id)
    recipe_titles = [recipe.title for recipe in recipes]
    category = Recipe_Category.objects.get(id=category_id)

    context = {
        "title": "Страница категории",
        "category.title": f"Категория: {category}",
        "recipes": f"Рецепты: {recipe_titles}"
    }

    return render(request, "recipes/category_page.html", context)


def recipe_detail_page_view(request, recipe_id):
    recipes = Recipes.objects.get(id=recipe_id)

    ingredients = Ingredients.objects.filter(recipe=recipes)
    instructions = Instructions.objects.filter(recipe=recipes)

    context = {
        "title": "Страница рецептов",
        "recipe": recipes,
        "ingredients": ingredients,
        "instructions": instructions
    }
    return render(request, "recipes/recipe_detail.html", context)