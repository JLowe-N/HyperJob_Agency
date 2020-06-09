from django.shortcuts import render
from django.views import View
from .models import vacancy_model_manager


vacancies = vacancy_model_manager.all()


class VacancyBaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancybase.html', context={'vacancies': vacancies})
