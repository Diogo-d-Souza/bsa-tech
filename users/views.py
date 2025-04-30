from django.shortcuts import render

def websocket_demo(request):
    return render(request, 'websocket_demo.html')
