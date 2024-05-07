import os

def deletion(force=False):
    """
    This function lets you delete all the files with user specified extension within a user specified path.

    Input:
    force - skips the prompt if set to True.

    Output:
    boolean value - True if succeeded, False if failed.
    """
    path = str(input("Wybierz sciezke do folderu, z ktorego chcesz usunac pliki: ")) # ./wazne
    extension = str(input("Wybierz rozszerzenie, dla ktorego chcesz usunac pliki: ")) # txt

    try:
        dir = os.listdir(path)
    except FileNotFoundError:
        print("Nie znaleziono folderu.")
        return False
    
    print(dir)

deletion()