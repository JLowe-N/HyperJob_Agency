from django.db import models
from django.contrib.auth import get_user_model

class Resume(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


resume_objects_manager = Resume.objects
# Because the database isn't helping troubleshoot

#Resume.objects.create(description='Best web developer', author=User.objects.get_by_natural_key("jlowen"))
#Resume.objects.create(description='Engineer', author=User.objects.get_by_natural_key("jlowen"))

