#!/usr/bin/env python3
"""
Event Processing Module
Handles grouping and organizing events
"""

from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Any


def group_events_by_month(events: List[Dict[str, Any]], subjects: Dict[str, Dict[str, str]]) -> Tuple[Dict[Tuple[int, int], List[Dict[str, Any]]], List[Dict[str, Any]]]:
    """
    Group events by month and sort them.
    
    Args:
        events: List of event dictionaries
        subjects: Dictionary of subject information
        
    Returns:
        Tuple of (events_by_month dict, exam_period_events list)
    """
    events_by_month = defaultdict(list)
    exam_period_events = []
    
    for event in events:
        # Handle exam period separately
        if event.get('section') == 'Exam Period':
            exam_period_events.append(event)
            continue
        
        date_str = event['date']
        if date_str == 'TBA':
            continue
            
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            month_key = (date_obj.year, date_obj.month)
            
            # Get subject info
            subject_key = event['subject']
            subject_info = subjects.get(subject_key, {})
            
            # Prepare event data
            event_data = {
                'date': date_obj,
                'time': event.get('time', ''),
                'type': event['type'],
                'subject_name': subject_info.get('name', subject_key),
                'subject_code': subject_info.get('code', ''),
                'room': event.get('room') or subject_info.get('default_room', ''),
                'date_str': date_obj.strftime('%d %b (%a)')
            }
            
            events_by_month[month_key].append(event_data)
        except ValueError:
            continue
    
    # Sort events within each month
    for month_key in events_by_month:
        events_by_month[month_key].sort(key=lambda e: (e['date'], e['time']))
    
    return events_by_month, exam_period_events
