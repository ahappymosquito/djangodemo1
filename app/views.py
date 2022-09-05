from django.shortcuts import render,redirect
from app import models


# Create your views here.
def depart_list(request):
    queryall = models.department.objects.all()

    return render(request,'depart_list.html',{'queryall':queryall})

def depart_add(request):

    if request.method == "GET":
        return render(request, 'depart_add.html')

    title = request.POST.get("title")

    models.department.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request):

    nid = request.GET.get('nid')

    models.department.objects.filter(id=nid).delete()

    return redirect('/depart/list')

def depart_edit(request,nid):
    if request.method == "GET":
        editobj = models.department.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',{'editobj':editobj})
    title = request.POST.get("title")
    models.department.objects.filter(id=nid).update(title = title)
    return redirect('/depart/list')



def user_list(request):
    queryset = models.UserInfo.objects.all()

    return render(request,'user_list.html',{'queryset':queryset})