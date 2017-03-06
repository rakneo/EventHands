from django import template
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import RegisterDesk, EventList
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
import itertools
import functools

# Create your views here.
decorator = [login_required]


@method_decorator(decorator, name='dispatch')
class RegisterView(CreateView):
    model = RegisterDesk
    fields = ['candidate_name', 'candidate_college', 'candidate_email', 'candidate_contact_no', 'events_enrolling']
    template_name = 'registraton_form.html'



def EventsView(request):
    all_events = EventList.objects.all()
    return render(request, 'events_page.html', {'all_events': all_events})


class EventsDetail(DetailView):
    model = EventList
    template_name = 'events_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventsDetail, self).get_context_data(**kwargs)
        context['registerdesk'] = RegisterDesk.objects.all()
        context['count'] = functools.partial(next, itertools.count(1))
        return context



def loginview(request):
    if request.user.is_authenticated:
        return redirect('events')
    else:
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('register')
    return render(request, 'login_form.html')


def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')


def successpage(request):
    return render(request, 'Register_success_page.html')


def updatesuccesspage(request):
    return render(request, 'update_success.html')


def participant_list(request):

    all_participants = RegisterDesk.objects.all().order_by('candidate_college')
    return render(request, 'Participant_list.html', {'all_participants': all_participants})


class Participant_del(DeleteView):
    model = RegisterDesk
    success_url = reverse_lazy('participant')


@method_decorator(decorator, name='dispatch')
class ParticipantDetail(DetailView):
    model = RegisterDesk
    template_name = 'participant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ParticipantDetail, self).get_context_data()
        context['events'] = EventList.objects.all()

        return context


@method_decorator(decorator, name='dispatch')
class ParticipantUpdate(UpdateView):
    model = RegisterDesk
    fields = ['candidate_name', 'candidate_college', 'candidate_email', 'candidate_contact_no', 'events_enrolling']
    template_name = 'update_form.html'

    def get_success_url(self):
        return reverse_lazy('update_success')








