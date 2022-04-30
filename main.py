import os
import sys
import json

from typing import List

from file import File
from ttl import apply_ttl

_usage = """
Usage:
    python main.py <release_artifact_directory> <ttl_config> <default_ttl_in_seconds>
Example:
    python main.py /mnt/s3/release_artifacts '{"8.3.1.ci": 10, "8.3.2.ci": 100}' 100
"""
def main():
    if len(sys.argv) < 3:
        print("Missing argument: release_artifact_directory or ttl_config")
        print(_usage)
        sys.exit(-1)

    if len(sys.argv) == 4:
        default_ttl = int(sys.argv[3])
    else:
        default_ttl = 50

    try:
        ttl_config = json.loads(sys.argv[2])
    except Exception as e:
        print(e)
        print(sys.argv[2])
        print("Unable to parse ttl_config, it must be in json format.")
        sys.exit(-2)

    file_obj: List[File] = []
    for root_path, _, files in os.walk(sys.argv[1]):
        for file in files:
            file = os.path.join(root_path, file)
            file_obj.append(File(path=file, modified_time=os.path.getmtime(file)))

    files_with_ttl = apply_ttl(file_obj, ttl_config, default_ttl)

    for f in files_with_ttl:
        print(f"{f.path}: {f.ttl}")

if __name__ == '__main__':
    main()
