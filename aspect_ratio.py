import ctypes

def get_screen_aspect_ratio():
    # Function to calculate the greatest common divisor
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # Get screen width
    width = ctypes.windll.user32.GetSystemMetrics(0)
    # Get screen height
    height = ctypes.windll.user32.GetSystemMetrics(1)

    # Calculate GCD of the screen dimensions
    ratio_gcd = gcd(width, height)

    # Normalize the width with respect to the height
    normalized_width = width / height  # Use floating-point division

    # Format the result to 2 decimal places
    return f"{normalized_width:.2f}:1"

# Get and print the aspect ratio
aspect_ratio = get_screen_aspect_ratio()
print(f"Aspect Ratio: {aspect_ratio}")
