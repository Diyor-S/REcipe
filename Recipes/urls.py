from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page_view, name="main_page"),
    path('category/<int:category_id>/', category_page_view, name="category"),
    path('recipe/<int:recipe_id>/', recipe_detail_page_view, name="recipe_detail")

]