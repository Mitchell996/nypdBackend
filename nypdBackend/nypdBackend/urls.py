from api import views
from django.urls import include, path


urlpatterns = [
    path('conviction/', views.CreateConviction.as_view()),
    #path('csv/', view.getCSV.as_view()),
   # path('/', include('client.urls')),
]

