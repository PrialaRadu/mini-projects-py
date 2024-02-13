# System notification that alerts the user if battery is running low

# Used for retrieving battery information
import psutil
# Used for sending a system notification
from plyer import notification

# Retrieves information about the battery
my_battery = psutil.sensors_battery()


# Checks if the battery percentage is lower than 25. Displays a system notification
# with information about the low battery percentage and remaining time left.
def battery_notification(battery):
    if battery.percent < 25:
        notification.notify(
            title="Low Battery",
            message=f"Your Battery is running low. Percentage: {battery.percent}."
                    f"Time left: {int(battery.secsleft / 60)} minutes.",
            timeout=5
        )


battery_notification(my_battery)
