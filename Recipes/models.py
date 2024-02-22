from django.db import models



class Recipe_Category(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Recipes(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    preparation_time = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='Recipes/', null=True, blank=True)
    category = models.ForeignKey(Recipe_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    recipes = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True, blank=True, related_name="ingredients")


    def __str__(self):
        return self.title


class Instructions(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    recipes = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True, blank=True, related_name="instructions")




