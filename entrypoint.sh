#!/bin/bash
set -e

echo "Python version:"
python --version

echo "Pip list:"
pip list

echo "Uvicorn location:"
which uvicorn

echo "Starting application..."
exec uvicorn main:app --host 0.0.0.0 --port $PORT