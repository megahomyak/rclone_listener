import subprocess
from pathlib import Path
from watchfiles import watch

RCLONE_FLAGS = [
    "--links",
    "--progress",
    "--fast-list",
    "--transfers", "20",
    "--checkers", "20",
    "-vvv",
    "--metadata"
]

REMOTES = [
    "yadisk_crypt:",
    "server_crypt:",
]

BASE_DIR = Path.home().absolute() / "i"

for changes in watch('.'):
    for change in changes:
        change_type, file_path = change
        file_path = str(Path(file_path).relative_to(BASE_DIR))
        for remote in REMOTES:
            subprocess.run([
                "rclone",
                "sync",
                BASE_DIR,
                remote,
                *RCLONE_FLAGS,
                "--include",
                file_path,
            ])
