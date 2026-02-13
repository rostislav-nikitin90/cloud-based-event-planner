from django.urls import path
from . import views

 # URL patterns define the API endpoints for the event planner project
 # Each path maps a specific URL to a corresponding view function in views.py
urlpatterns = [
    # --- Event endpoints ---
    # GET request → fetch all events from Firestore
    path('events/', views.get_events),
    # POST request → add a new event (requires authentication)
    path('events/add/', views.add_event),
    # PUT request → update an existing event by its event_id
    path('events/<str:event_id>/update/', views.update_event),
    # DELETE request → remove an event by its event_id
    path('events/<str:event_id>/delete/', views.delete_event),

    # --- Guest endpoints ---
    # GET request → fetch all guests from Firestore
    path('guests/', views.get_guests),
    # POST request → add a new guest
    path('guests/add/', views.add_guest),

    # --- RSVP endpoints ---
    # GET request → fetch all RSVPs from Firestore
    path('rsvps/', views.get_rsvps),
    # POST request → record a new RSVP for an event
    path('rsvp/', views.rsvp),
]

