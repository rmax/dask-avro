import sys

import dask.bag

from dask_avro import read_avro
from dask.diagnostics import progress


def main():
    if not sys.argv[1:]:
        sys.stderr.write("Usage: python %s <avro file>\n" % sys.argv[0])
        sys.exit(1)

    data = dask.bag.from_delayed(read_avro(sys.argv[1], blocksize=1024 * 1024))
    print("Partitions: %s" % data.npartitions)

    task = data.count()
    with progress.ProgressBar():
        count = task.compute()

    print("Result: %s" % count)


if __name__ == "__main__":
    main()
