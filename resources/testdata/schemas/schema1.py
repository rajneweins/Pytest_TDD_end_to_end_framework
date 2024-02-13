import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("APPLICATION", pa.string(), False),
        ("HOSTNAME", pa.string(), False),
        ("VERSION", pa.string(), False),
        ("INGESTION_TIME", pa.timestamp('ns'), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False)
    ]
)
data = [
    ("HONEYWELL1", "App1", "HostA", "1.0.0", datetime(2023, 7, 10, 12, 34, 56), datetime(2023, 7, 1, 10, 0, 0)),
    ("HONEYWELL1", "App2", "HostB", "2.1.0", datetime(2050, 7, 10, 14, 30, 15), datetime(2050, 7, 2, 11, 0, 0)),
]
