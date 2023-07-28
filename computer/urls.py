from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name= 'home'),
    # path('computer', views.create_computer, name= 'computer'),
    # path('update/<int:pk>', views.update_computer, name= 'update_computer'),
    # path('delete/<int:pk>', views.delete_computer, name= 'delete_computer'),
    # path('brand', views.create_brand, name= 'brand'),
    # path('generation', views.create_generation, name= 'generation'),
    # path('specification', views.create_specification, name= 'specification'),

    path('', views.HomeView.as_view(), name='home'),
    path('computer', views.CreateComputerView.as_view(), name='computer'),
    path('update/<int:pk>', views.UpdateComputerView.as_view(), name='update_computer'),
    path('delete/<int:pk>', views.DeleteComputerView.as_view(), name='delete_computer'),

    path('brand', views.CreateBrandView.as_view(), name='brand'),
    path('brandlist', views.ListBrandView.as_view(), name='listbrand'),
    path('brand/update/<int:pk>', views.UpdateBrandView.as_view(), name='update_brand'),
    path('brand/delete/<int:pk>', views.DeleteBrandView.as_view(), name='delete_brand'),

    path('generation', views.CreateGenerationView.as_view(), name='generation'),
    path('generationlist', views.ListGenerationView.as_view(), name='listgeneration'),
    path('generation/update/<int:pk>', views.UpdateGenerationView.as_view(), name='update_generation'),
    path('generation/delete/<int:pk>', views.DeleteGenerationView.as_view(), name='delete_generation'),

    path('specification', views.CreateSpecificationView.as_view(), name='specification'),
    path('specificationlist', views.ListSpecificationView.as_view(), name='listspecification'),
    path('specification/update/<int:pk>', views.UpdateSpecificationView.as_view(), name='update_specification'),
    path('specification/delete/<int:pk>', views.DeleteSpecificationView.as_view(), name='specification_brand'),
]