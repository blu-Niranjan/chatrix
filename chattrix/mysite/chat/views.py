from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, "chat/index.html")

def room(request):
    room_name = request.GET.get('room_name', None)
    if not room_name:
        # handle missing room_name - maybe redirect or error
        return redirect('index')

    username = request.GET.get('username', 'Anonymous')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username,
    })