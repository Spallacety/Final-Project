from rest_framework import permissions

class IsOnwerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      if obj.employee.user == request.user:
        if request.method == 'DELETE':
          return True
      return False

class IsSaleOnwerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      if obj.sale.employee.user == request.user:
        if request.method == 'DELETE':
          return True
        else:
          return False
      return False