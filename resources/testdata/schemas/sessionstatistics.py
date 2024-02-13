import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("START_TIME", pa.timestamp('ns'), False),
        ("GK_ID", pa.int64(), False),
        ("NUM_REGISTERED_METERS", pa.int64(), False),
        ("LINE_NUMBER", pa.int64(), False),
        ("TOTAL_TIME_IN_SECONDS", pa.int64(), False),
        ("BYTES_RX", pa.int64(), False),
        ("BYTES_TX", pa.int64(), False),
        ("PACKETS_SUCCESSFUL", pa.int64(), False),
        ("PACKETS_RETRIED", pa.int64(), False),
        ("PACKETS_FAILED", pa.int64(), False),
        ("SESSION_STATUS", pa.int64(), False),
        ("AVG_PACKET_TIME", pa.int64(), False),
        ("MIN_PACKET_TIME", pa.int64(), False),
        ("MAX_PACKET_TIME", pa.int64(), False),
        ("WFID", pa.int64(), True),
        ("SCHEDULE_START_TIME", pa.timestamp('ns'), True),
        ("DIRECTION", pa.int64(), False),
        ("SESSION_ID", pa.int64(), False),
        ("SCHEDULE_ID", pa.int64(), True),
        ("CONNECTION_TIME", pa.int64(), True),
        ("LIM_HOST", pa.string(), True),

    ]
)
data = [

    ("24a36712f1c", datetime(2023, 8, 7, 12, 0, 0), datetime(2023, 7, 20, 12, 12), 2, 200, 2, 500, 2048,
     1024, 190, 10, 0, 1, 45, 5, 800, 50, datetime(2023, 7, 19, 12, 12, 12), 1, 2, 100002, 300, "HostA"),
    ("24a36712f1c", datetime(2099, 8, 7, 12, 0, 0), datetime(2099, 7, 20, 12, 12), 2, 200, 2, 500, 2048,
     1024, 190, 10, 0, 1, 45, 5, 800, 50, datetime(2099, 7, 19, 12, 12, 12), 1, 2, 100002, 300, "HostB"),

]