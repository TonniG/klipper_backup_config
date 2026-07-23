>>> import sys

>>> config_file_path = '/home/biqu/printer_data/config/printer.cfg'
... 
... def modifyLine(mode):
...     
...     with open(config_file_path, 'r') as f:
...         lines = f.readlines()
... 
...     include_lines = ''
... 
...     if mode =="CUT" or mode =="C":
...         include_lines = ['[include 3DPrint.cfg]\n', '#[include PolyCut.cfg]\n']
...         print("Mode changed to CUT")
...     elif mode =="PRINT" or mode =="P":
...         include_lines = ['#[include 3DPrint.cfg]\n', '[include PolyCut.cfg]\n']
...         print("Mode changed to PRINT")
... 
...     with open(config_file_path, 'w') as f:
...         for line in lines:
...             if line in include_lines:
...                 line = line.lstrip('#') if line.startswith('#') else '#' + line
...             f.write(line)
... 
... if __name__ == "__main__":
...     # Check if at least one command-line argument is provided
...     if len(sys.argv) < 2:
...         print("Usage: python myscript.py <your_variable>")
...         sys.exit(1)
...         
...     mode:str = sys.argv[1]
... 
...     modifyLine(mode.upper())
