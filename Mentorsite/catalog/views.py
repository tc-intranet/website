from django.shortcuts import render

# Create your views here.
from catalog.models import Mentee, Mentor, Mentorgroup

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_mentee = Mentee.objects.all().count()
    num_mentor = Mentor.objects.all().count()
    num_mentorgroup = Mentorgroup.objects.all().count()
    # Available books (status = 'a')
    
    
    # The 'all()' is implied by default.    
    
    
    context = {
        'num_mentee': num_mentee,
        'num_mentor': num_mentor,
        'num_mentorgroup': num_mentorgroup,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)