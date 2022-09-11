from django.shortcuts import render,redirect
from app import models
from django import forms

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



class MyForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name","password","age","account","create_time","depart","gender"]

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)

        for name ,field in self.fields.items():
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

def user_add(request):
    if request.method == "GET":
        form = MyForm()
        return render(request, 'user_add.html', {"form": form})

    form = MyForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request,'user_add.html',{"form":form})

def user_edit(request,nid):
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = MyForm(instance=row_obj)
        return render(request, 'user_edit.html', {"form": form})

    form = MyForm(data = request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    return render(request,'user_edit.html',{"form":form})

def user_delete(request,nid):
    models.UserInfo.objects.filter(id = nid).delete()

    # return render(request,'user_list.html')
    return redirect('/user/list/')





















