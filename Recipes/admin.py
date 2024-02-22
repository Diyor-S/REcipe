from django.contrib import admin
from .models import *
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preparation_time', 'category')
    list_filter = ('category',)

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipes', 'recipe')
    list_filter = ('recipe',)


class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipes', 'recipe')
    list_filter = ('recipe',)


admin.site.register(Recipe_Category)
admin.site.register(Recipes, RecipeAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Instructions, InstructionsAdmin)

