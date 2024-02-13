import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [

        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("METRIC_ID", pa.int64(), False),
        ("OBJECT_TYPE", pa.string(), False),
        ("METRIC_NAME", pa.string(), False),
        ("METRIC_CATEGORY", pa.string(), False),
        ("METRIC_UNITS", pa.string(), True)

    ]
)
data = [
    ("24a36712f1c", datetime(2023, 9, 15, 10, 30, 00), 1, "Object1", "MetricName1", "Category1", "Units1"),
    ("24a36712f1c", datetime(2023, 9, 15, 10, 30, 00), 2, "Object2", "MetricName2", "Category2", "Units2"),
    ("24a36712f1c", datetime(2099, 9, 15, 10, 30, 00), 3, "Object3", "MetricName3", "Category3", None)
]

