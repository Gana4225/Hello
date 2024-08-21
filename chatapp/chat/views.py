from django.shortcuts import render
from .models import ChatMessage

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        tagged_message_id = request.POST.get('tagged_message_id')
        username = request.user.get('name')
        
        tagged_message = None
        if tagged_message_id:
            tagged_message = ChatMessage.objects.get(id=tagged_message_id)
        
        ChatMessage.objects.create(username=username, message=message, tagged_message=tagged_message)

    messages = ChatMessage.objects.all().order_by('-timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Chat App!")
