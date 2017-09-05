from django.conf.urls import url


from . import views
app_name = 'writingmatch'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^handle/$', views.get_name, name = 'handle'),
	url(r'^thanks/$', views.thanks, name = 'thanks')
]