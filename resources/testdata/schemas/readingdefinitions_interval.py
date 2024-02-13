import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("OBJECT_NUMBER", pa.int64(), False),
        ("PERIOD", pa.string(), False),
        ("TYPE", pa.string(), True),
        ("SUBTYPE", pa.string(), False),
        ("TIER", pa.string(), False),
        ("UOM", pa.string(), False),
        ("DIRECTION", pa.string(), False),
        ("QUADRANT", pa.string(), False),
        ("CIM_READINGTYPE_V2", pa.string(), False),
        ("CIM_READINGTYPE_V1", pa.string(), False),
        ("COMMODITY_TYPE", pa.int32(), False),
        ("IS_REGISTER", pa.int32(), False),
        ("IS_INTERVAL", pa.int32(), True),
        ("IS_INSTRUMENTATION", pa.int32(), False),
        ("IS_PQM", pa.int32(), False),
        ("INTERVAL_LENGTH_MINS", pa.int32(), False)
    ]
)
data = (
    ("24a36712f1c", datetime(2023, 10, 4, 10, 0, 0), 54, "Period 1", "Type A", "Subtype W", "Tier 1", "UOM 1",
     "Direction 1",
     "Quadrant A", "Reading 1", "Reading 1", 1, 0, 1, 0, 0, 15),
    ("24a36712f1c", datetime(2023, 10, 4, 11, 3, 0), 55, "Period 2", "Type B", "Subtype X", "Tier 2", "UOM 2",
     "Direction 2",
     "Quadrant B", "Reading 2", "Reading 2", 2, 0, 1, 0, 0, 15),
    ("24a36712f1c", datetime(2045, 10, 4, 12, 15, 0), 56, "Period 3", "Type C", "Subtype Y", "Tier 3", "UOM 3",
     "Direction 3",
     "Quadrant C", "Reading V2", "Reading V1", 3, 0, 1, 0, 0, 15)
)
