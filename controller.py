from pyfirmata import Arduino, util

# Define the COM port
board = Arduino('COM9')

# Define LED pins
led_pins = [10, 9, 6, 5, 3]
leds = [board.get_pin(f'd:{pin}:p') for pin in led_pins]

def leds(total, intensity):
    """Control LEDs based on the total count and intensity."""
    intensity = max(0, min(1, intensity))  # Ensure intensity is within 0-1

    for i in range(len(leds)):
        if i < total:
            leds[i].write(intensity)
        else:
            leds[i].write(0)
