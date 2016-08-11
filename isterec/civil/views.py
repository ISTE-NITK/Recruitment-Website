from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.forms.formsets import formset_factory
from django.core.mail import send_mail
import re

 
from civil.forms import CivilForm
from civil.forms import QuestionForm
from civil.models import CivilRecData
from civil.models import Question, Answer

@ensure_csrf_cookie
def home(request):
        if request.method == 'POST':
                form = CivilForm(request.POST)
                if form.is_valid():
                        request.session['_civil_info_post'] = request.POST
                        request.session.set_expiry(request.session.get_expiry_age())
                        return HttpResponseRedirect('/civil/questions/1')
        else:
                form = CivilForm()

        data = {'form': form}
        return render(request, 'civil/home.html', data)

def questions_1(request):
        if request.session.get('_civil_info_post') is None:
                return HttpResponseRedirect('/civil/success')
        else:
                if request.method == 'POST':
                        form = QuestionForm(request.POST, page = 1)
                        if form.is_valid():
                                info_post = request.session.get('_civil_info_post')
                                form_new = CivilRecData(name=info_post['name'], rollno=info_post['rollno'], email=info_post['email'], mobileno=info_post['mobileno'])
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

                                request.session['_civil_info_success'] = 'success'
                                return HttpResponseRedirect('/civil/success')
                else:
                        form = QuestionForm(page = 1)

                data = {'form': form}
                return render(request, 'civil/question.html', data)

def success(request):       
        if request.session.get('_civil_info_success') is None:
                raise Http404("User session expired/Fill form first")
        else:
                info_post = request.session.get('_civil_info_post')
                send_mail('ISTE NITK Recruitments 2016','Holla!\n\nThank You for filling up the recuitment form. We have recieved your submission. We look forward to meeting you in the interaction.\n\nIf you haven\'t applied then please report back to us.\n\nSee you soon! :)\n\nTeam ISTE-NITK','istenitkchapter@gmail.com',[info_post['email']],fail_silently=False,)
                del request.session['_civil_info_post']
                del request.session['_civil_info_success']
                return render(request, 'civil/success.html')
