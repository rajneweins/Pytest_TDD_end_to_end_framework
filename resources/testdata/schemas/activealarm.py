
import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("OBJECT_NAME", pa.string(), False),
        ("EVENT_ID", pa.int64(), False),
        ("LAST_UPDATED", pa.timestamp('ns'), True)
    ]
)
data = [
    ("24a36712f1c", datetime(2023, 8, 1, 8, 34, 56), "Object_A", 101, None),
    ("24a36712f1c", datetime(2023, 8, 1, 8, 34, 56), "Object_B", 102, None),
    ("24a36712f1c", datetime(2099, 8, 1, 8, 34, 56), "Object_A", 103, None),

]

