# ================================================
# CleansiPy Configuration File
# ================================================
# 
# IMPORTANT: Before using CleansiPy, you MUST update the file paths below!
# 
# 1. Replace "input_data.csv", "input_numeric.csv", etc. with YOUR actual file paths
# 2. For categorical data: update COLUMNS_TO_CLEAN with your column names
# 3. For numeric data: update numeric_cols, constraints, outliers, and precision with your column names
# 4. Make sure your input files exist in the specified locations
#
# Example file paths:
#   - Absolute path: r"C:\Users\YourName\Documents\my_data.csv"
#   - Relative path: r"data\sales_data.csv" (relative to where you run CleansiPy)
#   - Current directory: r"my_file.csv"
#
# ================================================

#############################################
#config2 for categoricaldata                   #
#############################################
# EDIT THESE SETTINGS AS NEEDED
# Replace the file paths below with your actual data file paths
config2 = {
    "INPUT_FILE": r"input_data.csv",              # Path to your input CSV file (change this!)
    "OUTPUT_FILE": r"cleaned_categorical.csv",        # Where to save the cleaned data
    "TARGET_COLUMN": None,               # Optional target column for supervised learning
    "COLUMNS_TO_CLEAN": None,  # Set to None for auto-detection or list specific columns like ["category", "type"]
    "EXCLUDE_COLUMNS": [],               # Columns to exclude from cleaning
    "EXPLORE_ONLY": False,               # Set to True to only explore data without cleaning
    "FILE_PATH": r"categorical_cleaning_report.txt",  # Path to save the cleaning report
    
    # Advanced Settings
    "FIX_TYPOS": True,                   # Whether to fix typos in text
    "GROUP_RARE": True,                  # Whether to group rare categories
    "RARE_THRESHOLD": 0.05,              # Categories with frequency below this are considered rare
    "SIMILARITY_THRESHOLD": 80,          # Threshold (0-100) for fuzzy matching of typos
    "MEMORY_EFFICIENT": False,           # Set to True for very large datasets
    "PARALLEL_JOBS": -1                  # Number of parallel jobs (-1 for all cores)
}
#############################################

# NUMERIC DATA CONFIG-
# --------------------------
# Replace the file paths below with your actual data file paths
# Modify these settings based on your specific dataset requirements.This configuration controls how the data cleaning pipeline processes your dataset.

DEFAULT_CONFIG = {

    'input_file': r'input_numeric.csv',  # Path to your input CSV file (change this!)
    'output_file': r'cleaned_numeric.csv',  # Path for output cleaned CSV file
    'report_file': r'numeric_cleaning_report.txt',  # Path to save cleaning report

    # Type Conversion Settings
    # -----------------------
    # Specify which columns should be converted to numeric types
    # For non-numeric datasets, set this to [] or remove columns that aren't numeric
    # CHANGE THESE COLUMN NAMES TO MATCH YOUR DATA:
    'type_conversion': {
        'numeric_cols': []  # Example: ['sales', 'revenue', 'age'] - replace with your column names
    },
    
    # Missing Value Handling
    # ---------------------
    # strategy: how to fill missing values ('mean', 'median', 'mode')
    # threshold: maximum ratio of missing values allowed (0.0 to 1.0)
    'missing_values': {
        'strategy': 'mean',  # Options: 'mean', 'median', 'mode'
        'threshold': 0.5     # Columns with >40% missing values will be flagged
    },
    
    # Data Constraints & Validation
    # ----------------------------
    # Define valid ranges/rules for each column using lambda functions
    # correction: how to replace invalid values ('median', 'mean', 'mode')
    # CHANGE THESE TO MATCH YOUR DATA COLUMNS:
    'data_errors': {
        'constraints': {
            # Example: 'price': lambda x: (x >= 0) & (x <= 10000),  # Add your column constraints here
        },
        'correction': 'median'  # Use median of valid values to replace invalid ones
    },
    
    # Outlier Detection & Handling
    # --------------------------
    # method: technique to detect outliers ('iqr', 'zscore')
    # action: how to handle outliers ('cap', 'remove')
    # columns: specific columns to check for outliers
    # CHANGE THESE TO MATCH YOUR DATA COLUMNS:
    'outliers': {
        'method': 'iqr',  # Interquartile Range method (Q1-1.5*IQR to Q3+1.5*IQR)
        'action': 'cap',  # Cap values at the boundaries instead of removing rows
        'columns': []  # Example: ['price', 'quantity'] - add your numeric column names
    },
    
    # Duplicate Handling
    # -----------------
    # subset: columns to consider when identifying duplicates (None = all columns)
    # keep: which occurrence to keep ('first', 'last', False)
    'duplicates': {
        'subset': None,  # Consider all columns when identifying duplicates
        'keep': 'first'  # Keep the first occurrence and remove others
    },
    
    # Numeric Precision
    # ----------------
    # Control decimal places for each column (0 = integer, >0 = decimal places)
    # CHANGE THESE TO MATCH YOUR DATA COLUMNS:
    'precision': {
        # Example: 'price': 2,  # Two decimal places for currency
        # Example: 'rating': 1,  # One decimal place for ratings
    }
}


