from django.urls import path
from .views import list_elections, election_detail, vote
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', list_elections, name='list_elections'),
    path('<int:election_id>/', election_detail, name='election_detail'),
    path('vote/<int:candidate_id>/', vote, name='vote'),
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('', RedirectView.as_view(url='/accounts/dashboard/', permanent=False)),  # Redirect root to dashboard
]
