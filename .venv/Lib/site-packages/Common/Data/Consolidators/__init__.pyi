from typing import overload
from enum import Enum
import Common.Data.Consolidators
import QuantConnect.Data.Consolidators


class DollarVolumeRenkoConsolidator(QuantConnect.Data.Consolidators.VolumeRenkoConsolidator):
    """
    This consolidator transforms a stream of BaseData instances into a stream of RenkoBar
    with a constant dollar volume for each bar.
    """

    def __init__(self, bar_size: float) -> None:
        """
        Initializes a new instance of the DollarVolumeRenkoConsolidator class using the specified .
        
        :param bar_size: The constant dollar volume size of each bar
        """
        ...

    def adjust_volume(self, volume: float, price: float) -> float:
        """
        Converts raw volume into dollar volume by multiplying it with the trade price.
        
        This method is protected.
        
        :param volume: The raw trade volume
        :param price: The trade price
        :returns: The dollar volume.
        """
        ...


