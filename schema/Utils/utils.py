# utils.py
import os, tempfile, json, hashlib
from google.cloud import storage
import psycopg2
from contextlib import contextmanager
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS, GCS_RAW_BUCKET

# DB connection helper
def get_db_conn():
    return psycopg2.connect(
        host=DB_HOST, 
        port=DB_PORT, 
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASS
    )

@contextmanager
def db_cursor(commit=False):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        yield cur
        if commit:
            conn.commit()
    finally:
        cur.close()
        if commit:
            conn.close()
        else:
            conn.close()

# upload file to GCS, return gs:// URI
def upload_to_gcs(
        local_path, 
        bucket_name, 
        dest_path
):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_path)
    blob.upload_from_filename(local_path)
    
    return f"gs://{bucket_name}/{dest_path}"

# compute sha256
def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

# read JSON safely
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
