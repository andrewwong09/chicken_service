import time
import logging

import u6 as u6

import logger as logger


logger.setup_logging('chicken.log')


class LabMotorDoor():
    def __init__(self):
        self.logger = logging.getLogger('foobar.ljm')
        self.logger.info('LJM Created')
        self.dev = u6.U6()
        self.PUL_pin = 0
        self.DIR_pin = 1
        self.fwd_state = 0
        self.sleep_step = 0
        self.steps_to_pull = None
        ret = self.dev.configU6()
        self.logger.info(ret)


    def step(self, num_steps, dir_state):
        self.dev.setDOState(ioNum=self.DIR_pin,
                            state=dir_state)
        self.logger.info(f'Stepping: {dir_state} {num_steps}')
        for _ in range(num_steps):
            self.dev.setDOState(ioNum=self.PUL_pin,
                                state=0)
            time.sleep(self.sleep_step)
            self.dev.setDOState(ioNum=self.PUL_pin,
                                state=1)
            time.sleep(self.sleep_step)
        self.logger.info('Done Stepping')

if __name__ == '__main__':
    ljm = LabMotorDoor()
    ljm.step(100, 0)
    ljm.step(100, 1)

