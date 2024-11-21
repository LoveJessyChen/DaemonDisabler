from sys import platform
import shutil
import subprocess
import PyInstaller.__main__
import os

def universal2():
    python_path = shutil.which("python3")
    arch = subprocess.run(['file', python_path], capture_output=True, text=True)
    return 'arm64' in arch.stdout and 'x86_64' in arch.stdout

def get_version():
    git_dir = '.git'
    head_file = os.path.join(git_dir, 'HEAD')
    tags_dir = os.path.join(git_dir, 'refs', 'tags')
    if os.path.isdir(tags_dir):
        tags = os.listdir(tags_dir)
        if tags:
            latest_tag = sorted(tags)[-1]
            return latest_tag
    if os.path.exists(head_file):
        with open(head_file, 'r') as f:
            ref_line = f.readline().strip()
            if ref_line.startswith('ref:'):
                ref_path = ref_line.split(' ')[1]
                commit_hash_file = os.path.join(git_dir, ref_path)
                if os.path.exists(commit_hash_file):
                    with open(commit_hash_file, 'r') as commit_file:
                        return commit_file.readline().strip()[:7]
            else:
                return ref_line[:7]
    return ""

def version_file():
    version = get_version()
    os.makedirs('./build', exist_ok=True)
    with open('./build/version', 'w') as file:
        file.write(version)

version_file()

args = [
    'gui_app.py',
    '--hidden-import=zeroconf',
    '--hidden-import=zeroconf._utils.ipaddress',
    '--hidden-import=zeroconf._handlers.answers',
    '--name=DaemonDisabler',
    '--windowed',
    '--icon=./icon/icon.ico',
    '--add-data=./build/version:.',
    '--noconfirm'
]


if platform == "darwin":
    args.append('--onedir')
    if universal2():
        args.append('--target-arch=universal2')
else:
    args.append('--onefile')

PyInstaller.__main__.run(args)

if platform == "darwin":
    shutil.rmtree('./dist/_internal', ignore_errors=True)
    shutil.rmtree('./dist/DaemonDisabler', ignore_errors=True)
os.remove('./build/version')