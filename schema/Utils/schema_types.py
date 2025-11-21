"""
Common type definitions for schema configurations.
"""
from typing import TypedDict, Literal
from mf_data_constants import ALL_SCHEMAS

class FieldSchema(TypedDict, total=True):
    """
    Schema definition for a single field.
    
    All fields are required. Type checker will flag missing fields.
    """
    srno: int
    PrimaryKey: bool
    field_type: str
    description: str


class TableConfig(TypedDict, total=True):
    """
    Configuration for a table including its schema and metadata.
    
    All fields are required. Type checker will flag missing fields.
    SCHEMA_NAME must be one of: master, staging, historical, audit, aux, analytics
    """
    TABLE_DESCRIPTION: str
    TABLE_NAME: str
    SCHEMA_NAME: str
    SCHEMA: dict[str, FieldSchema]
    API: str

TYPE_MAP: dict[str, str] = {  # maps generic types to DB-specific types
    "int":"INTEGER",
    "integer":"INTEGER",
    "bigint":"BIGINT",
    "float":"FLOAT",
    "double":"DOUBLE PRECISION",
    "numeric":"NUMERIC",
    "decimal":"NUMERIC",
    "text":"TEXT",
    "string":"TEXT",
    "nvarchar(max)": "TEXT",
    "varchar":"VARCHAR(255)",
    "timestamp":"TIMESTAMP",
    "date":"DATE",
    "Datetime": "TIMESTAMP",
    "boolean":"BOOLEAN",
    "json":"JSONB",
    "jsonb":"JSONB"
}