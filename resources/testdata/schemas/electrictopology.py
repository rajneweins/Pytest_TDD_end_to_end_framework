import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("DEVICE_NAME", pa.string(), False),
        ("TRANSFORMER_ID", pa.string(), False),
        ("FEEDER_ID", pa.string(), False),
        ("SUBSTATION_ID", pa.string(), False),
        ("AREA_ID", pa.string(), False),
        ("NOMINAL_VOLTAGE", pa.string(), False),  # Fix the data type here
        ("SUPPLY_PHASE", pa.int32(), False),
    ]
)

data = [
    ("24a36712f1c", datetime(2023, 7, 19, 23, 0, 0), "Device A", "TRX001", "FEED002", "121", "530012", "220.5", 1),
    ("24a36712f1c", datetime(2023, 10, 10, 23, 0, 0), "Device B", "TRX002", "FEED003", "122", "530084", "260.5", 2),
    ("24a36712f1c", datetime(2050, 7, 19, 23, 0, 0), "Device A", "TRX003", "FEED004", "123", "530012", "245.5", 3),
]