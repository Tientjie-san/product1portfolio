from portfolio.models import *

def add_variable_to_context(request):

    return {
        'github': Social.objects.get(social_name='Github'),
        'linkedin': Social.objects.get(social_name='Linkedin'),
    }