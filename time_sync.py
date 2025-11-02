"""
Windows time synchronization utility.

This module forces Windows to synchronize its system time with the
configured time server using the w32tm command.
"""

import subprocess
import time


def sync_time() -> None:
    """
    Execute Windows time synchronization command.

    Uses the w32tm utility to force time resynchronization with the
    configured time server.

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If time sync command fails
    """
    try:
        # Command to force time synchronization
        subprocess.run(
            ['w32tm', '/resync'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print("Time synchronization command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(e.stdout.decode())
        print(e.stderr.decode())


def main() -> None:
    """
    Run time synchronization and wait for completion.

    Returns:
        None
    """
    sync_time()
    time.sleep(30)


if __name__ == '__main__':
    main()
