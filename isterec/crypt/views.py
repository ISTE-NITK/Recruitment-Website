from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie

 
from crypt.forms import CryptForm
from crypt.forms import CryptFileForm
from crypt.models import CryptRecData
from crypt.models import File

@ensure_csrf_cookie
def home(request):
        if request.method == 'POST':
                form = CryptForm(request.POST)
                if form.is_valid():
                        request.session['_crypt_info_post'] = request.POST
                        request.session.set_expiry(request.session.get_expiry_age())
                        return HttpResponseRedirect('/crypt/upload')
        else:
                form = CryptForm()

        data = {'form': form}
        return render_to_response('crypt/home.html', data, RequestContext(request))

def upload(request):
        if request.session.get('_crypt_info_success') is not None:
                return HttpResponseRedirect('/crypt/success')
        elif request.session.get('_crypt_info_post') is None:
                return HttpResponseRedirect('/crypt/success')
        else:
                if request.method == 'POST':
                        if request.FILES == None:
                                raise Http404("No files uploaded")
                        old_post = request.session.get('_crypt_info_post')
                        form_new = CryptRecData(name=old_post['name'], rollno=old_post['rollno'], email=old_post['email'], mobileno=old_post['mobileno'], body=old_post['body'])
                        form_new.save()
                        for newfile in request.FILES:
                                addfile = File(file = request.FILES[newfile], creator=form_new)
                                addfile.save()
                        request.session['_crypt_info_success'] = 'success'
                        return HttpResponseRedirect('/')
                else:
                        form = CryptFileForm()

                data = {'form': form}
                return render_to_response('crypt/upload.html', data, RequestContext(request))

def success(request):
        
        if request.session.get('_crypt_info_success') is None:
                raise Http404("User session expired/Fill form first")
        else:
                del request.session['_crypt_info_post']
                del request.session['_crypt_info_post_check']
                del request.session['_crypt_info_success']
                return render(request, 'crypt/success.html')
