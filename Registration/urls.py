from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$',RegisterView.as_view(), name='register'),
    url(r'^$',EventsView, name='events'),
    url(r'^login/',loginview,name='login'),
    url(r'^logout/', admin_logout, name='logout'),
    url(r'^registration-success/', successpage, name='success'),
    url(r'participants/', participant_list, name='participant'),
    url(r'^events/(?P<pk>[0-9]+)/$', EventsDetail.as_view(), name='eventdetail'),
    url(r'participant/(?P<pk>[0-9]+)/$', ParticipantDetail.as_view(), name='participant_detail'),
    url(r'participant/update/(?P<pk>[0-9]+)/$', ParticipantUpdate.as_view(), name='participant_update'),
    url(r'participant/delete/(?P<pk>[0-9]+)/$',Participant_del.as_view(), name='participant_delete'),
    url(r'^participant/update/success$', updatesuccesspage, name='update_success'),
    url(r'^main/settings$', Settings, name='settings')
]
