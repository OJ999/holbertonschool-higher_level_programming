#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    """
    Print the computed metrics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of each status code.
    """
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{:d}: {:d}".format(status_code, status_counts[status_code]))

def parse_line(line):
    """
    Parse a line of input and extract the status code and file size.

    Args:
        line (str): Input line to parse.

    Returns:
        tuple: A tuple containing the status code (int) and file size (int).
    """
    parts = line.strip().split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
