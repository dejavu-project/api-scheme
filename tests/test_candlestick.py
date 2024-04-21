##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import unittest
from datetime import datetime

# Third-party
from src.utils.messages import (
    get_ohlcv_message,
    get_timestamp_message,
    get_candlestick_message,
    get_signal_message,
)


class TestCandlestick(unittest.TestCase):
    """ Tests for `Candlestick` """


    def test_get_timestamp_message(self):
        """ Test for `get_timestamp_message` """
        _datetime = datetime(
            year = 2024,
            month = 3,
            day = 20,
            hour = 12,
            minute = 20,
            second = 45,
            microsecond = 150
        )
        timestamp = get_timestamp_message(_datetime)
        # Test
        assert timestamp.seconds == 1710937245, 'invalid seconds value'
        assert timestamp.nanos == 150000, 'invalid nanoseconds value'
        # Return value
        return timestamp


    def test_get_ohlcv_message(self):
        """ Test for `get_ohlcv_message` """
        open = 100
        high = 110
        low = 90
        close = 80
        volume = 1000
        ohlcv = get_ohlcv_message(open, high, low, close, volume)
        # Test
        assert ohlcv.open == open, 'invalid `open` field value'
        assert ohlcv.high == high, 'invalid `high` field value'
        assert ohlcv.low == low, 'invalid `low` field value'
        assert ohlcv.close == close, 'invalid `close` field value'
        assert ohlcv.volume == volume, 'invalid `volume` field value'
        # Return value
        return ohlcv


    def test_get_candlestick_message(self):
        """ Test for `get_candlestick_message` """
        timestamp   = self.test_get_timestamp_message()
        ohlcv       = self.test_get_ohlcv_message()
        signal      = self.test_get_signal_message()
        candlestick = get_candlestick_message(
            timestamp = timestamp,
            ohlcv = ohlcv,
            signal = signal
        )
        # Test
        assert candlestick.ohlcv == ohlcv, 'invalid `ohlcv` value'
        assert candlestick.timestamp == timestamp, 'invalid `timestamp` value'


    def test_get_signal_message(self):
        """ Test for `get_signal_message` """
        _datetime = datetime(
            year = 2024,
            month = 3,
            day = 20,
            hour = 12,
            minute = 20,
            second = 45,
            microsecond = 150
        )
        take_profit = 110
        stop_loss = 90
        confidence = 0.9
        signal = get_signal_message(
            timestamp = _datetime,
            position = 'LONG',
            side = 'BUY',
            take_profit = take_profit,
            stop_loss = stop_loss,
            confidence = confidence
        )
        # Test
        assert signal.timestamp.seconds == 1710937245, 'invalid seconds value'
        assert signal.timestamp.nanos == 150000, 'invalid nanoseconds value'
        assert signal.take_profit == take_profit, 'invalid take_profit value'
        assert signal.stop_loss == stop_loss, 'invalid stop_loss value'
        assert signal.confidence == confidence, 'invalid confidence value'


if __name__ == '__main__':
    unittest.main(exit=False)
