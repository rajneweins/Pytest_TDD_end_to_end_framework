import pyarrow as pa
from datetime import datetime

# Define the schema

schema = pa.schema([
    ("CUSTOMER",pa.string(), False),
    ("EXPORT_TIME",pa.timestamp('ns'), False),
    ("JOB_ID",pa.int64(), False),
    ("NOTIFICATION_TYPE",pa.int64(), False),
    ("NOTIFICATION_INFO",pa.string(), False),
    ("JOB_STATUS_ID", pa.int32(), False),
    ("JOB_STATUS", pa.string(), False),
    ("CREATED", pa.timestamp('ns'), False),
    ("STARTED", pa.timestamp('ns'), True),
    ("COMPLETED", pa.timestamp('ns'), True),
    ("CANCELED", pa.timestamp('ns'), True),
    ("PRIORITY", pa.int32(), False),
    ("CONTEXT", pa.int64(), False),
    ("EXPIRATION_TIME", pa.timestamp('ns'), True),
    ("SUBMIT", pa.int32(), True),
    ("PUBLISH", pa.int32(), True),
    ("CONSUMER", pa.string(), False),
    ("JOBNAME", pa.string(), False),
    ("CORRELATION_ID", pa.string(), False),
    ("SCHEDULED_START_TIME", pa.timestamp('ns'), True),
    ("PUBLISH_PRIORITY", pa.int32(), False),
    ("JOB_TYPE_ID", pa.int32(), False),
    ("JOB_TYPE",pa.string(), False),
    ("DESCRIPTION",pa.string(), True),
    ("LAST_UPDATED", pa.timestamp('ns'), True)
])

data = [
    ("24a36712f1c", datetime(2023, 9, 20), 1, 10, "Info1", 101, "InProgress", datetime(2023, 8, 1), None, None, None, 1,
     1001, None, 1, 0, "Consumer1", "Job1", "Correlation1", None, 1, 10, "Type1", None, None),
    ("24a36712f1c", datetime(2099, 9, 20), 2, 20, "Info2", 102, "Completed", datetime(2099, 8, 2), datetime(2099, 8, 2),
     datetime(2099, 8, 2), None, 2, 1002, datetime(2023, 8, 3), 2, 1, "Consumer2", "Job2", "Correlation2",
     datetime(2099, 8, 3), 2, 20, "Type2", "Description2", datetime(2099, 8, 4)),


]



