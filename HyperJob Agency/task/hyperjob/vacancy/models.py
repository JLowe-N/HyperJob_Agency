from django.db import models
from django.contrib.auth import get_user_model

class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

vacancy_model_manager = Vacancy.objects

#Vacancy.objects.create(description='Python Dev', author=User.objects.get_by_natural_key("jlowen"))
#Vacancy.objects.create(description='Chemical Lead', author=User.objects.get_by_natural_key("jlowen"))
