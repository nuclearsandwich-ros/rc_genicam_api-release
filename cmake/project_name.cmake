# This cmake code sets the variables
#
# - PROJECT_NAME_UPPER
# - PROJECT_NAME_LOWER
# - PROJECT_NAMESPACE

string(TOUPPER "${PROJECT_NAME}" PROJECT_NAME_UPPER)
string(TOLOWER "${PROJECT_NAME}" PROJECT_NAME_LOWER)
set(PROJECT_NAMESPACE "${PROJECT_NAME}")