from django.conf.urls.defaults import patterns, url, include
import hr_payment.apps.payment

urlpatterns = patterns('',
    (r'^payment/subscribe', 'hr_payment.apps.payment.views.subscribe'),
    (r'^payment/ipnsecret234299394/', include('paypal.standard.ipn.urls')),
)
