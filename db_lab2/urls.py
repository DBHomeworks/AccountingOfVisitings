from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showallinfo, name='all_posts'),
    url(r'^Accounting$', views.accounting, name='Accounting'),
    url(r'^Addvisiting$', views.addvisiting, name='AddVisiting'),
    url(r'^Deletevisiting$', views.deletevisiting, name='DeleteVisiting'),
    url(r'^Showwithfamily$', views.showwithfamily, name='ShowWithFamily'),
    url(r'^DateSearch$', views.datesearch, name='DateSearch'),
    url(r'^ExactlySearch$', views.exactlysearch, name='ExactlySearch'),
    url(r'^BooleanModeSearch$', views.booleanmodesearch, name='BooleanModeSearch'),
    url(r'^GetInfo$', views.accounting, name='get_info'),
    url(r'^EditVisiting$', views.editvisiting, name='get_info'),


    #url(r'^Accounting/GetId$', views.GetId, name='Accounting'),
    ]
