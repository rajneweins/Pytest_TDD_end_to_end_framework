import pyarrow as pa
from datetime import datetime

schema = pa.schema(
    [
        ("CUSTOMER", pa.string(), False),
        ("EXPORT_TIME", pa.timestamp('ns'), False),
        ("CATEGORY", pa.string(), False),
        ("SUBCATEGORY", pa.string(), False),
        ("NAME", pa.string(), False),
        ("DISPLAY_CATEGORY", pa.string(), True),
        ("DISPLAY_NAME", pa.string(), True),
        ("SETTING_TYPE", pa.string(), False),
        ("DEFAULT_VALUE", pa.string(), True),
        ("LAST_DEFAULT_UPDATED", pa.timestamp('ns'), True),
        ("VALUE", pa.string(), True),
        ("LAST_VALUE_UPDATED", pa.timestamp('ns'), True),
        ("VISIBILITY", pa.string(), True),
        ("EFFECTIVE_WHEN", pa.string(), True),
        ("HELP_TEXT", pa.string(), True),
        ("LAST_CHANGE_NOTE", pa.string(), True),
        ("LAST_MODIFIED_BY", pa.string(), True),
        ("UNITS", pa.string(), True),
        ("VALIDATION", pa.string(), True),
        ("RULE", pa.string(), True)
    ]
)

data = [
    ("24a36712f1c", datetime(2023, 8, 10), "CategoryA", "Subcategory1", "Setting1", "DisplayCategory1", None, "Type1",
     "Default1", datetime(2023, 7, 10), "Value1", datetime(2023, 8, 10), "Visible", "Effective", "HelpText1",
     "Note2", "User1", "Unit1", "Validation1", "Rule1"),
    ("24a36712f1c", datetime(2023, 8, 10), "CategoryB", "Subcategory2", "Setting2", "DisplayCategory2", None, "Type2",
     "Default1", datetime(2023, 7, 10), "Value1", datetime(2023, 8, 10), "Visible", "Effective", "HelpText2", "Note2",
     "User1", "Unit2", "Validation2", "Rule2"),
    ("24a36712f1c", datetime(2067, 8, 10), "CategoryA", "Subcategory2", "Setting2", "DisplayCategory2", None, "Type2",
     "Default1", datetime(2067, 7, 10), "Value1", datetime(2090, 8, 10), "Visible", "Effective", "HelpText2", "Note2",
     "User1", "Unit2", "Validation2", "Rule2")

    ]