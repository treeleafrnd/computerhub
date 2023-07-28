from .forms import ComputerForm, BrandForm, SpecificationForm, GenerationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Computer, ComputerBrands,ComputerGeneration, ComputerSpecification
from django.http import JsonResponse

class HomeView(View):
    def get(self, request):
        list = Computer.objects.all()
        context = {
            'list': list
        }
        return render(request, 'home.html', context)
class CreateComputerView(View):
    def get(self, request):
        form = ComputerForm()
        context = {
            'form': form,
        }
        return render(request, 'computerform.html', context)

    def post(self, request):
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

class UpdateComputerView(View):
    def get(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        form = ComputerForm(instance=computer)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        form = ComputerForm(request.POST, request.FILES, instance=computer)
        print(form)
        if form.is_valid():

            form.save()
            return redirect('/')

# class DeleteComputerView(View):
#     def get(self, request, pk):
#         computer = get_object_or_404(Computer, pk=pk)
#         computer.delete()
#         return redirect('/')
#
#     def post(self, request, pk):
#         computer = get_object_or_404(Computer, pk=pk)
#         computer.delete()
#         return redirect('/')


class DeleteComputerView(View):
    def post(self, request, pk):
        computer = get_object_or_404(Computer, pk=pk)
        computer_name = computer.computer_code
        computer.delete()
        return JsonResponse({'message': f'Generation "{computer_name}" deleted successfully.'})


class ListBrandView(View):
    def get(self,request):
        list = ComputerBrands.objects.all()
        context = {
            'list': list,
        }
        return render(request,'brandlist.html', context)

class CreateBrandView(View):
    def get(self, request):
        form = BrandForm()
        context = {
            'form': form,
        }
        return render(request, 'brandform.html', context)

    def post(self, request):
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listbrand')
class UpdateBrandView(View):
    def get(self, request, pk):
        brand = get_object_or_404(ComputerBrands, pk=pk)
        form = BrandForm(instance=brand)
        return render(request, 'brand_update.html', {'form': form})
    def post(self, request, pk):
        brand = get_object_or_404(ComputerBrands, pk=pk)
        form = BrandForm(request.POST,request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('listbrand')

class DeleteBrandView(View):
    def post(self, request, pk):
        brand = get_object_or_404(ComputerBrands, pk=pk)
        brand_name = brand.brand_name
        brand.delete()
        return JsonResponse({'message': f'Generation "{brand_name}" deleted successfully.'})

class CreateGenerationView(View):
    def get(self, request):
        form = GenerationForm()
        context = {
            'form': form,
        }
        return render(request, 'generationform.html', context)

    def post(self, request):
        form = GenerationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listgeneration')

class ListGenerationView(View):
    def get(self, request):
        list = ComputerGeneration.objects.all()
        context = {
            'list':list,
        }
        return render(request, 'generationlist.html', context)

class DeleteGenerationView(View):
    def post(self, request, pk):
        generation = get_object_or_404(ComputerGeneration, pk=pk)
        generation_name = generation.generation
        generation.delete()
        return JsonResponse({'message': f'Generation "{generation_name}" deleted successfully.'})

class UpdateGenerationView(View):
    def get(self, request, pk):
        generation = get_object_or_404(ComputerGeneration, pk=pk)
        form = GenerationForm(instance=generation)
        return render(request, 'generation_update.html', {'form': form})

    def post(self, request, pk):
        generation = get_object_or_404(ComputerGeneration, pk=pk)
        form = GenerationForm(request.POST, instance=generation)
        if form.is_valid():
            form.save()
            return redirect('listgeneration')

class CreateSpecificationView(View):
    def get(self, request):
        form = SpecificationForm()
        context = {
            'form': form,
        }
        return render(request, 'specificationform.html', context)

    def post(self, request):
        form = SpecificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listspecification')

class ListSpecificationView(View):
    def get(self, request):
        list = ComputerSpecification.objects.all()
        context = {
            'list':list,
        }
        return render(request,'specificationlist.html',context)

class DeleteSpecificationView(View):
    def post(self, request, pk):
        specification = get_object_or_404(ComputerSpecification, pk=pk)
        specification_name = specification.generation
        specification.delete()
        return JsonResponse({'message': f'Generation "{specification_name}" deleted successfully.'})

class UpdateSpecificationView(View):
    def get(self, request, pk):
        specification = get_object_or_404(ComputerSpecification, pk=pk)
        form = SpecificationForm(instance=specification)
        return render(request, 'specification_update.html', {'form': form})

    def post(self, request, pk):
        specification = get_object_or_404(ComputerSpecification, pk=pk)
        form = SpecificationForm(request.POST, instance=specification)
        if form.is_valid():
            form.save()
            return redirect('listspecification')