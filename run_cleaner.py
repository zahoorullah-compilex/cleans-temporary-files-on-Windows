from clear_temp import clear_temp
from notify import notify_user

if __name__ == "__main__":
    files, folders, freed_mb = clear_temp()
    message = f"Deleted {files} files, {folders} folders\nFreed {freed_mb:.2f} MB"
    notify_user("Temp Cleanup Complete", message)
