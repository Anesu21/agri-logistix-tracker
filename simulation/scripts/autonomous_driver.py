import subprocess
import time

TOPIC = "/model/agri_transport_vehicle/cmd_vel"


def publish_velocity(forward, turn):
    command = (
        f'linear: {{x: {forward}}}, '
        f'angular: {{z: {turn}}}'
    )

    subprocess.run(
        [
            "gz", "topic",
            "-t", TOPIC,
            "-m", "gz.msgs.Twist",
            "-p", command
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )


def drive(forward, turn, duration):
    end_time = time.monotonic() + duration

    while time.monotonic() < end_time:
        publish_velocity(forward, turn)
        time.sleep(0.1)


def stop():
    for _ in range(5):
        publish_velocity(0.0, 0.0)
        time.sleep(0.1)

    print("DROID parked.")


try:
    print("DROID starting autonomous route...")

    drive(0.2, 0.0, 2.0)
    drive(0.0, 0.3, 1.5)
    drive(0.2, 0.0, 2.0)
    drive(0.0, -0.3, 1.5)

    stop()
    print("Route complete.")

except KeyboardInterrupt:
    print("\nEmergency stop requested.")
    stop()

except subprocess.CalledProcessError as error:
    print(f"Gazebo command failed: {error}")
    stop()

finally:
    stop()
