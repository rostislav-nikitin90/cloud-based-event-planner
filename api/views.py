from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EventSerializer, GuestSerializer, RSVPSerializer
from django.conf import settings

# Firestore database reference (configured in settings.py)
db = settings.DB

# --- Events ---
@api_view(['POST'])
def add_event(request):
    # Check if Firebase authentication middleware attached user info
    user_info = getattr(request, "firebase_user", None)
    if not user_info:
        # Reject request if no valid ID token was provided
        return Response({"error": "Authentication required"}, status=401)

    # Validate incoming JSON against EventSerializer
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Save event data in Firestore under "events" collection
        db.collection("events").document(data['event_id']).set(data)
        return Response({"message": "Event added", "created_by": user_info['uid']})
    # Return validation errors if serializer fails
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_events(request):
    # Access Firebase user info if available
    user_info = getattr(request, "firebase_user", None)
    if user_info:
        # Print claims from ID token for debugging
        print("Authenticated UID:", user_info['uid'])
        print("Email:", user_info.get('email'))
    else:
        print("No Firebase user attached")

    # Query all documents in "events" collection
    events = db.collection("events").stream()
    # Convert Firestore documents into list of dicts
    results = [{e.id: e.to_dict()} for e in events]
    return Response(results)

@api_view(['PUT'])
def update_event(request, event_id):
    # Require authentication
    user_info = getattr(request, "firebase_user", None)
    if not user_info:
        return Response({"error": "Authentication required"}, status=401)

    # Update event document with new data
    db.collection("events").document(event_id).update(request.data)
    return Response({"message": "Event updated", "updated_by": user_info['uid']})

@api_view(['DELETE'])
def delete_event(request, event_id):
    # Require authentication
    user_info = getattr(request, "firebase_user", None)
    if not user_info:
        return Response({"error": "Authentication required"}, status=401)

    # Delete event document from Firestore
    db.collection("events").document(event_id).delete()
    return Response({"message": "Event deleted", "deleted_by": user_info['uid']})

# --- Guests ---
@api_view(['POST'])
def add_guest(request):
    # Validate guest data
    serializer = GuestSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Save guest in "guests" collection
        db.collection("guests").document(data['guest_id']).set(data)
        return Response({"message": "Guest added"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_guests(request):
    # Retrieve all guests from Firestore
    guests = db.collection("guests").stream()
    results = [{g.id: g.to_dict()} for g in guests]
    return Response(results)

# --- RSVPs ---
@api_view(['POST'])
def rsvp(request):
    # Validate RSVP data
    serializer = RSVPSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Add RSVP to "rsvps" collection (auto-generated ID)
        db.collection("rsvps").add(data)
        return Response({"message": "RSVP recorded"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_rsvps(request):
    # Retrieve all RSVPs from Firestore
    rsvps = db.collection("rsvps").stream()
    results = [{r.id: r.to_dict()} for r in rsvps]
    return Response(results)
