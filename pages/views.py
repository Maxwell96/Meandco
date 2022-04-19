from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import Page
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect
from .forms import ContactForm
# We are using functional based views 

# render is a special django function that creates a shortcut for communicating with the web browser
# It returns the appropriately formatted response without you having to code the intermediate steps
# We are returning the original request object from the browser and the name of our site template
def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    pg = get_object_or_404(Page, permalink=pagename)
    context ={
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                      connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(),
    'submitted': submitted})
