from rest_framework import serializers

# Serializer for Event objects
# Defines the structure and validation rules for event data
class EventSerializer(serializers.Serializer):
    # Unique identifier for the event (used as Firestore document ID)
    event_id = serializers.CharField()
    # Name/title of the event (e.g., "Birthday Party")
    name = serializers.CharField()
    # Date of the event (stored as string; could be ISO format)
    date = serializers.CharField()
    # Location of the event (city, venue, etc.)
    location = serializers.CharField()

# Serializer for Guest objects
# Ensures guest data is properly structured before saving to Firestore
class GuestSerializer(serializers.Serializer):
    # Unique identifier for the guest (used as Firestore document ID)
    guest_id = serializers.CharField()
    # Guest’s full name
    name = serializers.CharField()
    # Guest’s email address (validated as proper email format)
    email = serializers.EmailField()

# Serializer for RSVP objects
# Represents a guest’s response to an event invitation
class RSVPSerializer(serializers.Serializer):
    # ID of the event being responded to
    event_id = serializers.CharField()
    # ID of the guest who is responding
    guest_id = serializers.CharField()
    # RSVP status (e.g., "Yes", "No", "Maybe")
    status = serializers.CharField()
