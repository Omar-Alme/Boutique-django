from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm



def checkout(request):
    """ A view to return the checkout page """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OQSwkLqAapZR5NVhCwPlwQZ96XcqP5VL2y03oqsxGcAYfQHKinGSI1LcvG2qc5Wb4k1Yq7hBVhbNuJjGRvQBLi900BQCTwXZF',
        'client_secret': 'test client secret',
    }



    return render(request, template, context)


