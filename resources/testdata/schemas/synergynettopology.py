from datetime import datetime
import pyarrow as pa

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("ROUTER_NAME", pa.string(), True),
        ("PARENT_NAME", pa.string(), True),
        ("ALT_PARENT_NAME", pa.string(), True),
        ("REPORTED_LEVEL", pa.int32(), True),
        ("EUI64", pa.string(), True),
    ]
)

data = [
    ("24a36712f1c", datetime(2023, 6, 25, 12, 34, 56), "Device1", "Router1", "Parent1", "AltParent1", 5, "EUI64-001"),
    ("24a36712f1c", datetime(2023, 7, 25, 11, 11, 11), "Device1", "Router1", "Parent2", "AltParent2", 4, "EUI64-002"),
    ("24a36712f1c", datetime(2023, 7, 25, 11, 11, 11), "Device1", "Router1", "Parent2", "AltParent2", 4, "EUI64-002"),
    ("24a36712f1c", datetime(2090, 7, 25, 14, 12, 23), "Device1", "Router1", "Parent3", "AltParent3", 3, "EUI64-003")
]
