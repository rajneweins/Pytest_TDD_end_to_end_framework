import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), True),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("ROUTER_NAME", pa.string(), False),
        ("PARENT_NAME", pa.string(), False),
        ("ALT_PARENT_NAME", pa.string(), False),
        ("REPORTED_LEVEL", pa.int32(), False),
        ("NUM_DESCENDANTS", pa.int32(), False),
    ]
)

data = [
    ("24a36712f1c", datetime(2023, 8, 11, 12, 34, 56), "Device1", "Router1", "Parent1", "AltParent1", 5, 1),
    ("24a36712f1c", datetime(2023, 8, 11, 12, 34, 56), "Device1", "Router1", "Parent1", "AltParent1", 5, 1),
    ("24a36712f1c", datetime(2099, 8, 11, 11, 11, 11), "Device2", "Router2", "Parent2", "AltParent2", 4, 1),
    ("24a36712f1c", datetime(2067, 8, 11, 14, 12, 23), "Device3", "Router3", "Parent3", "AltParent3", 3, 1)
]
