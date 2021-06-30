from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/', views.renewMembership, name="renewMembership"),
	path('createMembership/', views.createMembership, name="createMembership"),
	path('viewMemberships/', views.viewMemberships, name="viewMemberships"),
	path('viewProducts/', views.viewProducts, name='viewProducts'),
	path('createProduct/', views.createProduct, name='createProduct'),
	path('groupTrainings/', views.viewGroupTrainings, name='viewGroupTrainings'),
	path('createGroupTraining/', views.createGroupTraining, name='createGroupTrainings'),
	path('signForTraining/', views.signUpForTraining, name='signForTraining'),
	path('viewAllProducts/', views.viewAllProducts, name='viewAllProducts'),
	path('addProduct/', views.addProduct, name='addProduct'),
	path('deleteProduct/', views.deleteProductFromTheShop, name='deleteProduct'),
	path('viewShops/', views.viewShops, name='viewShops'),
	path('createShop/', views.createShop, name='createShop'),
	path('test', views.test, name='test'),
	path('shop/', views.ShopView.as_view(), name="shop")
]
