from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from account.models import User
from .models import *
from .sort import *
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
# negeer de pylint no member, Django pylint moet nog geinstalleerd worden.
def home(request):
    context = {
        'profile': Profile.objects.get(profile_id = 1),
        'image': Image.objects.get(profile = 1),
        'document_title': "Home"
    }
    return render(request,'portfolio/home.html', context)

def profile(request):
    context ={
        'profile': Profile.objects.get(profile_id=1),
        'image': Image.objects.get(profile=1),
        'interests': Interest.objects.all(),
        'vaardigheden': Tag.objects.all(),
        'document_title': "Profile"
    }
    return render(request, 'portfolio/profile.html', context)
    
def cv(request):
    work = Work_experience.objects.all()
    education = Education.objects.all()
    context ={
        'profile': Profile.objects.get(profile_id=1),
        'work_experiences': work_date_sort(work),
        'educations': education_date_sort(education),
        'document_title': "CV"
    }
    return render(request, 'portfolio/cv.html', context)

def portfolio(request):
    context = {
        'projects': Project.objects.all(),
        'images': Image.objects.exclude(project=None).filter(thumbnail=True),
        'document_title': "Portfolio"
        
    }
    return render(request, 'portfolio/portfolio.html', context)

class ProjectDetailView(DetailView):
      model = Project
      template_name = 'portfolio/project_details.html'
      context_object_name = "project"
      slug_field = "project_title"
      slug_url_kwarg = "project_title"
     
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs) 
          project = get_object_or_404(Project, project_title =self.kwargs.get('project_title'))
          context['images'] = Image.objects.filter(project_id= project.project_id )
          context['document_title'] = project.project_title
          return context


     


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
        messages.success(request, "Formulier is succesvol verzonden!")

    context = {
        'form': form,
        'document_title': "Contact"
    }
    return render(request, 'portfolio/contact.html', context)