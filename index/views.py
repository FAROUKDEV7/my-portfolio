from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def index(request):
    # Contact Me
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid:
            my_form=form.save(commit=False)
            my_form.user=request.user
            my_form.save()
    else:
        form=ContactForm()

    context={
        'form':form
    }
    return render(request,'pages/index.html',context)