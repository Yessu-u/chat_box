from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import *

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/groups/")
        else:
            return redirect("/")
    else:
        return render(request,'chat/login.html')

def logout_user(request):
    logout(request)
    return redirect("/")


def frontpage(request):
    return render(request,'chat/frontpage.html')

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', locals())

@login_required
def addrooms(request):
    rooms = Room.objects.all()
    if request.method=="POST":
        room_name = request.POST['groupname']
        obje = Room.objects.create(name=room_name, slug=room_name.lower())
        return redirect("/groups/")
    return render(request, 'chat/addrooms.html', locals())

@login_required
def delrooms(request):
    rooms = Room.objects.all()
    if request.method=="POST":
        userlst = request.POST.getlist('rname')
        for i in userlst:
            obje = Room.objects.get(name = i)
            obje.delete()
        return redirect("/groups/")
    return render(request, 'chat/delrooms.html', locals())

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'chat/room.html', locals())

@login_required
def roomusers(request, slug, id):
    grp_members = user_room.objects.filter(room_id=id)
    return render(request, 'chat/roomusers.html', locals())

@login_required
def addusers(request, slug, id):
    u_ids = user_room.objects.filter(room_id=id)
    u_ids_lst = []
    for i in u_ids:
        u_ids_lst.append(i.user_id)
    u_ids_lst = list(set(u_ids_lst))
    grp_members = User.objects.exclude(id__in = u_ids_lst)
    if request.method=="POST":
        userlst = request.POST.getlist('userid')
        for i in userlst:
            obje = user_room.objects.create(user=User.objects.get(id=i), room=Room.objects.get(id=id))
        return redirect("/groups/"+slug+"/"+str(id)+"/")
    return render(request, 'chat/addusers.html', locals())

@login_required
def delusers(request, slug, id):
    grp_members = user_room.objects.filter(room_id = id)
    if request.method=="POST":
        userlst = request.POST.getlist('userid')
        for i in userlst:
            obje = user_room.objects.get(id = i)
            obje.delete()
        return redirect("/groups/"+slug+"/"+str(id)+"/")
    return render(request, 'chat/delusers.html', locals())
