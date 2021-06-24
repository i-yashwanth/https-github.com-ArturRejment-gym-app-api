from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/<int:id>/', views.renewMembership, name="renewMembership"),
	path('viewProducts/<int:id>/', views.viewProducts, name='viewProducts')
]