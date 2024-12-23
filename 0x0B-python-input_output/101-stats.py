
"""
Created on Mon Dec 23 05:50:52 2024

@author: Albert Mwanza
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Reads stdin line by line and computes metrics.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Statistics printed after every 10 lines and upon keyboard interruption:
- Total file size: sum of all file sizes from input lines.
- Number of lines by status code in ascending order.
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-23"
__version__ = "1.1"


# Initialize metrics
total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Print the collected statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    import sys
    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.strip().split()
                # Extract file size and status code
                file_size = int(parts[-1])
                status_code = parts[-2]

                # Update total file size
                total_size += file_size

                # Update status code counts
                if status_code in valid_status_codes:
                    if status_code not in status_counts:
                        status_counts[status_code] = 0
                    status_counts[status_code] += 1

            except (IndexError, ValueError):
                # Ignore lines that don't conform to the expected format
                continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats()
        raise

    # Final stats print
    print_stats()
