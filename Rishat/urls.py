from django.contrib import admin
from django.urls import path
from polls.views import (
    CreateCheckoutSessionView,
    ItemMainPageView,
    SuccessView,
    CancelView,
    MainPageView,
    AddToOrderView,
    OrderPageView,
    CreateCheckoutSessionOrderView,
    StripeIntentView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view, name='create-payment-intent'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<pk>/', ItemMainPageView.as_view(), name='item-page'),
    path('', MainPageView.as_view(), name='items-page'),
    path('add-to-order/<int:item_id>/', AddToOrderView.as_view(), name='add_to_order'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('order/', OrderPageView.as_view(), name='order-page'),
    path('order/<pk>/', CreateCheckoutSessionOrderView.as_view(), name='buy_order'),
]
