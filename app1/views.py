from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request,'team.html')
def points_table(request):
    return render(request,'points table.html')
def players(request):
    return render(request,'players.html')
