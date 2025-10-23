import pathlib
import zipfile


def make_archive(filepathes,dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepathes:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(['/home/vv/PycharmProjects/AandP-2025/cli.py',
                  '/home/vv/PycharmProjects/AandP-2025/gui.py','b1.txt'],
                 '/home/vv/PycharmProjects/AandP-2025/bonuses')