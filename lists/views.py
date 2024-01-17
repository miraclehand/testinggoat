from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.forms import ItemForm
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
        else:
            return render(request, 'list.html', {'list': list_, 'form': form})

    our_list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': our_list, 'form': form})

def new_list(request):
    form = ItemForm(data=request.POST)

    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)

    Item.objects.create(text=request.POST['text'], list=our_list)
    return redirect(f'/lists/{our_list.id}/')
