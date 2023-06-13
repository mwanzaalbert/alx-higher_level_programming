#!/usr/bin/python3
def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")

total_size = 0
status_codes = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1

        # Extract relevant information from the input line
        _, _, _, _, _, status_code, file_size = line.strip().split()

        # Update total file size
        total_size += int(file_size)

        # Update status code count
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)
            print()

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
