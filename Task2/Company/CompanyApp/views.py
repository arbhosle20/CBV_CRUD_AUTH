from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop
from django .views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AddLaptopView(LoginRequiredMixin,View):
    def get(self,request):
        form = LaptopModelForm()
        template_name = 'CompanyApp/addlaptop.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
        template_name = 'CompanayApp/addlaptop.html'
        context = {'form':form}
        return render(request,template_name,context)

class ShowLaptopView(View):
    def get(self,request):
        laptop_list = Laptop.objects.all()
        template_name = 'CompanyApp/showlaptop.html'
        context = {'laptop_list':laptop_list}
        return render(request,template_name,context)

class LaptopUpdate(LoginRequiredMixin,View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=laptop)
        template_name = 'CompanyApp/addlaptop.html'
        context ={'form':form}
        return render(request,template_name,context)
    def post(self ,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
        template_name = 'CompanyApp/addlaptop.html'
        context = {'form':form}
        return render(request,template_name,context)

class LaptopDelete(LoginRequiredMixin,View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'CompanyApp/deletelaptop.html'
        context = {'laptop':laptop}
        return render(request,template_name,context)

    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        laptop.delete()
        return redirect('show_laptop')





# Create your views here.
