#!/usr/bin/env python3
"""
LaTeX Header Generator
Generates the LaTeX document preamble and header configuration
"""

from typing import List


def generate_latex_header() -> List[str]:
    """
    Generate LaTeX document header with all required packages and configurations.
    
    Returns:
        List of LaTeX header lines
    """
    lines = []
    lines.append(r"\documentclass[landscape,a4paper,10pt]{article}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[margin=1.5cm]{geometry}")
    lines.append(r"\usepackage{longtable}")
    lines.append(r"\usepackage{array}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{enumitem}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage{hyperref}")
    lines.append(r"\usepackage{pifont}")
    lines.append(r"\usepackage{tikz}")
    lines.append(r"\usetikzlibrary{calendar,shapes.geometric}")
    lines.append("")
    lines.append(r"% Configure hyperref")
    lines.append(r"\hypersetup{")
    lines.append(r"    colorlinks=false,")
    lines.append(r"    pdfborder={0 0 0}")
    lines.append(r"}")
    lines.append("")
    lines.append(r"% Remove page numbers")
    lines.append(r"\pagestyle{empty}")
    lines.append("")
    lines.append(r"% Adjust spacing")
    lines.append(r"\setlength{\parindent}{0pt}")
    lines.append(r"\setlength{\parskip}{0pt}")
    lines.append("")
    lines.append(r"% Add extra row spacing for tables")
    lines.append(r"\renewcommand{\arraystretch}{1.5}")
    lines.append("")
    lines.append(r"% Define column types")
    lines.append(r"\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}")
    lines.append(r"\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}")
    lines.append(r"\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}")
    lines.append("")
    lines.append(r"% Define clickable checkboxes with custom symbols")
    lines.append(r"% Using checkboxsymbol parameter: \ding{51} for checkmark, \ding{55} for cross")
    lines.append(r"\newcommand{\donebox}{%")
    lines.append(r"    \makebox[2cm][c]{%")
    lines.append(r"        \CheckBox[name=done\thedone,width=0.35cm,height=0.35cm,borderwidth=1,bordercolor=0 0 0,checkboxsymbol=\ding{51}]{}%")
    lines.append(r"        \hspace{0.35cm}%")
    lines.append(r"        \CheckBox[name=notdone\thedone,width=0.35cm,height=0.35cm,borderwidth=1,bordercolor=0 0 0,checkboxsymbol=\ding{55}]{}%")
    lines.append(r"    }%")
    lines.append(r"    \stepcounter{done}%")
    lines.append(r"}")
    lines.append(r"\newcounter{done}")
    lines.append("")
    lines.append(r"% Define macro for event day styling")
    lines.append(r"\newcommand{\eventday}[1]{%")
    lines.append(r"  if (equals=#1) [nodes={draw=red, circle, very thick, minimum width=1.3em, minimum height=1.3em, inner sep=0pt}]%")
    lines.append(r"}")
    lines.append("")
    return lines
