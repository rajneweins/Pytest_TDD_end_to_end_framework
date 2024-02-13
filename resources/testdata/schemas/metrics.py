import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), True),
        ("EXPORT_TIME", pa.timestamp('ns'), True),
        ("TIMESTAMP", pa.timestamp('ns'), False),
        ("METRIC_ID", pa.int64(), False),
        ("OBJECT_NAME", pa.string(), True),
        ("METRIC_VALUE", pa.float64(), True),

    ]
)
data = [
    ("24a36712f1c", datetime(2023, 9, 15, 10, 30, 00), datetime(2023, 7, 17, 10, 31, 00), 1, "Object1", 1.5),
    ("24a36712f1c", datetime(2023, 9, 15, 11, 12, 00), datetime(2023, 7, 17, 11, 46, 00), 2, "Object2", 2.5),
    ("24a36712f1c", datetime(2099, 7, 15, 12, 15, 00), datetime(2023, 7, 17, 12, 6, 00), 3, "Object3", 3.5)
]