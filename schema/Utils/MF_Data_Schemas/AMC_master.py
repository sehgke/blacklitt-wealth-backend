"""
AMC Master schema field definitions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from mf_data_constants import SCHEMA_MASTER, SECTION_MASTER
from schema_types import FieldSchema, TableConfig

SCHEMA: dict[str, FieldSchema] = {
    "amc_code": {
        "srno": 1,
        "PrimaryKey": True,
        "field_type": "Integer",
        "description": "Accord AMC Code is unique for each company"
    },
    "amc": {
        "srno": 2,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC's Name"
    },
    "fund": {
        "srno": 3,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "Mutual Fund's Name"
    },
    "srno": {
        "srno": 4,
        "PrimaryKey": False,
        "field_type": "Integer",
        "description": "Srno. 1 for 'Registered Office' and 2 for 'Corporate Office'"
    },
    "office_type": {
        "srno": 5,
        "PrimaryKey": False,
        "field_type": "Varchar(60)",
        "description": "AMC Office Type (Registered or Corporate)"
    },
    "add1": {
        "srno": 6,
        "PrimaryKey": False,
        "field_type": "nVarchar(max)",
        "description": "AMC Address1"
    },
    "add2": {
        "srno": 7,
        "PrimaryKey": False,
        "field_type": "nVarchar(max)",
        "description": "AMC Address2"
    },
    "add3": {
        "srno": 8,
        "PrimaryKey": False,
        "field_type": "nVarchar(max)",
        "description": "AMC Address3"
    },
    "email": {
        "srno": 9,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC Email ID"
    },
    "phone": {
        "srno": 10,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC Phone Number"
    },
    "fax": {
        "srno": 11,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC FAX Number"
    },
    "website": {
        "srno": 12,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC Website"
    },
    "setup_date": {
        "srno": 13,
        "PrimaryKey": False,
        "field_type": "Datetime",
        "description": "Mutual Fund Set-up Date"
    },
    "mf_type": {
        "srno": 14,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "Type of Mutual Fund Company"
    },
    "trustee_name": {
        "srno": 15,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "AMC Trustee Name"
    },
    "sponsor_name": {
        "srno": 16,
        "PrimaryKey": False,
        "field_type": "nVarchar(max)",
        "description": "AMC Sponsor Name"
    },
    "amc_inc_date": {
        "srno": 17,
        "PrimaryKey": False,
        "field_type": "Datetime",
        "description": "AMC Inception date"
    },
    "s_name": {
        "srno": 18,
        "PrimaryKey": False,
        "field_type": "Varchar(50)",
        "description": "Short name"
    },
    "amc_symbol": {
        "srno": 19,
        "PrimaryKey": False,
        "field_type": "Varchar(50)",
        "description": "AMC symbol"
    },
    "city": {
        "srno": 20,
        "PrimaryKey": False,
        "field_type": "Varchar(255)",
        "description": "City"
    },
    "rtamccode": {
        "srno": 21,
        "PrimaryKey": False,
        "field_type": "Varchar(100)",
        "description": "RT AMC Code - Ignore this field."
    },
    "rtamccode_1": {
        "srno": 22,
        "PrimaryKey": False,
        "field_type": "Varchar(100)",
        "description": "RT AMC Code"
    },
    "flag": {
        "srno": 23,
        "PrimaryKey": False,
        "field_type": "Varchar(1)",
        "description": "Updation Flag"
    },    
}

AMC_MASTER_CONFIG: TableConfig = {
    "TABLE_NAME": "amc_mst",    
    "SCHEMA_NAME": SCHEMA_MASTER,
    "TABLE_DESCRIPTION": "This table contains Information about all Asset Management Companies.",
    "FILE_NAME": "Amc_mst_new",
    "SECTION": SECTION_MASTER,
    "SCHEMA": SCHEMA,
}
