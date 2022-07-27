from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    RegistrationView,
    ProfileView,
    ReturnView,
    QuestionsView,
    MakeAnswerOrderView,
    PhoneView,
    PhoneOrderView,
    PaginatorView,
    CatalogDetailView
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('return/', ReturnView.as_view(), name='return'),
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('make-answer-order/', MakeAnswerOrderView.as_view(), name='make_answer_order'),
    path('phone/', PhoneView.as_view(), name='phone'),
    path('phone-order/', PhoneOrderView.as_view(), name='phone_order'),
    path('', PaginatorView.as_view(), name='base'),
    path('catalog/<str:slug>/', CatalogDetailView.as_view(), name='catalog_detail')
]

