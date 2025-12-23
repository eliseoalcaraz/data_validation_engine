import pandas as pd
from typing import List, Dict, Any, Optional
from pathlib import Path
from io import StringIO

def read_csv_fix_quotes(file_path: str) -> pd.DataFrame:
    file_path = Path(file_path)
    with file_path.open() as f:
        cleaned_lines = [line.strip().strip('"') for line in f.readlines()]
    csv_content = "\n".join(cleaned_lines)
    df = pd.read_csv(StringIO(csv_content))
    df.columns = df.columns.str.strip().str.lower()
    return df

def validate_csv(df: pd.DataFrame) -> Dict[str, Any]:

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

    for idx, row in df.iterrows():
        row_index = idx + 1
        row_id = row.get("id")

        email = row.get("email")
        if pd.isna(email) or str(email).strip() == "":
            errors.append({
                "row_index": row_index,
                "id": row_id,
                "column": "email",
                "error_message": "Email is missing or empty."
            })

        age_value = row.get("age")

        if pd.isna(age_value):
            errors.append({
                "row_index": row_index,
                "id": row_id,
                "column": "age",
                "error_message": "Invalid age format."
            })
        else:
            try:
                age_int = int(age_value)
                if age_int < 18 or age_int > 100:
                    errors.append({
                        "row_index": row_index,
                        "id": row_id,
                        "column": "age",
                        "error_message": "Age out of allowed range (18–100)."
                    })
            except (ValueError, TypeError):
                errors.append({
                    "row_index": row_index,
                    "id": row_id,
                    "column": "age",
                    "error_message": "Invalid age format."
                })

    status = "pass" if not errors else "fail"

    return {
        "status": status,
        "errors": errors
    }



