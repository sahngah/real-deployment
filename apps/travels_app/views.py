from django.shortcuts import render, redirect
from ..add_plan_app.models import Plan
from ..login_and_registration_app.models import User

# Create your views here.
def index(request):
    variable3 = User.objects.get(id=request.session["user"])
    context={
    'user': variable3,
    'user_on' : variable3.plan_created.all()|variable3.plans_joined.all(),
    # 'user_on' : Plan.objects.filter(user=variable3)|Plan.objects.filter(users=variable3),
    'user_off' : Plan.objects.exclude(user=variable3).exclude(users=variable3)
    }
    return render(request, 'travels_app/page.html', context)

def details(request, id):
    trip = Plan.objects.get(id=id)
    context = {
    'trip' : trip
    }
    return render(request, 'travels_app/details.html', context)

def join(request, id):
    triptrip = Plan.objects.get(id=id)
    useruser = User.objects.get(id=request.session['user'])
    triptrip.users.add(useruser)
    return redirect('travel:index')
