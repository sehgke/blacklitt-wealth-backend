-- 1. AMC Master (Amc_mst_new / Amc_mst)
CREATE TABLE IF NOT EXISTS amc_mst (
  amc_code INTEGER PRIMARY KEY,
  amc VARCHAR(255),
  fund VARCHAR(255),
  srno INTEGER,
  office_type VARCHAR(60),
  add1 TEXT,
  add2 TEXT,
  add3 TEXT,
  email VARCHAR(255),
  phone VARCHAR(255),
  fax VARCHAR(255),
  website VARCHAR(255),
  setup_date TIMESTAMP,
  mf_type VARCHAR(255),
  trustee_name VARCHAR(255),
  sponsor_name TEXT,
  amc_inc_date TIMESTAMP,
  s_name VARCHAR(50),
  amc_symbol VARCHAR(50),
  city VARCHAR(255),
  rtamccode VARCHAR(100),
  rtamccode_1 VARCHAR(100),
  flag VARCHAR(1), -- A-Add, O-Open, D-Delete
  /*raw_json JSONB,*/
  feed_date DATE,
  updated_at TIMESTAMP DEFAULT now(),
  active_flag BOOLEAN DEFAULT TRUE
);
COMMENT ON TABLE amc_mst IS 'This table contains Information about all Asset Management Companies.; source: Amc_mst_new';
COMMENT ON COLUMN amc_mst.amc_code IS 'Primary key: Accord Fintech AMC code';
COMMENT ON COLUMN amc_mst.flag IS 'Vendor update flag (A/O/D)';
-- COMMENT ON COLUMN amc_mst.raw_json IS 'Original vendor JSON row';