#############################################
#   date&time cleaner                 #
#############################################
# EDIT THESE SETTINGS AS NEEDED
# Replace the file paths below with your actual data file paths
config3 = {
    "INPUT_FILE": r"input_dates.csv",             # Path to your input CSV file (change this!)
    "OUTPUT_FILE": r"cleaned_dates.csv",          # Where to save the cleaned data
    "REPORT_FILE": r"datetime_cleaning_report.txt",  # Path to save the cleaning report

    # Date column settings
    "DATE_COLUMNS": None,                  # Set to None for auto-detection or list specific columns
                                           # Example: ["order_date", "shipping_date"]
    "START_END_PAIRS": [],                 # List of (start_date, end_date) column pairs to validate
                                           # Example: [("start_date", "end_date")]

    # Cleaning options
    "PARSE_DATES": True,                   # Convert strings to datetime objects
    "IMPUTE_MISSING": True,                # Fill in missing date values
    "STANDARDIZE_TIMEZONE": False,         # Convert to a standard timezone
    "EXTRACT_FEATURES": True,              # Generate calendar features from dates

    # Advanced settings
    "IMPUTATION_METHOD": "linear",         # Options: "linear", "forward", "backward", "seasonal", "mode"
    "SEASONAL_PERIOD": 7,                  # For seasonal imputation (e.g., 7=weekly, 12=monthly)
    "TARGET_TIMEZONE": "UTC",              # Target timezone for standardization
    "CONSISTENCY_ACTION": "flag",          # How to handle inconsistent dates: "flag", "swap", "drop", "truncate"
    "MEMORY_EFFICIENT": False,             # Set to True for very large datasets

    # Feature extraction
    "CALENDAR_FEATURES": [                 # Features to extract from date columns
        "year", "month", "day", "dayofweek", "quarter", 
        "is_weekend", "is_month_end", "is_quarter_end", 
        "fiscal_quarter", "season"
    ],
    "FISCAL_YEAR_START": 10                # Starting month of fiscal year (1-12)
}
#############################################
#==========================================
#TEXT CLEANING DATA CONFIGURATION
#======================================
# Replace the file paths below with your actual data file paths

config = {
    'lowercase': True,              # Convert all text to lowercase
    'remove_punctuation': True,     # Remove all punctuation marks
    'remove_stopwords': True,       # Remove common stopwords (e.g., "the", "is", "and")
    'remove_urls': True,            # Remove URLs and web addresses
    'remove_html': True,            # Remove HTML tags from text
    'remove_emojis': True,          # Remove emojis and special symbols
    'remove_numbers': True,         # Remove all numeric digits
    'expand_contractions': False,    # Expand contractions (e.g., "don't" -> "do not")
    'spelling_correction': False,    # Correct spelling mistakes in words
    'lemmatize': True,              # Reduce words to their base form (e.g., "running" -> "run")
    'stem': False,                  # Reduce words to their root form (e.g., "running" -> "run"); set True to enable
    'tokenize': 'word',             # Tokenize text into words ('word'), sentences ('sentence'), or None for no tokenization
    'ngram_range': (1, 1),          # Generate n-grams; (1,1) for unigrams only, (1,2) for unigrams and bigrams, etc.
    'profanity_filter': False,      # Remove or mask profane words; set True to enable
    'language': 'english',          # Language for stopwords, lemmatization, and spell checking
    'custom_stopwords': None,       # List of additional stopwords to remove (e.g., ['foo', 'bar']); None for default
    'custom_profanity': None,       # List of additional profane words to filter; None for default
    'input_file': r"text_test.csv",   # Path to input CSV file (change this!)
    'output_file': r"cleaned_text.csv",  # Path to save cleaned output
    'report_file': r"text_cleaning_report.txt",  # Path to save cleaning report
    'text_column': None,            # Specify text column to clean (None for auto-detect)
    'sample_count': 5               # Number of samples to show in report
}