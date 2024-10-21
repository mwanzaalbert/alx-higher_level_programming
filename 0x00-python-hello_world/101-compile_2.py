#!/bin/bash
# A script to compile a Python script from an environment variable

# Check if PYFILE is set
if [ -z "$PYFILE" ]; then
  echo "Error: PYFILE environment variable is not set."
  exit 1
fi

# Check if PYFILE has a .py extension
if [[ "$PYFILE" != *.py ]]; then
  echo "Error: PYFILE does not have a .py extension."
  exit 1
fi

# Get the base filename without the extension
BASENAME=$(basename "$PYFILE" .py)

# Compile the Python file using compileall
python3 -m compileall -l -b -f -d . "$PYFILE"

# Find the generated .pyc file in __pycache__ and move it
PYC_FILE=$(find __pycache__ -name "${BASENAME}.cpython-*.pyc")

if [ -f "$PYC_FILE" ]; then
  mv "$PYC_FILE" "./${BASENAME}.pyc"
  echo "Compilation successful: ${BASENAME}.pyc created."
else
  echo "Compilation failed."
  exit 1
fi

# Clean up the __pycache__ directory
rmdir __pycache__
