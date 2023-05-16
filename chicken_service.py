import time
import datetime
import logging

from astral import Astral

import logger as logger
import door_control as dc


logger.setup_logging('chicken.log')


def in_between(now, start=None, end=None):
    if start is None or end is None:
        city_name = 'San Francisco'
        a = Astral()
        a.solar_depression = 'civil'
        city = a[city_name]
        sun = city.sun(date=now, local=True)
        if start is None:
            start = sun['sunrise']
        if end is None:
            end = sun['sunset'] + datetime.timedelta(hours=1) 

    if start <= end:
        return start <= now.astimezone() < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now.astimezone() or now.astimezone() < end


if __name__ == '__main__':
    logger = logging.getLogger('foobar')
    logger.info("Chicken Door Service Has Begun!")
    ljm = dc.LabMotorDoor()
    ljm.reset()
    
    while(True):
        now = datetime.datetime.now()
        if in_between(now):  # Door should be open
            if ljm.door_state == "closed":
                logger.info("Openning Door")
                ljm.open()
            else:
                logger.info("Door remaining opened.")
        else:  # Door should be closed
            if ljm.door_state == "opened":
                logger.info("Closing Door")
                ljm.close()
            else:
                logger.info("Door remaining closed.")
        time.sleep(60 * 15)

    # This will never be reached
    ljm.dev.close()

