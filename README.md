# apply-ttl

Small utility which dumps TTL value based on the given config.

# Usage

```sh
Usage:
    python main.py <release_artifact_directory> <ttl_config> <default_ttl_in_seconds>
Example:
    python main.py /mnt/s3/release_artifacts '{"8.3.1.ci": 10, "8.3.2.ci": 100}' 100
```

```sh
python main.py /tmp/test '{"7.1.1": 500}'
/tmp/test/8.0-725.tar.gz: 1651328050.5499382
/tmp/test/8.0-720.tar.gz: 1651328050.5246987
/tmp/test/8.0-723.tar.gz: 1651328050.539679
/tmp/test/7.1.1-162.tar.gz: 1651328500.565001
```

# Run tests
```sh
python ttl_test.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
