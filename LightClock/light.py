
from dataclasses import dataclass
import numpy as np

@dataclass
class LightClock:
    def __init__(self, d, v):
        d: float # Distance between mirrors (meters)
        v: float # Velocity of moving clock (m/s)
        c: float # Speed of light (m/s)

def stationary_time(self) -> float:
    # Calc the time for the photon to travel in the stationary frame
    return self.d / self.c

def compute_light_path(d: float, v: float, c: float) -> float:
    # Using the formula for the hypotenuse of the light's path in the moving frame
    time_in_moving_frame = d / np.sqrt(c**2 - v**2)



