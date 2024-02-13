import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("SERVICE_DISCONNECT_STATE", pa.int32(), False),
        ("LAST_SERVICE_DISCONNECT", pa.timestamp('ns'), True),
        ("LAST_SERVICE_RECONNECT", pa.timestamp('ns'), True),
        ("LAST_COMM_CONNECTION", pa.timestamp('ns'), True),
        ("LAST_SELF_READ", pa.timestamp('ns'), True),
        ("LAST_CURR_READ", pa.timestamp('ns'), True),
        ("LAST_PREV_READ", pa.timestamp('ns'), True),
        ("LAST_PSEAS_READ", pa.timestamp('ns'), True),
        ("LAST_INTERVAL_1_READ", pa.timestamp('ns'), True),
        ("LAST_INTERVAL_2_READ", pa.timestamp('ns'), True),
        ("LAST_INTERVAL_3_READ", pa.timestamp('ns'), True),
        ("LAST_PROGRAMMED", pa.timestamp('ns'), True),
        ("LAST_COMM_ADDRESS_CHANGE", pa.timestamp('ns'), True),

    ]
)

data = [

    ("24a36712f1c", datetime(2023, 9, 15, 12, 0, 0), "UDP", 1, None, None, None, None, None, None, None, None, None,
     None, None, None),
    ("24a36712f1c", datetime(2023, 9, 15, 12, 0, 0), "UDP", 1, None, None, None, None, None, None, None, None, None,
     None, None, None),
    ("24a36712f1c", datetime(2090, 9, 15, 12, 0, 0), "UDP", 1, None, None, None, None, None, None, None, None, None,
     None, None, None)

]
