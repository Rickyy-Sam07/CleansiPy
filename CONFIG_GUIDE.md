# CleansiPy Configuration Guide

## Quick Setup

1. **Install CleansiPy:**
   ```bash
   pip install CleansiPy
   ```

2. **Copy the default config to your working directory:**
   ```bash
   cleansipy-config
   ```

3. **Edit the `config.py` file** with your actual file paths and column names.

4. **Run CleansiPy:**
   ```bash
   cleansipy
   ```

## Key Changes Made

### ✅ Fixed Issues:
- **File paths**: Removed hardcoded `testdata\` paths 
- **Column names**: Removed hardcoded column names
- **Function parameter**: Fixed `put_path` → `input_path` in categorical cleaner
- **Data type bug**: Fixed `dtypesv` → `dtypes` in preview function

### ✅ User-Friendly Defaults:
- `input_data.csv` → change to your file
- `cleaned_categorical.csv` → output file
- Auto-detection for categorical columns (set `COLUMNS_TO_CLEAN: None`)
- Empty lists for numeric column configurations

## Configuration Examples

### For Categorical Data:
```python
config2 = {
    "INPUT_FILE": r"my_sales_data.csv",
    "OUTPUT_FILE": r"cleaned_sales.csv", 
    "COLUMNS_TO_CLEAN": None,  # Auto-detect columns
    # ... other settings
}
```

### For Numeric Data:
```python
DEFAULT_CONFIG = {
    'input_file': r'sales_data.csv',
    'type_conversion': {
        'numeric_cols': ['price', 'quantity', 'revenue']  # Your column names
    },
    'outliers': {
        'columns': ['price', 'quantity']  # Columns to check for outliers
    },
    # ... other settings
}
```

### For Text Data:
```python
config = {
    'input_file': r"reviews.csv",
    'output_file': r"cleaned_reviews.csv",
    'text_column': None,  # Auto-detect text column
    # ... other settings
}
```

## Next Steps

After updating your config file, run:
```bash
cleansipy
```

And select the type of data cleaning you need!
