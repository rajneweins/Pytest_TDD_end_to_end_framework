import pyarrow as pa
from datetime import datetime
schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("SYSTEM_NAME", pa.string(), False),
        ("EVENT_ID", pa.int64(), False),
        ("OBJECT_TYPE", pa.string(), False),
        ("EVENT_NAME", pa.string(), False),
        ("EVENT_CATEGORY", pa.string(), False),
        ("EVENT_SEVERITY", pa.int32(), False),
        ("EVENT_DOC", pa.string(), True),
        ("CIM_ENDDEVICEEVENTTYPE", pa.string(), True)
    ]
)

data = [
    ("24a36712f1c", datetime(2023, 9, 15, 12, 12, 12), "System A", 1, "Type A", "Event A", "Category A", 1,
     "This is event A.", None),
    ("24a36712f1c", datetime(2045, 7, 24, 12, 12, 12), "System D", 4, "Type D", "Event D", "Category D", 4,
     "This is event E.", None),
    ("24a36712f1c", datetime(2050, 7, 24, 11, 11, 11), "System E", 5, "Type E", "Event E", "Category E", 5,
     "This is event F.", "EndDeviceEventType B")

]
