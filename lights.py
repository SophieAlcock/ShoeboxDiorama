
from ledtheatre import init, Sequence

try:
    # Initialise
    from Adafruit_PCA9685 import PCA9685
    init(PCA9685(), pull_up=True)
except ImportError:
    # This is not important - ledtheatre will issue a warning later
    # We will fall back to simulating the PCA9685
    pass
  
WHITE = 0
BLUE = 1
YELLOW = 2
ALL = [WHITE, BLUE, YELLOW]

daysequence = Sequence() \
    .snap().led(ALL, 0) \
    .transition(1.5).led(YELLOW, 1) \
    .sleep(2) \
    .transition(1.5).led(YELLOW, 0.3).led(BLUE, 0.5) \
    .transition(1.5).led(YELLOW, 0).led(BLUE, 1).led(WHITE, 1) \
    .sleep(2) \
    .transition(1.5).led(BLUE, 0).led(WHITE, 0)

# Run our Sequence
daysequence.execute()
