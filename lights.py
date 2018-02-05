
from ledtheatre import init, Sequence

try:
    # Initialise
    from Adafruit_PCA9685 import PCA9685
    init(PCA9685(), pull_up=True)
except ImportError:
    # This is not important - ledtheatre will issue a warning later
    # We will fall back to simulating the PCA9685
    pass
  
ALL = [0, 1, 2]

daysequence = Sequence() \
    .snap().led(ALL, 0) \
    .transition(0.5).led(0, 1) \
    .transition(1).led(1, 1).led(0, 0) \ 
    .transition(0.5).led(1, 0) \
    .sleep(1) \
    .snap().led(ALL, 1) \
    .sleep(0.2) \
    .snap().led(ALL, 0)

# Run our Sequence
daysequence.execute()
