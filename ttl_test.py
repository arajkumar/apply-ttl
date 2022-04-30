from file import File
from ttl import apply_ttl

# 1. Find latest build in each unique branch
# 2. Implement TTL based on given config

import unittest

class TestApplyTTL(unittest.TestCase):
    def test_ttl(self):
        for files, ttl_config, expected in (
                (
                    [
                        File(path="/a/b/c/8.3.0.cl-100.tar.gz", modified_time=100),
                        File(path="/a/b/c/8.3.0.cl-101.tar.gz", modified_time=101),
                        File(path="/a/b/c/8.3.0.cl-102.tar.gz", modified_time=102),
                        File(path="/a/b/c/8.3.1.cl-102.tar.gz", modified_time=103),
                        File(path="/a/b/c/8.3.1.cl-105.tar.gz", modified_time=105),
                    ], {
                        "8.3.0.cl": 100,
                        "8.3.1.cl": 110,
                    },
                    [
                        File(path="/a/b/c/8.3.0.cl-100.tar.gz", modified_time=100, ttl=150),
                        File(path="/a/b/c/8.3.0.cl-101.tar.gz", modified_time=101, ttl=151),
                        File(path="/a/b/c/8.3.0.cl-102.tar.gz", modified_time=102, ttl=202),
                        File(path="/a/b/c/8.3.1.cl-102.tar.gz", modified_time=103, ttl=153),
                        File(path="/a/b/c/8.3.1.cl-105.tar.gz", modified_time=105, ttl=215),
                    ],
                ),
        ):
            actual = apply_ttl(files, ttl_config, 50)
            expected = sorted(expected)
            actual = sorted(actual)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
