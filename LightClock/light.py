# https://docs.google.com/document/d/1cjb8-CP4d1oh7ynYrc7KWYee2rEwxb4PHhxsrHzJ_Ds/edit?tab=t.0#heading=h.s05u5js0hq3u

from dataclasses import dataclass
import numpy as np

# Step 1: Algorithm for Moving Light Clocks (Medium)
@dataclass
class LightClock:
    def __init__(self, d, v):
        d: float # Distance between mirrors (meters)
        v: float # Velocity of moving clock (m/s)
        c: float # Speed of light (m/s)

def stationary_time(self) -> float:
    # Calc the time for the photon to travel in the stationary frame
    return self.d / self.c

# Step 2: Algorithm for Moving Light Clocks (Medium)
def compute_light_path(d: float, v: float, c: float) -> float:
    # Using the formula for the hypotenuse of the light's path in the moving frame
    time_in_moving_frame = d / np.sqrt(c**2 - v**2)
    hypotenuse = np.sqrt((v * time_in_moving_frame) **2 + d ** 2)
    return hypotenuse




