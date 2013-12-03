from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext
from tutorium.freezer.models import *
from tutorium.freezer.forms import RecruitForm
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def Recruit(request):
    form = RecruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        email = form.cleaned_data['email']
        send_mail('Get started on TutoriumUK', 'You have successfully registered','tutoriumUK@gmail.com', [email], fail_silently=False)

    tutor_list = tutor.objects.all().order_by('firstname')

    if tutor_list:
        return render_to_response('person.html', {'tutor_list': tutor_list, 'form': form},context_instance=RequestContext(request))
    else:
        return HttpResponse("<div>There is nothing</div>")


#def register

"""
    if request.method  == 'POST':
        data = request.POST
        t = tutor(
            firstname = data['firstname'],
            lastname = data['lastname'],
            email = data['email']
            #phone = data['phone'],
            #university = data['university'],
            #degree = data['degree'],
            )
        t.save()
    tutor_list = tutor.objects.all().order_by('firstname')
    if tutor_list:
        return render_to_response('person.html', {'tutor_list': tutor_list},context_instance=RequestContext(request))
    else:
        return HttpResponse("<div>There is nothing</div>")


def contents(request):
	sample_list = Sample.objects.all().order_by('-date')
#	output = ','.join([s.label for s in sample_list])
	return render_to_response('contents.html', {'sample_list': sample_list})

def person(request):
    if request.method  == 'POST':
        data = request.POST
        p = Person(
            firstname = data['firstname'],
            lastname = data['lastname'],
            email = data['email']
            )
        p.save()
    person_list = Person.objects.all().order_by('lastname')
    return render_to_response('person.html', {'person_list': person_list},context_instance=RequestContext(request))



def strain(request):
    if request.method  == 'POST':
        data = request.POST
        s = Strain(
            name = data['name'],
            mutation = data['mutation'],
            species = Species.objects.get(id=data['species_id'])
            )
        s.save()
    strain_list = Strain.objects.all().order_by('name')
    species_list = Species.objects.all().order_by('name')
    return render_to_response('strain.html', {'strain_list': strain_list, 'species_list': species_list})

def sample(request):
    if request.method  == 'POST':
        data = request.POST
        s = Sample(
            label = data['label'],
            date = data['date'],
            strain = Strain.objects.get(id=data['strain_id']),
            person = Person.objects.get(id=data['person_id']),
            notes = data['notes']
            )
        s.save()
    sample_list = Sample.objects.all().order_by('label')
    strain_list = Strain.objects.all().order_by('name')
    person_list = Person.objects.all().order_by('lastname')
    return render_to_response('sample.html', {'sample_list': sample_list, 'strain_list': strain_list, 'person_list': person_list})
"""
