from . import views
from django.urls import path, include # New
from django.views.generic import TemplateView # New
from django.contrib.auth import views as auth_views
#from store.views import ProductListView

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),

	#path('', ProductListView.as_view(),name='store'),

	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('login/', views.login, name="login"),

	#path('', TemplateView.as_view(template_name="store/login")), # New
    path('accounts/', include('allauth.urls')), # New
	#Adding social auth path
    path('social-auth/', include('social_django.urls', namespace="social")),

    #path("", views.home, name="store"),
    #path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

	#path('registration/', include('social_django.urls',namespace = “social”)),

	path("qr_mobile/<mobile>/<amount>/", views.get_qr, name="qr"),
	path("qr_nid/<nid>/<amount>/", views.get_qr, name="qr"),
	#path("upload/", views.upload, name="upload"),
	path('index/', views.image_upload_view, name="index"),
	#path("promo/")


]