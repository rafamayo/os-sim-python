"""Simple utility to execute a notebook and report errors (uses nbclient)."""
import sys
from nbclient import NotebookClient
import nbformat

def run_notebook(path):
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=600)
    client.execute()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python tools/run_notebook_check.py notebooks/your.ipynb')
        sys.exit(2)
    path = sys.argv[1]
    try:
        run_notebook(path)
        print('Notebook executed successfully.')
    except Exception as e:
        print('Notebook execution failed:', e)
        raise
