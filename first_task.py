import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def copy_files_in_directory(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            extension = os.path.splitext(file)[1]
            target_folder = os.path.join(target_dir, extension.strip('.'))
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            target_file = os.path.join(target_folder, file)
            shutil.copy2(source_file, target_file)
            print(f"Copied {source_file} to {target_file}")


def process_directory(source_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        executor.submit(copy_files_in_directory, source_dir, target_dir)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python program.py <source_dir> [target_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' not found.")
        sys.exit(1)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    process_directory(source_dir, target_dir)

