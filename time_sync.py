import subprocess, time

def sync_time():
    try:
        # Command to force time synchronization
        subprocess.run(['w32tm', '/resync'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print("Time synchronization command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(e.stdout.decode())
        print(e.stderr.decode())

# Run the time synchronization function
sync_time()

time.sleep(30)