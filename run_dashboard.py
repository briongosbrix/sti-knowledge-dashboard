#!/usr/bin/env python
"""
Launch script for the STI Knowledge Research Dashboard
This script adds the roaming Python packages to sys.path before importing streamlit
"""

import sys
import os

# Add the roaming Python packages directory to path
roaming_path = os.path.expanduser(r'~\AppData\Roaming\Python\Python311\site-packages')
if roaming_path not in sys.path:
    sys.path.insert(0, roaming_path)

# Now import and run streamlit
import streamlit.cli as stcli

if __name__ == '__main__':
    sys.argv = ['streamlit', 'run', 'app.py']
    stcli.main()
