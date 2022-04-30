import heapq
import itertools

from typing import Dict, List, Tuple
from collections import defaultdict

from file import File

def find_unique_releases(files: List[File]) -> Dict[str, List[File]]:
    group_by_release_branch = defaultdict(list)
    for file in files:
        group_by_release_branch[file.branch_name()].append(file)
    return group_by_release_branch

def apply_ttl(files: List[File], ttl_config: Dict[str, int], default_ttl: int) -> List[File]:
    """
    ttl_config will be applied on the latest release, rest will
    be set to the default.
    """
    group_by_release_branch = find_unique_releases(files)
    for release, files in group_by_release_branch.items():
        heapq.heapify(files)
        # apply given ttl_config for latest release which will be in 0th index.
        files[0].ttl = ttl_config.get(release, default_ttl) + files[0].modified_time
        # rest of the files will be set to default_ttl.
        for f in files[1:]:
            f.ttl = default_ttl + f.modified_time
    return itertools.chain(*group_by_release_branch.values())
