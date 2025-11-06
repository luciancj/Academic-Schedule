#!/usr/bin/env python3
"""
Calendar Generator
Generates mini calendar visualizations with event highlighting
"""

from datetime import date
from typing import List, Set, Dict, Any


def generate_calendars(months: List[Dict[str, Any]], event_dates: Set[date]) -> List[str]:
    """
    Generate mini calendars section with highlighted event days.
    
    Args:
        months: List of month dictionaries (year, month, name, date_obj)
        event_dates: Set of dates with scheduled events
        
    Returns:
        List of LaTeX lines for calendar section
    """
    lines = []
    lines.append(r"% Mini Calendars")
    lines.append(r"\begin{center}")
    lines.append(r"\begin{tikzpicture}[every calendar/.style={")
    lines.append(r"    week list, ")
    lines.append(r"    month label above centered, ")
    lines.append(r"    month text=\textbf{\%mt \%y0},")
    lines.append(r"    day xshift=2.2em,")
    lines.append(r"    day yshift=1.8em")
    lines.append(r"}]")
    lines.append("")
    
    for idx, month in enumerate(months):
        lines.append(f"% {month['name']} {month['year']}")
        
        # Position calculation (3 calendars per row)
        x_pos = (idx % 3) * 10
        y_pos = -(idx // 3) * 10
        
        at_clause = f", at={{({x_pos}cm,{y_pos}cm)}}" if idx > 0 else ""
        
        lines.append(f"\\calendar[dates={month['year']}-{month['month']:02d}-01 to {month['year']}-{month['month']:02d}-last, name={month['name'].lower()}{at_clause},")
        lines.append(r"          every day/.style={anchor=base}]")
        
        # Add event days for this month
        for event_date in sorted(event_dates):
            if event_date.year == month['year'] and event_date.month == month['month']:
                lines.append(f"  \\eventday{{{event_date.year}-{event_date.month:02d}-{event_date.day:02d}}}")
        
        lines.append(";")
        lines.append("")
    
    lines.append(r"\end{tikzpicture}")
    lines.append("")
    lines.append(r"\vspace{0.5em}")
    lines.append("")
    lines.append(r"\small{\textit{Red circles indicate days with scheduled events}}")
    lines.append(r"\end{center}")
    lines.append("")
    lines.append(r"\vspace{0.8em}")
    lines.append("")
    
    return lines
