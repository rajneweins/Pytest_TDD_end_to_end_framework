import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("TIMESTAMP", pa.timestamp('ns'), False),
        ("DETECTION_TIME", pa.timestamp('ns'), False),
        ("START_TIME", pa.timestamp('ns'), True),
        ("END_TIME", pa.timestamp('ns'), True),
        ("EVENT_ID", pa.int64(), False),
        ("OBJECT_NAME", pa.string(), False),
        ("PARAMETERS", pa.string(), True)
    ]
)
data = [

        ("24a36712f1c", datetime(2023, 8, 11, 12, 34, 56), datetime(2023, 8, 11, 12, 34, 56),
         datetime(2023, 8, 11, 12, 34, 56), datetime(2023, 8, 11, 4, 34, 56), datetime(2023, 8, 11, 12, 34, 56), 1,
         "obj1", "12512"),
        ("24a36712f1c", datetime(2023, 8, 11, 12, 34, 56), datetime(2023, 8, 11, 12, 34, 56),
         datetime(2023, 8, 11, 12, 34, 56), datetime(2023, 8, 11, 4, 34, 56), datetime(2023, 8, 11, 12, 34, 56), 1,
         "obj2", "1678"),
        ("24a36712f1c", datetime(2099, 8, 11, 12, 34, 56), datetime(2099, 8, 11, 12, 34, 56),
         datetime(2099, 8, 11, 12, 34, 56), datetime(2099, 8, 11, 12, 34, 56), datetime(2099, 8, 11, 12, 34, 56), 3,
         "obj1", "17838")

]
