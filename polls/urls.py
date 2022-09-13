# from django.urls import path
# from .views import (
#     CreateCheckoutSessionView,
#     ItemMainPageView,
#     SuccessView,
#     CancelView,
#     MainPageView,
#     AddToOrderView
# )
#
# urlpatterns = [
#     path('cancel/', CancelView.as_view(), name='cancel'),
#     path('success/', SuccessView.as_view(), name='success'),
#     path('item/<pk>/', ItemMainPageView.as_view(), name='item-page'),
#     path('', MainPageView.as_view(), name='items-page'),
#     path('add-to-order/<item_id:int>/', AddToOrderView.as_view(), name='add_to_order'),
#     path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy')
# ]
