from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.db.models import Q
from django.forms.models import model_to_dict

from blog_sab_app.models import Estudio, Viajes, Empleos
from blog_sab_app.forms import EstudioForm, ViajesForm, EmpleosForm

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "blog_sab_app/home.html")

def estudios(request):
    estudios = Estudio.objects.all()

    context_dict = {
        'estudios': estudios
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog_sab_app/estudios.html"
    )

def viajes(request):
    viajes = Viajes.objects.all()

    context_dict = {
        'viajes': viajes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog_sab_app/viajes.html"
    )

def empleos(request):
    empleos = Empleos.objects.all()

    context_dict = {
        'empleos': empleos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="blog_sab_app/empleos.html"
    )

def form_hmtl(request):

    if request.method == 'POST':
        estudio = Estudio(universidad=request.POST['universidad'], anio_inicio=request.POST['anio_inicio'], titulo=request.POST['titulo'], finalizado=request.POST['finalizado'])
        estudio.save()

        estudios = Estudio.objects.all()
        context_dict = {
            'estudios': estrudios
        }

        return render(
            request=request,
            context=context_dict,
            template_name="blog_sab_app/estudios.html"
        )

    return render(
        request=request,
        template_name='blog_sab_app/formHTML.html'
    )

def estudio_forms_django(request):
    if request.method == 'POST':
        estudio_form = EstudioForm(request.POST)
        if estudio_form.is_valid():
            data = estudio_form.cleaned_data
            estudio = Estudio(universidad=data['universidad'], anio_inicio=data['anio_inicio'], titulo=data['titulo'], finalizado=data['finalizado'])
            estudio.save()

            estudios = Estudio.objects.all()
            context_dict = {
                'estudios': estudios
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/estudios.html"
            )

    estudio_form = EstudioForm(request.POST)
    context_dict = {
        'estudio_form': estudio_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/estudio_django_forms.html'
    )

def empleo_forms_django(request):
    if request.method == 'POST':
        empleo_form = EmpleosForm(request.POST)
        if empleo_form.is_valid():
            data = empleo_form.cleaned_data
            empleo = Empleos(empresa=data['empresa'], periodo=data['periodo'], puesto=data['puesto'])
            empleo.save()

            empleos = Empleos.objects.all()
            context_dict = {
                'empleos': empleos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/empleos.html"
            )

    empleo_form = EmpleosForm(request.POST)
    context_dict = {
        'empleo_form': empleo_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/empleo_django_forms.html'
    )

def viaje_forms_django(request):
    if request.method == 'POST':
        viaje_form = ViajesForm(request.POST)
        if viaje_form.is_valid():
            data = viaje_form.cleaned_data
            viaje = Viajes(destino=data['destino'], nro_vuelo=data['nro_vuelo'], fecha=data['fecha'], notas=data['notas'])
            viaje.save()

            viajes = Viajes.objects.all()
            context_dict = {
                'viajes': viajes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/viajes.html"
            )

    viaje_form = ViajesForm(request.POST)
    context_dict = {
        'viaje_form': viaje_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/viaje_django_forms.html'
    )

#CRUD ESTUDIOS
def update_estudio(request, pk: int):
    estudio = Estudio.objects.get(pk=pk)

    if request.method == 'POST':
        estudio_form = EstudioForm(request.POST)
        if estudio_form.is_valid():
            data = estudio_form.cleaned_data
            estudio.universidad = data['universidad']
            estudio.anio_inicio = data['anio_inicio']
            estudio.titulo = data['titulo']
            estudio.finalizado = data['finalizado']
            estudio.save()

            estudios = Estudio.objects.all()
            context_dict = {
                'estudios': estudios
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/estudios.html"
            )

    estudio_form = EstudioForm(model_to_dict(estudio))
    context_dict = {
        'estudio': estudio,
        'estudio_form': estudio_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/estudio_form.html'
    )

def delete_estudio(request, pk: int):
    estudio = Estudio.objects.get(pk=pk)
    if request.method == 'POST':
        estudio.delete()

        estudios = Estudio.objects.all()
        context_dict = {
            'estudios': estudios
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog_sab_app/estudios.html"
        )

    context_dict = {
        'estudio': estudio,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/estudio_confirm_delete.html'
    )

#CRUD EMPLEOS
def update_empleo(request, pk: int):
    empleo = Empleos.objects.get(pk=pk)

    if request.method == 'POST':
        empleo_form = EmpleosForm(request.POST)
        if empleo_form.is_valid():
            data = empleo_form.cleaned_data
            empleo.empresa = data['empresa']
            empleo.periodo = data['periodo']
            empleo.puesto = data['puesto']
            empleo.save()

            empleos = Empleos.objects.all()
            context_dict = {
                'empleos': empleos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/empleos.html"
            )

    empleo_form = EmpleosForm(model_to_dict(empleo))
    context_dict = {
        'empleo': empleo,
        'empleo_form': empleo_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/empleo_form.html'
    )

