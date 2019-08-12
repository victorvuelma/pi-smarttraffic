from time import sleep

from smarttraffic.manager import manager
from smarttraffic.device import device 

class DeviceManager(manager.Manager):

    def __init__(self):
        super().__init__()
        self._devices = []

    def init_manager(self):
        self.setup_devices()

    def start_manager(self):
        self.init_devices()        

    def test_devices(self):
        confirm = input('[DEVICE Manager] Do you really want to test all devices? (Y/n) ')

        if confirm == 'Y':
            print(f'[DEVICE Manager] Testing all devices...')

            for target_device in self._devices:
                target_device.test_device()
                sleep(1)

            print(f'[DEVICE Manager] Test ended')
        else:
            print(f'[DEVICE Manager] Test cancelled')

    def link_device(self, target_device: device.Device):
        self._devices.append(target_device)

    def setup_devices(self):
        print(f'[DEVICE Manager] Setup all devices...')
        for target_device in self._devices:
            self.setup_device(target_device)

    def setup_device(self, target_device: device.Device):
        if(target_device.state is device.State.WAITING):
            target_device.setup_device()

    def init_devices(self):
        print(f'[DEVICE Manager] Init all devices...')
        for target_device in self._devices:
            self.init_device(target_device)

    def init_device(self, target_device: device.Device):
        if(target_device.state is device.State.SETUP):
            target_device.init_device()

device_manager = DeviceManager()