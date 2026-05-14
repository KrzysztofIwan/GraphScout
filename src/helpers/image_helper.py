from pathlib import Path

def get_latest_file(folder_path):
    path = Path(folder_path)
    
    # Pobranie wszystkich plików z rozszerzeniem .png
    files = list(path.glob('*.png'))
    
    if not files:
        return None
    
    # Znalezienie pliku z najpóźniejszą datą modyfikacji
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    
    return latest_file