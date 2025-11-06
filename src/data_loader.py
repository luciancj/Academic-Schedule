#!/usr/bin/env python3
"""
Data Loading Module
Handles loading and processing of schedule data from JSON
"""

import json
from datetime import datetime, date
from typing import Dict, List, Set, Any


def load_schedule_data(json_file: str = 'schedule_data.json') -> Dict[str, Any]:
    """
    Load schedule data from JSON file and validate structure.
    
    Args:
        json_file: Path to JSON file containing schedule data
        
    Returns:
        Dictionary containing schedule_info, subjects, and events
        
    Raises:
        FileNotFoundError: If JSON file doesn't exist
        json.JSONDecodeError: If JSON is malformed
        ValueError: If required fields are missing
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schedule file '{json_file}' not found")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in '{json_file}': {e.msg}", e.doc, e.pos)
    
    # Validate required top-level keys
    required_keys = ['schedule_info', 'subjects', 'events']
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        raise ValueError(f"Missing required fields in JSON: {', '.join(missing_keys)}")
    
    # Validate schedule_info structure
    schedule_info = data['schedule_info']
    required_schedule_fields = ['title', 'period', 'start_date', 'end_date']
    missing_fields = [field for field in required_schedule_fields if field not in schedule_info]
    if missing_fields:
        raise ValueError(f"Missing required schedule_info fields: {', '.join(missing_fields)}")
    
    # Validate date formats
    try:
        datetime.strptime(schedule_info['start_date'], '%Y-%m-%d')
        datetime.strptime(schedule_info['end_date'], '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format in schedule_info (use YYYY-MM-DD): {e}")
    
    return data


def get_event_dates(events: List[Dict[str, Any]]) -> Set[date]:
    """
    Extract all valid event dates from events list.
    
    Args:
        events: List of event dictionaries
        
    Returns:
        Set of date objects for all valid events
    """
    dates = set()
    for event in events:
        date_str = event.get('date', '')
        if date_str and date_str != 'TBA':
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                dates.add(date_obj.date())
            except ValueError:
                # Skip invalid dates silently
                pass
    return dates


def get_calendar_months(start_date_str: str, end_date_str: str) -> List[Dict[str, Any]]:
    """
    Get list of all months in the schedule period.
    
    Args:
        start_date_str: Start date in YYYY-MM-DD format
        end_date_str: End date in YYYY-MM-DD format
        
    Returns:
        List of dictionaries containing month information (year, month, name, date_obj)
    """
    start = datetime.strptime(start_date_str, '%Y-%m-%d')
    end = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    months = []
    current = start.replace(day=1)
    end_month = end.replace(day=1)
    
    while current <= end_month:
        months.append({
            'year': current.year,
            'month': current.month,
            'name': current.strftime("%B"),
            'date_obj': current
        })
        # Move to next month
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)
    
    return months
