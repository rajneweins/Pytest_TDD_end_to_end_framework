import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("NAME", pa.string(), False),
        ("FW_SSPEC", pa.int32(), False),
        ("FW_VERSION", pa.int32(), False),
        ("FW_REVISION", pa.int32(), False),
        ("FW_PATCH", pa.int32(), True),
        ("LAST_UPDATED", pa.timestamp('ns'), False),
        ("LAST_CONFIRMED", pa.timestamp('ns'), True)
    ]
)
data = [

    ("24a36712f1c", datetime(2023, 9, 21, 10, 30, 0), "alm meter", "Name1", 102, 1, 0, None, datetime(2023, 8, 21, 10, 30, 0), None),
    ("24a36712f1c", datetime(2023, 9, 21, 10, 30, 0), "alm meter", "Name1", 102, 1, 0, None, datetime(2023, 8, 21, 10, 30, 0), datetime(2023,9,21,12,12,12)),
    ("24a36712f1c", datetime(2090, 9, 21, 10, 30, 0), "alm meter", "Name1", 102, 1, 0, None, datetime(2090, 8, 21, 10, 30, 0), None),
    ("24a36712f1c", datetime(2099, 9, 21, 10, 30, 0), "alm meter", "Name1", 102, 1, 0, None, datetime(2099, 8, 21, 10, 30, 0), None)
]