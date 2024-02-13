import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("READING_TIMESTAMP", pa.timestamp('ns'), False),
        ("COLLECTION_TIMESTAMP", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("READING_TYPE_ID", pa.int64(), False),
        ("READING_VALUE", pa.float64(), False),
        ("QUALITY_FLAGS", pa.int64(), False),
        ("INGESTION_DATE", pa.date64(), False)
    ]
)
data = [
    ("24a36712f1c", datetime(2023, 8, 7, 12, 0, 0), datetime(2023, 8, 7, 12, 0, 0), datetime(2023, 8, 7, 12, 0, 0),
     "Device001", 54, 123.45, 1, datetime(2023, 8, 7)),
    ("24a36712f1c", datetime(2023, 8, 7, 12, 0, 0), datetime(2023, 8, 7, 12, 0, 0), datetime(2023, 8, 7, 12, 0, 0),
     "Device002", 55, 223.45, 2, datetime(2023, 8, 7)),
    ("24a36712f1c", datetime(2099, 8, 7, 12, 0, 0), datetime(2099, 8, 7, 12, 0, 0), datetime(2099, 8, 7, 12, 0, 0),
     "Device002", 56, 463.45, 2, datetime(2023, 8, 7))

]