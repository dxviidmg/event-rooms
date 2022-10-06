from rest_framework import permissions

class IsBussinesUser(permissions.BasePermission):
    message = "You are not bussines user"
    
    def has_permission(self, request, view):
        return (request.user.type == 1) or (request.user.is_superuser) 