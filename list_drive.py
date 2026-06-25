import os
from pathlib import Path

def list_directory(path, max_depth=2, current_depth=0, prefix=""):
    """
    Rekurzívan kilistázza a könyvtárat a megadott mélységig.
    
    Args:
        path: Az elérési út
        max_depth: Maximális mélység
        current_depth: Jelenlegi mélység
        prefix: Indentálás előtag
    """
    if current_depth > max_depth:
        return
    
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(f"{prefix}[Hozzáférés megtagadva]")
        return
    except Exception as e:
        print(f"{prefix}[Hiba: {e}]")
        return
    
    for item in items:
        item_path = os.path.join(path, item)
        indent = "  " * current_depth
        
        if os.path.isdir(item_path):
            print(f"{indent}📁 {item}/")
            # Rekurzív hívás következő mélységre
            if current_depth < max_depth:
                list_directory(item_path, max_depth, current_depth + 1, indent + "  ")
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    drive = "C:\\"
    print(f"C: meghajtó listázása 2 mélységig:\n")
    list_directory(drive, max_depth=2)
