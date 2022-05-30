from django.urls import path
from blog_sab_app import views

app_name='blog_sab_app'
urlpatterns = [
    path('', views.index, name='Home'),
    path('estudios', views.estudios, name='Estudios'),
    path('viajes', views.viajes, name='Viajes'),
    path('empleos', views.empleos, name='Empleos'),

    path('formHTML', views.form_hmtl),
    path('estudio-django-forms', views.estudio_forms_django, name='EstudiosDjangoForms'),
    path('empleo-django-forms', views.empleo_forms_django, name='EmpleosDjangoForms'),
    path('viaje-django-forms', views.viaje_forms_django, name='ViajesDjangoForms'),

    path('search', views.search, name='Search'),

#ESTUDIO
    path('estudio/<int:pk>/update', views.update_estudio, name='UpdateEstudio'),
    path('estudio/<int:pk>/delete', views.delete_estudio, name='DeleteEstudio'),

    path('estudio/add/', views.EstudioCreateView.as_view(), name='estudio-add'),
    path('estudio/<int:pk>/detail', views.EstudioDetailView.as_view(), name='estudio-detail'),
    path('estudio/<int:pk>/update', views.EstudioUpdateView.as_view(), name='estudio-update'),
    path('estudio/<int:pk>/delete', views.EstudioDeleteView.as_view(), name='estudio-delete'),

    path('estudios', views.EstudioListView.as_view(), name='estudio-list'),

#EMPLEO
    path('empleo/<int:pk>/update', views.update_empleo, name='UpdateEmpleo'),
    path('empleo/<int:pk>/delete', views.delete_empleo, name='DeleteEmpleo'),

    path('empleo/add/', views.EmpleoCreateView.as_view(), name='empleo-add'),
    path('empleo/<int:pk>/detail', views.EmpleoDetailView.as_view(), name='empleo-detail'),
    path('empleo/<int:pk>/update', views.EmpleoUpdateView.as_view(), name='empleo-update'),
    path('empleo/<int:pk>/delete', views.EmpleoDeleteView.as_view(), name='empleo-delete'),

    path('empleos', views.EmpleoListView.as_view(), name='empleo-list'),

#VIAJE
    path('viaje/<int:pk>/update', views.update_viaje, name='UpdateViaje'),
    path('viaje/<int:pk>/delete', views.delete_viaje, name='DeleteViaje'),

    path('viaje/add/', views.ViajeCreateView.as_view(), name='viaje-add'),
    path('viaje/<int:pk>/detail', views.ViajeDetailView.as_view(), name='viaje-detail'),
    path('viaje/<int:pk>/update', views.ViajeUpdateView.as_view(), name='viaje-update'),
    path('viaje/<int:pk>/delete', views.ViajeDeleteView.as_view(), name='viaje-delete'),

    path('viaje', views.ViajeListView.as_view(), name='viaje-list'),
]