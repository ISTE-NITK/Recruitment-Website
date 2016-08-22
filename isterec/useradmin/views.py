from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from crypt.models import CryptRecData
from charge.models import ChargeRecData
from credit.models import CreditRecData
from chronicle.models import ChronicleRecData
from create.models import CreateRecData
from clutch.models import ClutchRecData
from civil.models import CivilRecData
from django.db.models import Q
import re

from useradmin.forms import CryptScoreForm, CryptReviewForm
from useradmin.forms import ChargeScoreForm, ChargeReviewForm
from useradmin.forms import ClutchScoreForm, ClutchReviewForm
from useradmin.forms import CreditScoreForm, CreditReviewForm
from useradmin.forms import ChronicleScoreForm, ChronicleReviewForm
from useradmin.forms import CreateScoreForm, CreateReviewForm
from useradmin.forms import CivilScoreForm, CivilReviewForm
from useradmin.forms import RegistrationForm

@login_required(login_url='/admin/login/')
def home(request):
    return render(request, 'useradmin/home.html')

@login_required(login_url='/admin/login/')
def index(request, **kwargs):
    return render(request, 'useradmin/search.html', {'signame' :kwargs.pop('sig_name')})


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 


def get_query(query_string, search_fields):
    
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@login_required(login_url='/admin/login/')
def search(request, **kwargs):
    query_string = ''
    query_sort = ''
    sig_name = ''
    found_entries = None
    if ('q' in request.GET):
        query_string = request.GET['q'].strip()
        if query_string == '' :
            query_string = '1'
        query_sort = request.GET['sort']
        sig_name=kwargs.pop('sig_name')
        entry_query = get_query(query_string, ['rollno', 'name','mobileno','email',])
        
        if sig_name == 'crypt':
            found_entries = CryptRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'charge':
            found_entries = ChargeRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'credit':
            found_entries = CreditRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'chronicle':
            found_entries = ChronicleRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'create':
            found_entries = CreateRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'civil':
            found_entries = CivilRecData.objects.filter(entry_query).order_by(query_sort)
        elif sig_name == 'clutch':
            found_entries = ClutchRecData.objects.filter(entry_query).order_by(query_sort)
            
    return render(request, 'useradmin/results.html', { 'query_string': query_string, 'results': found_entries, 'signame': sig_name })

@login_required(login_url='/admin/login/')
def selected(request, **kwargs):
    found_entries = None
    query_sort = ''
    if ('sort' in request.GET):
        sig_name=kwargs.pop('sig_name')
        query_sort = request.GET['sort']
        if sig_name == 'crypt':
            found_entries = CryptRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'charge':
            found_entries = ChargeRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'credit':
            found_entries = CreditRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'chronicle':
            found_entries = ChronicleRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'create':
            found_entries = CreateRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'civil':
            found_entries = CivilRecData.objects.filter(is_selected=True).order_by(query_sort)
        elif sig_name == 'clutch':
            found_entries = ClutchRecData.objects.filter(is_selected=True).order_by(query_sort)
            
    return render(request, 'useradmin/selectedresults.html', { 'results': found_entries, 'signame': sig_name })

@login_required(login_url='/admin/login/')						  
def detailreply(request, **kwargs):
    sig_name = kwargs.pop('sig_name')
    query_id = kwargs.pop('pk')
    found_entry = None
    confirmation = ''

    if sig_name == 'crypt':
        found_entry = CryptRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = CryptReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CryptReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = CryptScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CryptScoreForm(instance=found_entry)

            
    elif sig_name == 'charge':
        found_entry = ChargeRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = ChargeReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ChargeReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = ChargeScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ChargeScoreForm(instance=found_entry)

                
    elif sig_name == 'credit':
        found_entry = CreditRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = CreditReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CreditReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = CreditScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CreditScoreForm(instance=found_entry)

            
    elif sig_name == 'chronicle':
        found_entry = ChronicleRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = ChronicleReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ChronicleReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = ChronicleScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ChronicleScoreForm(instance=found_entry)

            
    elif sig_name == 'create':
        found_entry = CreateRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = CreateReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CreateReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = CreateScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CreateScoreForm(instance=found_entry)

            
    elif sig_name == 'civil':
        found_entry = CivilRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = CivilReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CivilReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = CivilScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = CivilScoreForm(instance=found_entry)

            
    elif sig_name == 'clutch':
        found_entry = ClutchRecData.objects.get(id = query_id)
        if found_entry.reviewer_1 == '':
            if request.method == 'POST':
                form = ClutchReviewForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ClutchReviewForm(instance=found_entry)
        else:
            if request.method == 'POST':
                form = ClutchScoreForm(request.POST, instance=found_entry)
                if(form.is_valid()):
                    form.save()
                    confirmation = 'Changes Saved'
            else:
                form = ClutchScoreForm(instance=found_entry)

    
    data = {'form': form, 'result': found_entry, 'signame': sig_name, 'saveconf': confirmation }
    return render(request, 'useradmin/detail.html', data)

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['firstname'],
            last_name=form.cleaned_data['lastname'],
            is_active=False,
            )
            return HttpResponseRedirect('success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'useradmin/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'useradmin/success.html',
    )
