from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from helloworldapp.models import Poll
from django.template import Context, loader
from .forms import ContactForm
from django.http import Http404
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # template = loader.get_template('base.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
       # raise Http404
        return render(request, '404.html')
    return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def votes(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
def contact(request):
    form =ContactForm(request.POST or None)
    if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipient = ['studentmanik@gmail.com']
            if cc_myself:
                recipient.append(sender)
            from django.core.mail import send_mail

            send_mail(subject, message, sender, recipient)
            return HttpResponseRedirect('/helloworldapp/contact') # Redirect after post
    else:

        # Dynamic initial values.
        form = ContactForm(initial={'sender': 'studentmanik@gmail.com'})
    context={
        'title':'Contact us',
        'form':form,
    }
    return render(request,'polls/contact.html',context)