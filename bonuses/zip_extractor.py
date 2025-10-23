import zipfile

def extract_archive(archpath, dest_dir):
    with zipfile.ZipFile(archpath, 'r') as archive:
        archive.extractall(dest_dir)