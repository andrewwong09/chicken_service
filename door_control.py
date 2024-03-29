import os
import time
import logging

import u6 as u6

import logger as logger


logger.setup_logging('chicken.log')


class LabMotorDoor():
    def __init__(self):
        self.logger = logging.getLogger('foobar.ljm')
        self.logger.info('LJM Door Initiating...')
        try:
            self.dev = u6.U6()
            ret = self.dev.configU6()
        except Exception as err:
            self.logger.error(f'Could not open LJM device, rebooting in 10 minutes: {err}')
            time.sleep(600)
            os.system('sudo shutdown -r now')
        self.logger.info(f'We are initiated: {ret}')
        self.DIR_pin = 0
        self.PUL_pin = 1
        self.ENA_pin = 2
        self.sleep_step = 0.01
        self.door_state = None

    def step(self, num_steps, dir_state):
        self.dev.setDOState(ioNum=self.ENA_pin,
                            state=0)
        self.dev.setDOState(ioNum=self.DIR_pin,
                            state=dir_state)
        self.logger.info(f'Stepping: {dir_state} {num_steps}')
        for step_index in range(num_steps):
            self.dev.setDOState(ioNum=self.PUL_pin,
                                state=0)
            time.sleep(self.sleep_step)
            self.dev.setDOState(ioNum=self.PUL_pin,
                                state=1)
            time.sleep(self.sleep_step)
        if dir_state == 1:
            self.dev.setDOState(ioNum=self.ENA_pin,
                                state=0)
        else:
            self.dev.setDOState(ioNum=self.ENA_pin,
                                state=1)
        self.logger.info('Done Stepping')

    def open(self, rotations=6):
        self.step(rotations * 200, 1)
        self.door_state = "opened"

    def close(self, rotations=6):
        self.step(rotations * 200, 0)
        self.door_state = "closed"

    def reset(self, wait_s=60):
        # Disable enable pin so door closes by weight if it's open already
        self.logger.info(f'Resetting {wait_s} seconds.')
        self.dev.setDOState(ioNum=self.ENA_pin, state=1)
        time.sleep(wait_s)
        self.door_state = "closed"
        self.logger.info('Done resetting.')


if __name__ == '__main__':
    ljm = LabMotorDoor()
    ljm.reset()
    ljm.open()
    time.sleep(10)
    ljm.close()
    ljm.dev.close()
