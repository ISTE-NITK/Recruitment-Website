from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
 
from crypt.forms import UploadFileForm
from crypt.models import UploadFile

def index(request):
        return render(request, 'crypt/home.html')

def home(request):
        if request.method == 'POST':
                form = UploadFileForm(request.POST, request.FILES)
                if form.is_valid():
                        new_record = UploadFile(name=form.cleaned_data['name'],rollno=form.cleaned_data['rollno'],email=form.cleaned_data['email'],mobileno=form.cleaned_data['mobileno'],body=form.cleaned_data['body'], file= request.FILES['file'])
                        new_record.save()
                        return HttpResponseRedirect(reverse('crypt:home'))
        else:
                form = UploadFileForm()

        data = {'form': form}
        return render_to_response('crypt/home.html', data, context_instance=RequestContext(request))
