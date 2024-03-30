from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item

# Create your views here.

@login_required
def index(req):
    items = Item.objects.filter(created_by=req.user)
    print(items[0].created_by)
    one = items[0].created_by
    return render(req,'dashboard/index.html',{
        'items':items,
        'one':one,
    })

