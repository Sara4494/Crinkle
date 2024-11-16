from django.conf import settings

def get_cart_session_id(request):
    """
    Helper function to get or create the cart session ID
    """
    cart_session_id = settings.CART_SESSION_ID

   
    if not request.session.session_key:
        request.session.create()

    
    session_id = request.session.get(cart_session_id)
    if not session_id:
    
        session_id = request.session.session_key
        request.session[cart_session_id] = session_id

    return session_id
