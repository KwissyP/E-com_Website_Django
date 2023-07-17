from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/backoffice/'):
            if not request.user.is_authenticated or request.user.role.value != 'Admin':
                return redirect("home")
        
        return self.get_response(request)