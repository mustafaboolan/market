from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def new_conversation(req,item_pk):
    item = get_object_or_404(Item,pk=item_pk)
    if item.created_by == req.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(member__in = [req.user.id])
    if conversations:
        pass #redirect to conversation

    if req.method == 'POST':
        form = ConversationMessageForm(req.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.member.add(req.user)
            conversation.member.add(item.created_by)
            conversation.save()
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = req.user
            conversation_message.save()
            print(item.pk)
            return redirect('detail',pk=item_pk)
    else:
        form = ConversationMessageForm()
        return render (req,'conversation/new.html',{
            'form':form,
        })



@login_required
def inbox(req):
    conversations = Conversation.objects.filter(member__in = [req.user.id])

    return render(req,'conversation/inbox.html',{
        'conversations':conversations
    })

@login_required
def msg_detail(request,pk):
    msg = Conversation.objects.filter(member__in=[request.user.id]).get(pk=pk)
    return render(request,'conversation/msg_detail.html',{
        'messages':msg
    })
