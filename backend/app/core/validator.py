import pandas as pd

from typing import List, Dict, Any, Optional


def validate_csv(df: pd.DataFrame) -> List[str, Any]:

    errors: List[Dict[str, Optional[Any]]] = []

    required_columns = {"id", "email", "age"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        return {
            "status": "fail",
            "errors": [
                {
                    "row_index": None,
                    "id": None,
                    "column": None,
                    "error_message": f"Missing required columns: {', '.join(sorted(missing_columns))}"
                }
            ]
        }


    if len(df) <= 10:
        return {
            "status": "fail",
            "errors": [
                {
                    "row_index": None,
                    "id": None,
                    "column": None,
                    "error_message": "Volume check failed: file must contain more than 10 data rows."
                }
            ]
        }

    

