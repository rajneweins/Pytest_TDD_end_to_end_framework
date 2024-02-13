import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ('CUSTOMER', pa.string(), False),
        ('EXPORT_TIME', pa.timestamp('ns'), False),
        ('DEVICE_IRN', pa.int64(), False),
        ('DEVICE_NAME', pa.string(), True),
        ('DEVICE_TYPE', pa.int32(), True),
        ('SERIAL_NUMBER', pa.string(), False),
        ('COMM_ADDRESS', pa.string(), False),
        ('COMM_TYPE', pa.int32(), False),
        ('TIMEZONE_NAME', pa.string(), False),
        ('OBSERVES_DST', pa.string(), False),
        ('DESCRIPTION', pa.string(), False),
        ('ACCOUNT_ID', pa.string(), False),
        ('ACCOUNT_NAME', pa.string(), False),
        ('SDP_ID', pa.string(), False),
        ('SITE_LOCATION', pa.string(), False),
        ('LATITUDE', pa.float64(), False),
        ('LONGITUDE', pa.float64(), False),
        ('REMOTE_DISCONNECT', pa.int32(), False),
        ('SKU', pa.string(), False),
        ('INSTALL_DATE', pa.timestamp('ns'), False),
        ('REMOVAL_DATE', pa.timestamp('ns'), False),
        ('ROUTE_ID', pa.string(), False),
        ('BILLING_CYCLE_ID', pa.string(), False),
        ('UTILITY_ID', pa.int32(), False)
    ]
)
data = [
    ("svt-saas15", datetime(2023, 8, 7, 12, 0, 0), 1, "Bricked-9017020807", 1700, "9017020807",
     "10.1.0.62:4059", 12, "America/New_York", "1", None, None, None,
     None, None, 0, 0, 1, "0000", 0,
     datetime(2023, 7, 25, 12, 0, 0), None, None, 0),

    ("svt-saas15", datetime(2023, 8, 7, 12, 0, 0), 1, "Bricked-9017020807", 1700, "9017020807",
     "10.1.0.62:4059", 12, "America/New_York", "1", None, None, None,
     None, None, 0, 0, 1, "0000", datetime(2023, 7, 1, 0, 0, 0),
     0, None, None, 0),

]
