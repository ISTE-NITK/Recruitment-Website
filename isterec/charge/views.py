from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.forms.formsets import formset_factory
import re

 
from charge.forms import ChargeForm
from charge.forms import QuestionForm, QuestionForm_2
from charge.models import ChargeRecData
from charge.models import Question, Answer

@ensure_csrf_cookie
def home(request):
        if request.method == 'POST':
                form = ChargeForm(request.POST)
                if form.is_valid():
                        request.session['_charge_info_post'] = request.POST
                        request.session.set_expiry(request.session.get_expiry_age())
                        return HttpResponseRedirect('/charge/questions/1')
        else:
                form = ChargeForm()

        data = {'form': form}
        return render_to_response('charge/home.html', data, RequestContext(request))

def questions_1(request):
        if request.session.get('_charge_info_post') is None:
                return HttpResponseRedirect('/charge/success')
        else:
                if request.method == 'POST':
                        form = QuestionForm(request.POST, page = 1)
                        if form.is_valid():
                                request.session['_charge_Q_page_1'] = request.POST
                                return HttpResponseRedirect('/charge/questions/2')
                else:
                        form = QuestionForm( page = 1)

                data = {'form': form}
                return render_to_response('charge/question.html', data, RequestContext(request))

def questions_2(request):
        if request.session.get('_charge_info_post') is None:
                return HttpResponseRedirect('/charge/success')
        else:
                if request.method == 'POST':
                        form = QuestionForm_2(request.POST, page = 2)
                        if form.is_valid():
                                request.session['_charge_Q_page_2'] = request.POST
                                return HttpResponseRedirect('/charge/questions/3')
                else:
                        form = QuestionForm_2(page = 2)

                data = {'form': form}
                return render_to_response('charge/question.html', data, RequestContext(request))

def questions_3(request):
        if request.session.get('_charge_info_post') is None:
                return HttpResponseRedirect('/charge/success')
        else:
                if request.method == 'POST':
                        form = QuestionForm(request.POST, page = 3)
                        if form.is_valid():
                                info_post = request.session.get('_charge_info_post')
                                form_new = ChargeRecData(name=info_post['name'], rollno=info_post['rollno'], email=info_post['email'], mobileno=info_post['mobileno'])
                                form_new.save()
                                info_page_1 = request.session.get('_charge_Q_page_1')
                                info_page_2 = request.session.get('_charge_Q_page_2')
                                i=0
                                for key, data in info_page_1.items():
                                        if re.search(r'\d+', key) is None:
                                                continue 
                                        i = int(re.search(r'\d+', key).group())
                                        if i>=1:
                                                new_answer= Answer(answer=data, question=Question.objects.get(id=i), creator=form_new)
                                                new_answer.save()

                                for key, data in info_page_2.items():
                                        if re.search(r'\d+', key) is None or data == '':
                                                continue 
                                        i = int(re.search(r'\d+', key).group())
                                        if i>=1:
                                                new_answer= Answer(answer=data, question=Question.objects.get(id=i), creator=form_new)
                                                new_answer.save()

                                new_answer= Answer(answer=request.POST['extra_field_15'], question=Question.objects.get(id=15), creator=form_new)
                                new_answer.save()
                                                
                                request.session['_charge_info_success'] = 'success'
                                return HttpResponseRedirect('/charge/success')
                else:
                        form = QuestionForm(page = 3)

                data = {'form': form}
                return render_to_response('charge/question.html', data, RequestContext(request))

def success(request):       
        if request.session.get('_charge_info_success') is None:
                raise Http404("User session expired/Fill form first")
        else:
                del request.session['_charge_info_post']
                del request.session['_charge_Q_page_1']
                del request.session['_charge_Q_page_2']
                del request.session['_charge_info_success']
                return render(request, 'charge/success.html')
