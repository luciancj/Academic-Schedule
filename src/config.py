"""
Configuration Module
Centralized configuration for the schedule generator
"""

from typing import Dict, Any

# Default file paths
DEFAULT_JSON_FILE = 'schedule_data.json'
DEFAULT_OUTPUT_FILE = 'Academic Schedule.tex'

# PDF compilation settings
PDF_COMPILER = 'pdflatex'
PDF_COMPILER_OPTIONS = ['-interaction=nonstopmode']

# Loading bar settings
LOADING_BAR_LENGTH = 30
LOADING_BAR_FILLED_CHAR = '█'
LOADING_BAR_EMPTY_CHAR = '░'
LOADING_BAR_DELAY = 0.05  # seconds

# LaTeX auxiliary file extensions to clean up
AUX_FILE_EXTENSIONS = ['.aux', '.log', '.out']

# Date format for JSON input
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M'

# LaTeX table column widths
COLUMN_WIDTHS: Dict[str, str] = {
    'date': '2.8cm',
    'time': '1.5cm',
    'event': '13cm',
    'room': '2cm',
    'done': '1.8cm',
}

# Calendar layout (calendars per row)
CALENDARS_PER_ROW = 3
CALENDAR_X_SPACING = 10  # cm
CALENDAR_Y_SPACING = 10  # cm
