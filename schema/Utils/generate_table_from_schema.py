# generate_schema.py
"""
Generate and apply DDL for staging and master tables from a schema JSON.
Usage:
  export DB_PASS=...
  python3 generate_schema.py --schema-file schemas/amc_mst.json --table-key amc_master
This will:
 - create schemas (master, staging) if missing
 - create staging table (no audit cols, no PK constraints required)
 - create master table (apply PK if marked, plus audit columns from config.AUDIT_COLUMNS)
"""
import argparse, json, re
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from MF_Data_Schemas.Schema_list import Table_list
from audit_columns_config import AUDIT_COLUMNS
from mf_data_constants import SCHEMA_STAGING, STAGE_SUFFIX
from schema_types import TYPE_MAP
from utils import db_cursor


def normalize_colname(name):
    # simple normalization to snake_case
    s = re.sub(r'[^0-9a-zA-Z_]', '_', name).strip().lower()
    return re.sub(r'__+', '_', s)

def map_type(ftype):
    if not ftype: return "TEXT"
    t = str(ftype).strip().lower()

    return TYPE_MAP.get(t, t.upper())

def load_schema(schema_file):
    with open(schema_file,'r',encoding='utf-8') as f:
        return json.load(f)

def build_create_table_sql(table_name, schema_name, columns_meta, is_stage=False):
    lines=[]
    pk_cols=[]
    
    for raw_col, meta in columns_meta.items():
        col = normalize_colname(raw_col)
        typ = map_type(meta.get('field_type') or meta.get('type'))
        line = f'  "{col}" {typ}'
        if meta.get('PrimaryKey') or meta.get('primary'):
            pk_cols.append(col)
        lines.append(line)
    
    # append audit cols only if not stage
    if not is_stage:
        for k,v in AUDIT_COLUMNS.items():
            typ = v.get('type')
            default = v.get('default')
            line = f'  "{k}" {typ}'
            if default:
                line += f' DEFAULT {default}'
            lines.append(line)
    
    # build pk clause if any
    body = ",\n".join(lines)
    create = f'CREATE TABLE IF NOT EXISTS {schema_name}."{table_name}" (\n{body}\n'
    if pk_cols and not is_stage:
        pk = ", ".join([f'"{c}"' for c in pk_cols])
        create += f",\nPRIMARY KEY ({pk})\n"
    create += ");"
    
    return create

def apply_sql(sql):
    with db_cursor(commit=True) as cur:
        cur.execute(sql)

def main():
    #Parse Arguments
    p=argparse.ArgumentParser()
    p.add_argument('--table-key', required=True)
    args=p.parse_args()
    
    cfg = Table_list[args.table_key]
    master_schema_name = cfg['SCHEMA_NAME']
    stage_schema_name = SCHEMA_STAGING
    
    # ensure schemas exist
    apply_sql(f'CREATE SCHEMA IF NOT EXISTS {master_schema_name};')
    apply_sql(f'CREATE SCHEMA IF NOT EXISTS {stage_schema_name};')
    
    # build and apply staging
    stage_table = f"{cfg['TABLE_NAME']}_{STAGE_SUFFIX}"
    stage_sql = build_create_table_sql( 
        stage_table, 
        stage_schema_name, 
        cfg['SCHEMA'], 
        is_stage=True
    )

    print("Applying staging DDL...")
    apply_sql(stage_sql)
    print(stage_sql)
    print("Staging done.")

    # build and apply master
    master_sql = build_create_table_sql(
        cfg['TABLE_NAME'], 
        master_schema_name, 
        cfg['SCHEMA'], 
        is_stage=False
    )

    print("Applying master DDL...")
    apply_sql(master_sql)
    print(master_sql)
    print("Master done.")

if __name__ == '__main__':
    main()