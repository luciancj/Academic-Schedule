#!/usr/bin/env python3
"""
Table Generators
Generates monthly event tables and exam period tables
"""

from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any


def generate_month_table(month_name: str, year: int, month_events: List[Dict[str, Any]], subjects: Dict[str, Dict[str, str]], first_table: bool = True) -> List[str]:
    """
    Generate a table for a specific month.
    
    Args:
        month_name: Name of the month
        year: Year number
        month_events: List of events in this month
        subjects: Dictionary of subject information
        first_table: Whether this is the first table (affects page breaks)
        
    Returns:
        List of LaTeX lines for the month table
    """
    lines = []
    
    if not first_table:
        lines.append(r"\newpage")
    
    lines.append(f"% {month_name} {year}")
    lines.append(f"\\noindent\\textbf{{\\large {month_name} {year}}}")
    lines.append("")
    lines.append(r"\vspace{0.3em}")
    lines.append("")
    lines.append(r"\begin{longtable}{@{} L{2.8cm} M{1.5cm} L{13cm} M{2cm} M{1.8cm} @{}}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Date} & \textbf{Time} & \textbf{Event} & \textbf{Room} & \textbf{Done} \ding{51} \ding{55} \\")
    lines.append(r"\midrule")
    lines.append(r"\endfirsthead")
    lines.append("")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Date} & \textbf{Time} & \textbf{Event} & \textbf{Room} & \textbf{Done} \ding{51} \ding{55} \\")
    lines.append(r"\midrule")
    lines.append(r"\endhead")
    lines.append("")
    
    # Group events by date
    events_by_date = defaultdict(list)
    for event in month_events:
        events_by_date[event['date_str']].append(event)
    
    # Generate table rows
    for date_str in sorted(events_by_date.keys(), key=lambda d: datetime.strptime(d.split('(')[0].strip(), '%d %b')):
        date_events = events_by_date[date_str]
        
        for i, event in enumerate(date_events):
            if i == 0:
                date_col = date_str
            else:
                date_col = ""
            
            time_col = event['time']
            # Escape ampersands in event type and make it bold
            event_type_escaped = event['type'].replace('&', r'\&')
            # Get subject display with code
            subject_name = event.get('subject_name', '')
            subject_code = event.get('subject_code', '')
            subject_display = f"{subject_name} ({subject_code})" if subject_code else subject_name
            event_desc = f"\\textbf{{{event_type_escaped}}} -- \\textit{{{subject_display}}}"
            room_col = event['room']
            
            lines.append(f"{date_col} & {time_col} & {event_desc} & {room_col} & \\donebox \\\\")
        
        lines.append(r"\midrule")
        lines.append("")
    
    # Remove last midrule and add bottomrule
    if lines[-1] == "":
        lines.pop()
    if lines[-1] == r"\midrule":
        lines.pop()
    
    lines.append(r"\bottomrule")
    lines.append(r"\end{longtable}")
    lines.append("")
    lines.append(r"\vspace{0.5em}")
    lines.append("")
    
    return lines


def generate_exam_period_table(exam_events: List[Dict[str, Any]], subjects: Dict[str, Dict[str, str]]) -> List[str]:
    """
    Generate exam period table.
    
    Args:
        exam_events: List of exam period events
        subjects: Dictionary of subject information
        
    Returns:
        List of LaTeX lines for exam period table (empty list if no exam events)
    """
    if not exam_events:
        return []
    
    lines = []
    lines.append(r"\newpage")
    lines.append(r"% Exam Period")
    lines.append(r"\noindent\textbf{\large Exam Period}")
    lines.append("")
    lines.append(r"\vspace{0.3em}")
    lines.append("")
    lines.append(r"\begin{longtable}{@{} L{2.8cm} M{1.5cm} L{13cm} M{2cm} M{1.8cm} @{}}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Date} & \textbf{Time} & \textbf{Event} & \textbf{Room} & \textbf{Done} \ding{51} \ding{55} \\")
    lines.append(r"\midrule")
    lines.append(r"\endfirsthead")
    lines.append("")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Date} & \textbf{Time} & \textbf{Event} & \textbf{Room} & \textbf{Done} \ding{51} \ding{55} \\")
    lines.append(r"\midrule")
    lines.append(r"\endhead")
    lines.append("")
    
    for event in exam_events:
        subject_key = event['subject']
        subject_info = subjects.get(subject_key, {})
        subject_name = subject_info.get('name', subject_key)
        subject_code = subject_info.get('code', '')
        subject_display = f"{subject_name} ({subject_code})" if subject_code else subject_name
        room = event.get('room') or subject_info.get('default_room', '')
        
        # Escape ampersands in event type and make it bold
        event_type_escaped = event['type'].replace('&', r'\&')
        event_desc = f"\\textbf{{{event_type_escaped}}} -- \\textit{{{subject_display}}}"
        lines.append(f"{event['date']} & {event.get('time', '')} & {event_desc} & {room} & \\donebox \\\\")
    
    lines.append(r"\bottomrule")
    lines.append(r"\end{longtable}")
    lines.append("")
    
    return lines
