"""
Moodle role hierarchy stub.
Roles: guest, user, student, teacher, editingteacher, manager, admin.
Full implementation is MTP-15.
"""
from enum import IntEnum


class RoleLevel(IntEnum):
    GUEST          = 6
    USER           = 5
    STUDENT        = 4
    NON_EDITING_TEACHER = 3
    TEACHER        = 2
    MANAGER        = 1
    ADMIN          = 0


ROLE_SHORTNAMES: dict[str, RoleLevel] = {
    "guest":           RoleLevel.GUEST,
    "user":            RoleLevel.USER,
    "student":         RoleLevel.STUDENT,
    "teacher":         RoleLevel.NON_EDITING_TEACHER,
    "editingteacher":  RoleLevel.TEACHER,
    "manager":         RoleLevel.MANAGER,
    "admin":           RoleLevel.ADMIN,
}
