# -*- coding: utf-8 -*-
"""
WOI 3.7 : plasma current
"""
from pppat.libpulse.check_result import CheckResult as Result
from pppat.libpulse.waveform import get_waveform
import numpy as np

import logging
logger = logging.getLogger(__name__)


def check_WOI_3p7_plasma_current(is_online=False, waveforms=None):
    """ Check the expected plasma current values """
    check_name = 'WOI 3.7: plasma current'

    # retrieve the Ip waveform
    waveform_name = 'rts:WEST_PCS/Plasma/Ip/waveform.ref'

    waveform_ip = get_waveform(waveform_name, waveforms)

    if not waveform_ip:
        raise(ValueError(f'waveform {waveform_name} not found!?'))
    else:
        # check the max Ip
        Ip_max = np.amax(waveform_ip.values)
        logger.info(f'Max Ip from waveform: {Ip_max}')

        # TODO : retourner le temps & le segment de l'erreur (si errur)
        if Ip_max > 1e6:
            return Result(name=check_name, code=Result.ERROR,
                          text='Plasma current above maximum limit')
        else:
            return Result(name=check_name, code=Result.OK,
                          text='Plasma current OK')
