import os

def deletion(prompt=True):
    """
    This function lets you delete all the files with user specified extension within a user specified path.

    Input:
    prompt - skips the prompt if set to False.

    Output:
    boolean value - True if succeeded, False if failed.
    """
    path = str(input("Wybierz sciezke do folderu, z ktorego chcesz usunac pliki: ")) # ./wazne
    extension = str(input("Wybierz rozszerzenie, dla ktorego chcesz usunac pliki: ")) # txt lub .txt

    if extension[0] == ".": # also works if user adds a "." before the extension
        extension = extension[1::]

    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("Nie znaleziono folderu.")
        return False
        
    if prompt:
        full_files = []

        for file in files:
            if file.endswith(f'.{extension}'):
                full_files.append(file)

        deletion = input(f'Czy jestes pewien, ze chcesz usunac te pliki: {full_files} [y/n]: ')
        
        if deletion == 'y':
            for file in files:
                if file.endswith(f".{extension}"):
                    os.remove(os.path.join(path, file))

        else:
            print("Przerwano.")
            return False
        
    else:
        for file in files:
                if file.endswith(f".{extension}"):
                    os.remove(os.path.join(path, file))

    print(f"Pomyslnie pliki o rozszerzeniu .{extension} ze sciezki {path}.")

deletion()