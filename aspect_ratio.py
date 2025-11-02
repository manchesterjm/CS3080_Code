"""
Screen aspect ratio calculator for Windows.

This module retrieves the screen dimensions using Windows API and calculates
the aspect ratio normalized to the format X.XX:1.
"""

import ctypes


def get_screen_aspect_ratio() -> str:
    """
    Calculate the screen aspect ratio in X.XX:1 format.

    Uses Windows API to retrieve screen dimensions and calculates
    the normalized aspect ratio.

    Returns:
        str: Aspect ratio formatted as "X.XX:1"

    Example:
        >>> ratio = get_screen_aspect_ratio()
        >>> print(ratio)
        '1.78:1'
    """
    # Get screen width
    width = ctypes.windll.user32.GetSystemMetrics(0)
    # Get screen height
    height = ctypes.windll.user32.GetSystemMetrics(1)

    # Normalize the width with respect to the height
    normalized_width = width / height  # Use floating-point division

    # Format the result to 2 decimal places
    return f"{normalized_width:.2f}:1"


def main() -> None:
    """
    Get and display the screen aspect ratio.

    Returns:
        None
    """
    aspect_ratio = get_screen_aspect_ratio()
    print(f"Aspect Ratio: {aspect_ratio}")


if __name__ == '__main__':
    main()
