from rest_framework import permissions


class IsTeacherOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        is_teacher = hasattr(
            request.user, 'role') and request.user.role == 'teacher'
        is_admin = request.user.is_superuser or request.user.is_staff

        return request.user and request.user.is_authenticated and (is_teacher or is_admin)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.teacher == request.user or request.user.is_superuser


def is_teacher_or_admin(user):
    return user.is_authenticated and (user.role == 'teacher' or user.is_superuser)
