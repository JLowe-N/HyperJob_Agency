from django.shortcuts import render
from django.views import View
from .models import resume_objects_manager, Resume


resumes = resume_objects_manager


class ResumeBaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resumebase.html', context={'resumes': resumes.all()})
