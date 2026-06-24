"""
Moodle capability system stub.
Capabilities control what authenticated users can do within a context
(system > category > course > module).

Full implementation is MTP-54. This stub lets other modules import and
reference capability constants without breaking during Phase 0.
"""
from enum import StrEnum


class Context(StrEnum):
    SYSTEM   = "system"
    CATEGORY = "category"
    COURSE   = "course"
    MODULE   = "module"
    USER     = "user"
    BLOCK    = "block"


# Subset of the ~500 Moodle capabilities — extend as phases progress
CAPABILITY_VIEW_COURSE      = "moodle/course:view"
CAPABILITY_MANAGE_COURSE    = "moodle/course:update"
CAPABILITY_ENROL_SELF       = "moodle/course:enrolself"
CAPABILITY_MANAGE_USERS     = "moodle/user:update"
CAPABILITY_VIEW_USERS       = "moodle/user:viewdetails"
CAPABILITY_GRADE_ITEMS      = "moodle/grade:edit"
CAPABILITY_VIEW_GRADES      = "moodle/grade:view"
CAPABILITY_SITE_CONFIG      = "moodle/site:config"
