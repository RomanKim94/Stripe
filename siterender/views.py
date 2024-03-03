from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from Item.models import Item
from .forms import ItemForm


class ItemDetailView(DetailView):
    model = Item
    template_name = 'siterender/item_detail.html'
    context_object_name = 'item'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            max_pk = Item.objects.aggregate(Max('id', default=0))['id__max']
            return redirect('item-detail', pk=max_pk)
        else:
            error = 'Форма была заполнена не верно'

    form = ItemForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'siterender/item_create.html', data)


def buy_item(request):
    return HttpResponse('buy-item')
