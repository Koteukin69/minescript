# Key Functions to Use:
# look_at_block(x, y, z, ...): This is the best function for looking at a block, as it automatically targets the center of the block by adding 0.5 to the coordinates (e.g., 23.5, 54.5, 223.5).
# look_at(x, y, z, ...): Use this when you need to look at an exact point that is not the center of a block (e.g., an entity's head or a specific coordinate).
# speed: A higher value makes the movement faster. speed=N means 360 degree in N sec. 
# func: Allows you to change the smoothing effect:
# easeInOut (default): Slow start, fast middle, slow end (smooth).
# linear: Constant speed (no easing).
# easeOutQuad: Fast start, slow end.

from smooth_look import look_at, look_at_block, easeOutQuad #save the file into minescript folder as smooth_look.py

# --- Coordinates you want to look at ---
TARGET_X = 23
TARGET_Y = 54
TARGET_Z = 223

# --- Example 1: Look at the center of the block (23, 54, 223) ---
# This uses the look_at_block function, which is often the most convenient.
# Arguments: X, Y, Z, Speed (default=1), EasingFunction (default=easeInOut)
# Use the default speed and the default easeInOut curve
look_at_block(TARGET_X, TARGET_Y, TARGET_Z)


# --- Example 2: Look at a specific point with custom speed and easing ---

# Look at the bottom-front-left corner of the block
TARGET_POINT_X = 23.1
TARGET_POINT_Y = 54.0
TARGET_POINT_Z = 223.9

# Use a faster speed (e.g., 2.5) and the easeOutQuad function
print(f"Looking at the exact point ({TARGET_POINT_X}, {TARGET_POINT_Y}, {TARGET_POINT_Z}) quickly...")
look_at(TARGET_POINT_X, TARGET_POINT_Y, TARGET_POINT_Z, speed=2.5, func=easeOutQuad)


# --- Example 3: Smoothly rotate the player's view relative to current orientation ---
# Rotate 90 degrees to the right (Yaw) and 15 degrees up (Pitch) over 2 seconds.

print("Rotating 90 degrees right and 15 degrees up...")

# Note: The time taken is dependent on the rotation magnitude and speed.
# A speed of 1 is roughly 360 degrees per unit time.
from player_movement import rotate_releative
rotate_releative(x=90, y=15, speed=1)