def delete_empleo(request, pk: int):
    empleo = Empleos.objects.get(pk=pk)
    if request.method == 'POST':
        empleo.delete()

        empleos = Empleos.objects.all()
        context_dict = {
            'empleos': empleos
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog_sab_app/empleos.html"
        )

    context_dict = {
        'empleo': empleo,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/empleo_confirm_delete.html'
    )

#CRUD VIAJES
def update_viaje(request, pk: int):
    viaje = Viajes.objects.get(pk=pk)

    if request.method == 'POST':
        viaje_form = ViajesForm(request.POST)
        if viaje_form.is_valid():
            data = viaje_form.cleaned_data
            viaje.destino = data['destino']
            viaje.nro_vuelo = data['nro_vuelo']
            viaje.fecha = data['fecha']
            viaje.notas = data['notas']
            viaje.save()

            viajes = Viajes.objects.all()
            context_dict = {
                'viajes': viajes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="blog_sab_app/viajes.html"
            )

    viaje_form = ViajesForm(model_to_dict(viaje))
    context_dict = {
        'viaje': viaje,
        'viaje_form': viaje_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/viaje_form.html'
    )

def delete_viaje(request, pk: int):
    viaje = Viajes.objects.get(pk=pk)
    if request.method == 'POST':
        viaje.delete()

        viajes = Viajes.objects.all()
        context_dict = {
            'viajes': viajes
        }
        return render(
            request=request,
            context=context_dict,
            template_name="blog_sab_app/viajes.html"
        )

    context_dict = {
        'viaje': viaje,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='blog_sab_app/viaje_confirm_delete.html'
    )

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        estudios = Estudio.objects.filter(universidad__contains=search_param)
        context_dict = {
            'estudios': estudios
        }

    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(universidad__contains=search_param)
        estudios = Estudio.objects.filter(query)
        context_dict = {
            'estudio': estudio
        }

    return render(
        request=request,
        context=context_dict,
        template_name="blog_sab_app/home.html",
    )

#---------------------------------------------------------
#ESTUDIOS

class EstudioListView(ListView):
    model = Estudio
    template_name = "blog_sab_app/estudio_list.html"

class EstudioDetailView(DetailView):
    model = Estudio
    template_name = "blog_sab_app/estudio_detail.html"

class EstudioCreateView(CreateView):
    model = Estudio
    success_url = reverse_lazy('blog_sab_app:estudio-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class EstudioUpdateView(UpdateView):
    model = Estudio
    success_url = reverse_lazy('blog_sab_app:estudio-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class EstudioDeleteView(DeleteView):
    model = Estudio
    success_url = reverse_lazy('blog_sab_app:estudio-list')

#---------------------------------------------------------
#EMPLEOS

class EmpleoListView(ListView):
    model = Empleos
    template_name = "blog_sab_app/empleo_list.html"

class EmpleoDetailView(DetailView):
    model = Empleos
    template_name = "blog_sab_app/empleo_detail.html"

class EmpleoCreateView(CreateView):
    model = Empleos
    success_url = reverse_lazy('blog_sab_app:empleo-list')
    fields = ['empresa', 'periodo', 'puesto']

class EmpleoUpdateView(UpdateView):
    model = Empleos
    success_url = reverse_lazy('blog_sab_app:empleo-list')
    fields = ['empresa', 'periodo', 'puesto']

class EmpleoDeleteView(DeleteView):
    model = Empleos
    success_url = reverse_lazy('blog_sab_app:empleo-list')

#---------------------------------------------------------
#VIAJES

class ViajeListView(ListView):
    model = Viajes
    template_name = "blog_sab_app/viaje_list.html"

class ViajeDetailView(DetailView):
    model = Viajes
    template_name = "blog_sab_app/viaje_detail.html"

class ViajeCreateView(CreateView):
    model = Viajes
    success_url = reverse_lazy('blog_sab_app:viaje-list')
    fields = ['destino', 'nro_vuelo', 'fecha', 'notas']

class ViajeUpdateView(UpdateView):
    model = Viajes
    success_url = reverse_lazy('blog_sab_app:viaje-list')
    fields = ['destino', 'nro_vuelo', 'fecha', 'notas']

class ViajeDeleteView(DeleteView):
    model = Viajes
    success_url = reverse_lazy('blog_sab_app:viaje-list')
