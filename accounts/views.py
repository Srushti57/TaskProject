from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Item

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def videoView(request):
    obj = Item.objects.all()
    
    return render(request, 'video.html', {'obj': obj})

def counter(request):
    ct = request.session.get('count', 0)
    newct = ct + 1
    request.session['count'] = newct
    return render(request, 'counter.html', {'c':newct})

class CtChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Item.objects.all()
        return context
    def v(self,):
        views = Item.objects.all().count()
        return views
    