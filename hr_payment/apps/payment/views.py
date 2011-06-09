from django.template import Context, RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from paypal.standard.forms import PayPalPaymentsForm

import random, string

def subscribe(request):
    # What you want the button to do.
    invoice_id = ''.join(random.choice(string.letters+'1234567890') for i in xrange(9))    
    
    paypal_dict = {
        "business": "arbie@sportix.fr",
        "amount": "1.00",
        "item_name": "test payment",
        "invoice": invoice_id,
        "notify_url": "http://localhost:8000/payment/ipnsecret234299394",
        "return_url": "http://localhost:8000/payment/paypal_return",
        "cancel_return": "http://localhost:8000/payment/paypal_cancel",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    
    t = loader.get_template('payment/index.html')    
    c = RequestContext(request, {
        "form": form,
    })    
    return HttpResponse(t.render(c))

@csrf_exempt
def paypal_return(request):
    t = loader.get_template('payment/return.html')    
    c = RequestContext(request, {})

    return HttpResponse(t.render(c))

@csrf_exempt
def paypal_cancel(request):
    t = loader.get_template('payment/cancel.html')    
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

