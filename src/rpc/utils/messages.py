##########################################################
#
# Copyright (C) 2023-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

from datetime import datetime
from google.protobuf import timestamp_pb2
from protos import candlestick_struct_pb2


def get_timestamp_message(
    timestamp: datetime,
) -> timestamp_pb2.Timestamp:
    """
        Returns a `google.protobuf.Timestamp` message from Python datetime object.

        Parameters:
            - timestamp (datetime): Datetime object representing the timestamp.

        Returns:
            - (timestamp_pb2.Timestamp): Timestamp message.
    """
    timestamp_message = timestamp_pb2.Timestamp()
    timestamp_message.FromDatetime(timestamp)
    return timestamp_message


def get_candlestick_message(
    timestamp: timestamp_pb2.Timestamp,
    ohlcv: candlestick_struct_pb2.Ohlcv,
    signal: candlestick_struct_pb2.Signal
) -> candlestick_struct_pb2.Candlestick:
    """
        Returns a Candlestick message.

        Parameters:
            - timestamp (timestamp_pb2.Timestamp): Timestamp of the candlestick.
            - ohlcv (candlestick_struct_pb2.Ohlcv): OHLCV message.
            - signal (candlestick_struct_pb2.Signal): Signal message.

        Returns:
            - (candlestick_struct_pb2.Candlestick): Candlestick message.
    """
    return candlestick_struct_pb2.Candlestick(
        timestamp = timestamp,
        ohlcv = ohlcv,
        signal = signal,
    )


def get_ohlcv_message(
    open: float,
    high: float,
    low: float,
    close: float,
    volume: float,
) -> candlestick_struct_pb2.Ohlcv:
    """
        Returns a Ohlcv message.
    
        Parameters:
            - open (float): Opening price
            - high (float): Highest price.
            - low (float): Lowest price.
            - close (float): Closing price.
            - volume (float): Candlestick volume.

        Returns:
            - (candlestick_struct_pb2.Ohlcv): OHLCV message
    """
    return candlestick_struct_pb2.Ohlcv(
        open = open,
        high = high,
        low =  low,
        close = close,
        volume = volume,
    )


def get_signal_message(
    timestamp: datetime,
    position: str,
    side: str,
    take_profit: float,
    stop_loss: float,
    confidence: float
) -> candlestick_struct_pb2.Signal:
    """
        Returns a Signal message.

        Parameters:
            - timestamp (datetime): Timestamp of the signal.
            - position (str): Position of the signal.
            - side (str): Side of the signal.
            - take_profit (float): Take profit value.
            - stop_loss (float): Stop loss value.
            - confidence (float): Confidence level of the signal.

        Returns:
            - (candlestick_struct_pb2.Signal): Signal message.
    """
    timestamp = get_timestamp_message(timestamp)    # Python datetime to `google.protobuf.Timestamp`
    return candlestick_struct_pb2.Signal(
        timestamp = timestamp,
        position = position,
        side = side,
        take_profit = take_profit,
        stop_loss = stop_loss,
        confidence = confidence,
    )
