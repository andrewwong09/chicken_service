import time
import datetime
import logging

import logger as logger
import door_control as dc


logger.setup_logging('chicken.log')


def in_between(now, start=datetime.time(6, 30), end=datetime.time(20, 30)):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end


if __name__ == '__main__':
    logger = logging.getLogger('foobar')
    logger.info("Chicken Door Service Has Begun!")
    ljm = dc.LabMotorDoor()
    ljm.reset()
    
    while(True):
        if in_between(now.time()):
            if ljm.door_state == "closed":
                logger.info("Openning Door")
                ljm.open()
        else:
            if ljm.door_state == "openned":
                logger.info("Closing Door")
                ljm.close()
        time.sleep(60 * 15)

    # This will never be reached
    ljm.dev.close()

