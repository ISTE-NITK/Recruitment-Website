from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
 
from crypt.forms import UploadFileForm
from crypt.models import UploadFile
from django.utils.timezone import datetime

def index(request):
        return render(request, 'crypt/home.html')

def home(request):
        if request.method == 'POST':
                form = UploadFileForm(request.POST, request.FILES)
                if form.is_valid():
                        new_record = UploadFile(name=request.POST['name'],rollno=request.POST['rollno'],email=request.POST['email'],mobileno=request.POST['mobileno'],body=request.POST['body'],date=datetime.now(), file= request.FILES['file'])
                        new_record.save()
                        return HttpResponseRedirect(reverse('crypt:home'))
        else:
                form = UploadFileForm()

        data = {'form': form}
        return render_to_response('crypt/home.html', data, context_instance=RequestContext(request))
