"""
Academic Schedule Generator - Source Modules

This package provides modular components for generating academic schedules
from JSON data to professional PDF documents with LaTeX.
"""

from .data_loader import load_schedule_data, get_event_dates, get_calendar_months
from .event_processor import group_events_by_month
from .latex_header import generate_latex_header
from .calendar_generator import generate_calendars
from .table_generators import generate_month_table, generate_exam_period_table
from .pdf_compiler import compile_pdf
from . import config

__version__ = '1.0.0'
__author__ = 'Academic Schedule Generator Team'

__all__ = [
    'load_schedule_data',
    'get_event_dates',
    'get_calendar_months',
    'group_events_by_month',
    'generate_latex_header',
    'generate_calendars',
    'generate_month_table',
    'generate_exam_period_table',
    'compile_pdf',
    'config',
]
