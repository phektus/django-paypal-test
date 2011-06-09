from django.template import Context, RequestContext, loader
from django.http import HttpResponse

from paypal.standard.forms import PayPalPaymentsForm

import random, string

def subscribe(request):
    # What you want the button to do.
    invoice_id = ''.join(random.choice(string.letters+'1234567890') for i in xrange(9))    
    
    paypal_dict = {
        "business": "arbie@sportix.fr",
        "amount": "100.00",
        "item_name": "test payment",
        "invoice": invoice_id,
        "notify_url": "http://www.example.com/your-ipn-location/",
        "return_url": "http://www.example.com/your-return-location/",
        "cancel_return": "http://www.example.com/your-cancel-location/",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    
    t = loader.get_template('payment/index.html')    
    c = RequestContext(request, {
        "form": form,
    })    
    return HttpResponse(t.render(c))


def paypal_return(request):
    t = loader.get_template('payment/return.html')    
    c = RequestContext(request, {})

    return HttpResponse(t.render(c))


def paypal_cancel(request):
    t = loader.get_template('payment/cancel.html')    
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

