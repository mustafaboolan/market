from django.shortcuts import get_object_or_404, redirect, render
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)

    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    

    return render(request,'item/detail.html',{'item':item,'related_items':related_items})


@login_required
def addnew(request):
    if request.method =='POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid:
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('detail', pk=item.id)
    else:        
        form = NewItemForm()
        return render(request,'item/new.html',{
            'form':form,
            'title':'New item'
    })


@login_required
def delete(req,pk):
    item = get_object_or_404(Item,pk=pk,created_by=req.user)
    print(req.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    # print(request.user,'from edit')
    # print(list(request.POst))
    if request.method =='POST':
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid:
            # item=form.save(commit=False)
            # item.created_by=request.user
            # item.save()
            form.save()
            return redirect('detail', pk=item.id)
    else:        
        form = EditItemForm(instance=item)
        return render(request,'item/new.html',{
            'form':form,
            'title':'Edit item'
    })



# browser page view 
    
def items (request):
    search = request.GET.get('query','')
    cat_id = request.GET.get('category',0)
    print(search)
    items = Item.objects.filter(is_sold = False)
    cats  = Category.objects.all()
    # print(cats[0].name)
    if cat_id :
        items = items.filter(category_id=cat_id)

    if search!='':
        # the name here is name of item and icontains use to serch the string
        items=items.filter(name__icontains=search)

    return render(request,'item/items.html',{
        'items':items,
        'search':search,
        'categories':cats,
        'cat_id':int(cat_id)
    })