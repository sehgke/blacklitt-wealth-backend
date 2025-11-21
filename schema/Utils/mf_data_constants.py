"""
Constants for mutual fund data schemas and tables.
"""

# Schema Names
SCHEMA_MASTER = "master"
SCHEMA_STAGING = "staging"
SCHEMA_HISTORICAL = "historical"
SCHEMA_AUDIT = "audit"
SCHEMA_AUX = "aux"
SCHEMA_ANALYTICS = "analytics"

# List of all schemas
ALL_SCHEMAS = [
    SCHEMA_MASTER,
    SCHEMA_STAGING,
    SCHEMA_HISTORICAL,
    SCHEMA_AUDIT,
    SCHEMA_AUX,
    SCHEMA_ANALYTICS,
]

# Section Types from Vendor Data
SECTION_MASTER = "MFMaster"
SECTION_PORTFOLIO = "MFPortfolio"
SECTION_ADDITIONAL = "MFOther"

# STAGE Table Suffix
STAGE_SUFFIX = "stage"
