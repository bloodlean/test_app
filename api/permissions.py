from rest_framework.permissions import BasePermission

class EventPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class EventDetailPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True 

        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
            