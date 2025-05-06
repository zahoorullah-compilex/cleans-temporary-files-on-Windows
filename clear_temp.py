import os
import shutil
import tempfile
import platform
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Ensure the script runs only on Windows
if platform.system() != "Windows":
    print("This script is intended for Windows only.")
    exit()

# Rotating log handler
log_file = "cleanup.log"
handler = RotatingFileHandler(log_file, maxBytes=500_000, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s - %(message)s')

def clear_temp():
    temp_dir = tempfile.gettempdir()
    files_deleted = 0
    folders_deleted = 0
    freed_bytes = 0

    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                freed_bytes += os.path.getsize(file_path)
                os.remove(file_path)
                files_deleted += 1
            except PermissionError:
                logging.warning(f"Skipped locked file: {file_path}")
            except Exception as e:
                logging.error(f"Error deleting file: {file_path} - {e}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path, ignore_errors=True)
                folders_deleted += 1
            except Exception as e:
                logging.warning(f"Failed to delete folder: {dir_path} - {e}")

    freed_mb = freed_bytes / (1024 * 1024)
    log_msg = f"Deleted {files_deleted} files, {folders_deleted} folders. Freed {freed_mb:.2f} MB"
    logging.info(log_msg)

    return files_deleted, folders_deleted, freed_mb
