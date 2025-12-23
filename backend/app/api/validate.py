from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from core.validator import read_csv_fix_quotes, validate_csv

router = APIRouter()

@router.post("/validate")
async def validate_csv_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    contents = await file.read()
    temp_file_path = f"/tmp/{file.filename}"

    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(contents)

    try:
        df = read_csv_fix_quotes(temp_file_path)
        validation_result = validate_csv(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

    return validation_result

