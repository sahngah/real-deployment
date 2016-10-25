from django.shortcuts import render, redirect
from .models import Plan
from django.contrib import messages
from ..login_and_registration_app.models import User

# Create your views here.
def index(request):
    return render(request, 'add_plan_app/page.html')

def create(request):
    if request.method == "POST":
        planlist = Plan.objects.plan(request.POST, user=User.objects.get(id=request.session['user']))
        if 'plan' in planlist:
            context = {
            'plan' : planlist['plan']
            }
            # request.session['plan'] = planlist['plan'].name
            return redirect('travel:index')
        else:
            for error in planlist['errors']:
                messages.error(request, error)
    return redirect('addplan:index')
