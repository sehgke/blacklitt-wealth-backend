# ---- Audit columns config: applied only to master tables (not staging)
from schema_types import FieldSchema

AUDIT_COLUMNS: dict[str, FieldSchema] = {
    "updated_at": {
        "type": "TIMESTAMP", 
        "default": "now()", 
        "description": "Row last updated timestamp"},
    "active_flag": {
        "type": "BOOLEAN", 
        "default": "TRUE", 
        "description": "Soft-delete flag"
    }
}