from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^click$', views.click, name='click'),
    url(r'^ShowCompanies$', views.showcompanies, name='ShowCompanies'),
    url(r'^ShowAllInfo$', views.showallinfo, name='ShowAllInfo'),
    url(r'^ShowEmployeeInfo$', views.showemployeeinfo, name='ShowEmployeeInfo'),
    url(r'^ShowWorkPlace$', views.showworkplace, name='ShowWorkPlace'),
    url(r'^Accounting$', views.accounting, name='Accounting'),
    url(r'^Addvisiting$', views.addvisiting, name='AddVisiting'),
    url(r'^Deletevisiting$', views.deletevisiting, name='DeleteVisiting'),
    url(r'^Showwithfamily$', views.showwithfamily, name='ShowWithFamily'),
    url(r'^DateSearch$', views.datesearch, name='DateSearch'),
    url(r'^ExactlySearch$', views.exactlysearch, name='ExactlySearch'),
    url(r'^BooleanModeSearch$', views.booleanmodesearch, name='BooleanModeSearch'),
    url(r'^GetInfo$', views.accounting, name='get_info'),
    url(r'^EditVisiting$', views.editvisiting, name='get_info'),
    url(r'^LoadFromXML$', views.filldb, name='filldb'),
    url(r'^ClearDB$', views.cleardb, name='cleardb'),


    #url(r'^Accounting/GetId$', views.GetId, name='Accounting'),
    ]
