import stripe

from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html "


class CancelView(TemplateView):
    template_name = "cancel.html "


class MainPageView(TemplateView):
    template_name = 'main.html'


class ItemMainPageView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=kwargs.get('pk'))
        context = super(ItemMainPageView, self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddToOrderView(View):
    def get(self, request, item_id):
        order, _ = Order.objects.get_or_create(ip=get_ip_address(request))
        order.items.add(item_id)
        return JsonResponse({
            'id': item_id
        })


class OrderPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        full_price = 0
        items_name = ''
        orders = Order.objects.filter(pk=1)[0].items.all()
        for item in orders:
            full_price += item.price
            items_name += '|' + item.name + '| '
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context.update({
            "order": orders,
            "full_price": full_price,
            "items_name": items_name,
            "order_id": Order.objects.get(id=1).id,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class CreateCheckoutSessionOrderView(View):
    def post(self, request, *args, **kwargs):
        full_price = 0
        items_name = ''
        orders = Order.objects.filter(pk=1)[0].items.all()
        for item in orders:
            full_price += item.price
            items_name += '|' + item.name + '| '
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': full_price,
                        'product_data': {
                            'name': items_name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            item_id = self.kwargs["pk"]
            item = Item.objects.get(id=item_id)
            intent = stripe.PaymentIntent.create(
                amount=item.price,
                currency='usd'
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e) })


