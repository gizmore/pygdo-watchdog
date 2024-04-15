import argparse
import fnmatch

import psutil
import os
import signal
import time


def monitor_processes(threshold=3.14, all_users=False, pattern="*", warn=False):
    while True:
        # Get list of processes
        if all_users:
            processes = psutil.process_iter()
        else:
            processes = psutil.Process().children()

        # Check CPU usage of each process
        for process in processes:
            try:
                if not fnmatch.fnmatch(process.name(), pattern):
                    continue
                cpu_percent = process.cpu_percent(interval=1.0)
                if cpu_percent > threshold:
                    # Take action based on warn flag
                    if warn:
                        print(f"WARNING: Process {process.pid} exceeded CPU threshold ({cpu_percent}%).")
                    else:
                        print(f"Process {process.pid} exceeded CPU threshold ({cpu_percent}%). Killing...")
                        os.kill(process.pid, signal.SIGKILL)
            except psutil.NoSuchProcess:
                pass

        # Wait for 2 seconds before checking again
        time.sleep(2)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Pygdo - A tool to monitor and manage processes.")
    parser.add_argument("--all", action="store_true", help="Monitor processes for all users.")
    parser.add_argument("--threshold", type=float, default=3.14, help="CPU usage threshold (in %) above which to take action.")
    parser.add_argument("--warn", action="store_true", help="Issue warning instead of killing the process.")
    parser.add_argument("--pattern", help="Pattern of the process names. Defaults to *")
    args = parser.parse_args()

    # Start monitoring processes
    monitor_processes(threshold=args.threshold, all_users=args.all, pattern=args.pattern, warn=args.warn)


if __name__ == "__main__":
    main()
