#!/usr/bin/env python3
"""
PDF Compiler
Handles compilation of LaTeX to PDF with loading bar
"""

import subprocess
import sys
import time
import os
from . import config


def compile_pdf(tex_file: str) -> bool:
    """
    Compile LaTeX file to PDF with loading bar.
    
    Args:
        tex_file: Path to the .tex file to compile
        
    Returns:
        True if compilation successful, False otherwise
    """
    print("\nCompiling PDF...")
    
    # Get directory and filename
    tex_dir = os.path.dirname(tex_file) or '.'
    tex_filename = os.path.basename(tex_file)
    
    # Start compilation in the correct directory
    compile_process = subprocess.Popen(
        [config.PDF_COMPILER] + config.PDF_COMPILER_OPTIONS + [tex_filename],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        cwd=tex_dir
    )
    
    # Show loading bar while compiling
    bar_length = config.LOADING_BAR_LENGTH
    while compile_process.poll() is None:
        for i in range(bar_length):
            if compile_process.poll() is not None:
                break
            percent = (i / bar_length) * 100
            filled = config.LOADING_BAR_FILLED_CHAR * i
            empty = config.LOADING_BAR_EMPTY_CHAR * (bar_length - i)
            sys.stdout.write(f'\r{filled}{empty} {percent:.0f}%')
            sys.stdout.flush()
            time.sleep(config.LOADING_BAR_DELAY)
    
    # Show 100% completion
    sys.stdout.write(f'\r{config.LOADING_BAR_FILLED_CHAR * bar_length} 100%\n')
    sys.stdout.flush()
    
    # Check if PDF was created
    base_name = tex_file.replace('.tex', '')
    pdf_file = f"{base_name}.pdf"
    
    if os.path.exists(pdf_file):
        print(f"PDF compiled: {pdf_file}")
        
        # Clean up auxiliary files
        for ext in config.AUX_FILE_EXTENSIONS:
            aux_file = f"{base_name}{ext}"
            if os.path.exists(aux_file):
                os.remove(aux_file)
        print(f"Cleaned up auxiliary files ({', '.join(config.AUX_FILE_EXTENSIONS)})")
        return True
    else:
        print("PDF compilation failed")
        return False
