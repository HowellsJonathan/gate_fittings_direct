from django.shortcuts import render
from django_user_agents.utils import get_user_agent

# Create your views here.

def index(request):
    """ A view to return the index page """
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, 'home/mobile/index.html')
    elif user_agent.is_tablet:
        return render(request, 'home/index.html')
    elif user_agent.is_pc:
        return render(request, 'home/index.html')