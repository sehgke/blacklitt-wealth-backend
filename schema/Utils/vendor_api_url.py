# helper to build vendor API url for a config and feed_date (ddmmyyyy)
from Utils.config import VENDOR_API_BASE, VENDOR_API_TOKEN

def build_vendor_api_url(table_cfg, feed_date_str):
    # vendor params: filename, date, section, sub, token
    filename = table_cfg["FILE_NAME"]
    section = table_cfg.get("SECTION", "")
    token = VENDOR_API_TOKEN
    return f"{VENDOR_API_BASE}?filename={filename}&date={feed_date_str}&section={section}&sub=&token={token}"