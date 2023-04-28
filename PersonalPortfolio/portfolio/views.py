from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm


@login_required
def home(request):
    return render(request, 'home.html', {'name': 'Your Name', 'photo_url': 'https://example.com/photo.jpg', 'email': 'your.email@example.com', 'github': 'https://github.com/AkshithaThumma'})

@login_required
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

@login_required
def about(request):
    return render(request, 'about.html', {'bio': 'Hello, Im Akshitha Thumma, a Computer Science and Engineering graduate with a passion for innovation and creativity. I am always eager to explore new ideas and implement them with enthusiasm. I have a natural ability to learn quickly and adapt to different circumstances, which has helped me excel in various projects and endeavors. I am committed to constantly improving myself and my skills, and I strive to stay up-to-date with the latest technologies and trends in my field.'})

@login_required
def project_form_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # redirect to the portfolio view
            return redirect('portfolio')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
