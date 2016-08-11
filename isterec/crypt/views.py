from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
import re

 
from crypt.forms import CryptForm
from crypt.forms import CryptFileForm, QuestionForm
from crypt.models import CryptRecData
from crypt.models import File, Question, Answer

@ensure_csrf_cookie
def home(request):
        if request.method == 'POST':
                form = CryptForm(request.POST)
                if form.is_valid():
                        request.session['_crypt_info_post'] = request.POST
                        request.session.set_expiry(request.session.get_expiry_age())
                        return HttpResponseRedirect('/crypt/questions/1')
        else:
                form = CryptForm()

        data = {'form': form}
        return render(request, 'crypt/home.html', data)

def questions_1(request):
        if request.session.get('_crypt_info_post') is None:
                return HttpResponseRedirect('/crypt/success')
        else:
                if request.method == 'POST':
                        form = QuestionForm(request.POST, page = 1)
                        if form.is_valid():
                                info_post = request.session.get('_crypt_info_post')
                                form_new = CryptRecData(name=info_post['name'], rollno=info_post['rollno'], email=info_post['email'], mobileno=info_post['mobileno'])
                                form_new.save()
                                info_page_1 = request.POST
                                i=0
                                for key, data in info_page_1.items():
                                        if re.search(r'\d+', key) is None:
                                                continue 
                                        i = int(re.search(r'\d+', key).group())
                                        if i>=1:
                                                new_answer= Answer(answer=data, question=Question.objects.get(id=i), creator=form_new)
                                                new_answer.save()

                                request.session['_crypt_form_id'] = form_new.id
                                return HttpResponseRedirect('/crypt/upload')
                else:
                        form = QuestionForm(page = 1)

                data = {'form': form}
                return render(request, 'crypt/question.html', data)
				

def upload(request):
        if request.session.get('_crypt_info_success') is not None:
                return HttpResponseRedirect('/crypt/success')
        elif request.session.get('_crypt_form_id') is None:
                return HttpResponseRedirect('/crypt/success')
        else:
                if request.method == 'POST':
                        if not request.FILES:
                                request.session['_crypt_info_success'] = 'success'
                                return HttpResponseRedirect('/crypt/success')
                        for newfile in request.FILES:
                                addfile = File(creator=CryptRecData.objects.get(id=request.session.get('_crypt_form_id')),file = request.FILES[newfile])
                                addfile.save()
                        request.session['_crypt_info_success'] = 'success'
                        return HttpResponseRedirect('/')
                else:
                        form = CryptFileForm()

                data = {'form': form}
                return render(request, 'crypt/upload.html', data)

def success(request):
        
        if request.session.get('_crypt_info_success') is None:
                raise Http404("User session expired/Fill form first")
        else:
                info_post = request.session.get('_crypt_info_post')
                send_mail('ISTE NITK Recruitments','We have recieved your submission. If you feel this is an error then please report it.','shivshnkr420@gmail.com',[info_post['email']],fail_silently=False,)
                del request.session['_crypt_info_post']
                del request.session['_crypt_form_id']
                del request.session['_crypt_info_success']
                return render(request, 'crypt/success.html')
