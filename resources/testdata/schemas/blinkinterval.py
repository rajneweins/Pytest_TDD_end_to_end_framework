import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("CHARGER_NETWORK_ID", pa.string(), False),
        ("SESSION_ID", pa.string(), False),
        ("TIMESTAMP", pa.timestamp('ns'), False),
        ("MISSING", pa.string(), False),
        ("CHARGING_SESSION", pa.string(), False),
        ("ENERGY_CONSUMPTION", pa.float64(), False),
        ("AVERAGE_POWER", pa.float64(), False),
        ("PEAK_POWER", pa.float64(), False)
    ]
)
data = [
    (datetime(2023, 9, 21, 8, 34, 56), "Network_1", "Session_1", datetime(2023, 8, 10, 9, 34, 56), "False", "Session_A",
     100.23, 50.12, 75.5),
    (datetime(2023, 9, 21, 8, 34, 56), "Network_2", "Session_2", datetime(2023, 8, 10, 9, 34, 56), "False", "Session_B",
     100.23, 50.12, 75.5),
    (datetime(2023, 9, 21, 8, 34, 56), "Network_2", "Session_2", datetime(2023, 8, 10, 9, 34, 56), "False", "Session_B",
     100.23, 50.12, 75.5),
    (datetime(2090, 9, 21, 8, 34, 56), "Network_1", "Session_1", datetime(2023, 8, 10, 9, 34, 56), "False", "Session_A",
     100.23, 50.12, 75.5),
    (datetime(2099, 9, 21, 8, 34, 56), "Network_1", "Session_1", datetime(2023, 8, 10, 9, 34, 56), "False", "Session_A",
     100.23, 50.12, 75.5),
]
