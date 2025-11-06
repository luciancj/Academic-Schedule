#!/usr/bin/env python3
"""
Modular Schedule Generator from JSON Data
Reads schedule_data.json and generates Schedule.tex

This is the refactored version with separated modules for better organization.
"""

import sys
import os
from typing import Optional

from src import (
    load_schedule_data,
    get_event_dates,
    get_calendar_months,
    group_events_by_month,
    generate_latex_header,
    generate_calendars,
    generate_month_table,
    generate_exam_period_table,
    compile_pdf,
)


def generate_latex_from_json(json_file: str = 'schedule_data.json', output_file: str = 'Academic Schedule.tex') -> str:
    """
    Main function to generate LaTeX from JSON.
    
    Args:
        json_file: Path to input JSON file with schedule data
        output_file: Path to output .tex file
        
    Returns:
        Path to the generated .tex file
        
    Raises:
        FileNotFoundError: If JSON file doesn't exist
        ValueError: If JSON data is invalid or missing required fields
    """
    print(f"Reading {json_file}...")
    data = load_schedule_data(json_file)
    
    schedule_info = data['schedule_info']
    subjects = data['subjects']
    events = data['events']
    
    print(f"Loaded {len(events)} events and {len(subjects)} subjects")
    
    # Get event dates and months
    event_dates = get_event_dates(events)
    months = get_calendar_months(schedule_info['start_date'], schedule_info['end_date'])
    
    print(f"Schedule spans {len(months)} months")
    
    # Group events
    events_by_month, exam_events = group_events_by_month(events, subjects)
    
    print(f"Events grouped by month")
    
    # Start generating LaTeX
    latex_lines = []
    
    # Header
    latex_lines.extend(generate_latex_header())
    
    # Begin document
    latex_lines.append(r"\begin{document}")
    latex_lines.append(r"\begin{Form}")
    latex_lines.append("")
    
    # Title
    latex_lines.append(r"\begin{center}")
    latex_lines.append(f"{{\\LARGE\\bfseries {schedule_info['title']}}}\\\\[0.2em]")
    latex_lines.append(f"{{\\large {schedule_info['period']}}}")
    latex_lines.append(r"\end{center}")
    latex_lines.append("")
    latex_lines.append(r"\vspace{0.5em}")
    latex_lines.append("")
    
    # Calendars
    latex_lines.extend(generate_calendars(months, event_dates))
    
    # Month tables
    first_table = True
    for month in months:
        month_key = (month['year'], month['month'])
        if month_key in events_by_month:
            month_events = events_by_month[month_key]
            latex_lines.extend(generate_month_table(month['name'], month['year'], month_events, subjects, first_table))
            first_table = False
    
    # Exam period
    latex_lines.extend(generate_exam_period_table(exam_events, subjects))
    
    # End document
    latex_lines.append(r"\end{Form}")
    latex_lines.append(r"\end{document}")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(latex_lines))
    
    print(f"\nGenerated {output_file}")
    print(f"Total lines: {len(latex_lines)}")
    return output_file


if __name__ == "__main__":
    json_file = sys.argv[1] if len(sys.argv) > 1 else 'schedule_data.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'Academic Schedule.tex'
    
    try:
        # Generate LaTeX from JSON
        generate_latex_from_json(json_file, output_file)
        
        # Automatically compile PDF
        success = compile_pdf(output_file)
        if not success:
            sys.exit(1)
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Please ensure '{json_file}' exists in the current directory.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please check your JSON file structure and field values.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing required field in JSON: {e}")
        print("Please verify all required fields are present in your JSON file.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Please check your input files and try again.")
        sys.exit(1)
