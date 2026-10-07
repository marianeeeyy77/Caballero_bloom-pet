from django.shortcuts import render
from .models import Pet
from .forms import PetForm


def pet_list(request):
    pets = Pet.objects.all()

    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = PetForm()

    context = {
        'pets': pets,
        'form': form,
    }

    return render(request, 'invApp/pet_list.html', context)
