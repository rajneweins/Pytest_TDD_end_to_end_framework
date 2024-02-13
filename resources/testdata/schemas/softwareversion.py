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
    ("24a36712f1c", "UDP", "HostA", "1.0.0", datetime(2023, 9, 10, 12, 34, 56), datetime(2023, 9, 1, 10, 0, 0)),
    ("24a36712f1c", "UDP", "HostB", "2.0.0", datetime(2023, 10, 10, 12, 34, 56), datetime(2023, 10, 1, 10, 0, 0)),
    ("24a36712f1c", "UDP", "HostB", "2.1.0", datetime(2067, 7, 10, 14, 30, 15), datetime(2067, 7, 2, 11, 0, 0))

]
