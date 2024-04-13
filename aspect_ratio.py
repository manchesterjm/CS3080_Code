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

    # Return the aspect ratio as a tuple
    return (width // ratio_gcd, height // ratio_gcd)

# Get and print the aspect ratio
aspect_ratio = get_screen_aspect_ratio()
print(f"Aspect Ratio: {aspect_ratio[0]}:{aspect_ratio[1]}")
