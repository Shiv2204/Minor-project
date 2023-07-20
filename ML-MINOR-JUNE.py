import time
import threading

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining_time = duration
        self.is_running = False
        self.is_paused = False

    def start(self):
        self.is_running = True
        self.is_paused = False
        self._countdown()

    def reset(self):
        self.is_running = False
        self.is_paused = False
        self.remaining_time = self.duration

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        self._countdown()

    def _countdown(self):
        while self.remaining_time > 0 and self.is_running:
            if not self.is_paused:
                print(f"Time remaining: {self.remaining_time} seconds")
                self.remaining_time -= 1
                time.sleep(1)
            else:
                time.sleep(1)

        if self.is_running:
            print("Countdown completed!")
            self.is_running = False

if __name__ == "__main__":
    duration = 60  # Change this to set the countdown duration in seconds

    timer = CountdownTimer(duration)

    print("Starting countdown...")
    timer.start()

    # Simulate using the timer for a while
    time.sleep(5)

    print("\nPausing countdown...")
    timer.pause()

    # Simulate a pause for a few seconds
    time.sleep(3)

    print("\nResuming countdown...")
    timer.resume()

    # Simulate using the timer for a while again
    time.sleep(10)

    print("\nStopping and resetting the countdown...")
    timer.reset()
