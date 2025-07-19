import os

## a helper for loading stylesheets.
def load_stylesheet(filename):
    try:
        dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(dir, filename)

        with open(full_path, "r") as f:
            return f.read()
        
    except FileNotFoundError:
        print(f"Stylesheet '{filename}' not found.")
        return ""