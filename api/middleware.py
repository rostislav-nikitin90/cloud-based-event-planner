from firebase_admin import auth
from django.http import JsonResponse

def firebase_auth_middleware(get_response):
    # This function wraps the request/response cycle
    # It allows us to intercept each incoming request before it reaches the view
    def middleware(request):
        # Extract the Firebase ID token from the "Authorization" header
        # This token is sent by the client (curl, frontend, etc.) to prove identity
        id_token = request.headers.get("Authorization")
        if id_token:
            try:
                # Verify the token using Firebase Admin SDK
                # This checks signature, expiration, and validity
                decoded_token = auth.verify_id_token(id_token)

                # Attach decoded user info to the request object
                # This makes user claims available in views (e.g., UID, email)
                request.firebase_user = decoded_token
                
                # Example fields you can access later in views:
                # decoded_token['uid']        -> Firebase user unique ID
                # decoded_token.get('email')  -> User’s email if available
                # decoded_token.get('name')   -> User’s display name if set

            except Exception as e:
                # If verification fails (invalid, expired, malformed token),
                # return a 401 Unauthorized response with error details
                return JsonResponse({"error": f"Invalid token: {str(e)}"}, status=401)
        
        # If no token is provided, or after successful verification,
        # continue processing the request by passing it to the next middleware/view
        return get_response(request)
    
    # Return the middleware function so Django can use it in the request pipeline
    return middleware


