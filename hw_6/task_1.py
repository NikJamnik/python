from colorama import Fore
import time

class TrafficLight:
    color = ''

    def running(self):
        for i in range(1, 8):
            time.sleep(1)
            print(Fore.RED + f"Second {i}")
        for i in range(1, 3):
            time.sleep(1)
            print(Fore.YELLOW + f"Second {i}")
        for i in range(1, 8):
            time.sleep(1)
            print(Fore.GREEN + f"Second {i}")


trafficLight = TrafficLight()
trafficLight.running()
