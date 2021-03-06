from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from analyze import get_permissions, get_name
from django.conf import settings

from .models import APK,Permission
from .forms import APKForm
from .tasks import convert
import django_rq
queue = django_rq.get_queue('low')
print "yeahhhh", queue

# Create your views here.

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = APKForm(request.POST, request.FILES)
        if form.is_valid():
	    newdoc=APK(apk=request.FILES['apk'],name=request.FILES['apk'].name)
	    newdoc.save()
	    print "woahhh", newdoc.id    
	    p=request.FILES['apk'].name
	    #somefunc().enqueue(newdoc.id,p)
	    k=settings.MEDIA_ROOT+'/apks/'+str(p)
 	    queue.enqueue(convert, newdoc.id, k)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('droid.views.list'))
    else:
        form = APKForm() # A empty, unbound form
   # Load documents for the list page
    documents = APK.objects.all()

    return render(request, 'droid/test.html', {'documents': documents, 'form': form})

def permission(request,apkid):
	apk=APK.objects.get(id=apkid)
	perm=[str(p) for p in apk.permissions.all()]
	return render(request, 'droid/permission.html', {'permissions': enumerate(perm), 'apk': apk})
