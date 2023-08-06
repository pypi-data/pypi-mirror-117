from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

from ctlml_commons.entity.execution_type import ExecutionType
from ctlml_commons.entity.order import OrderType
from ctlml_commons.util.date_utils import convert_dates, datetime_to_str
from ctlml_commons.util.num_utils import convert_floats


@dataclass
class Execution:
    id: str
    b_id: str
    execution_type: ExecutionType
    symbol: str
    shares: float
    purchase_price: float
    sell_price: float
    profit_loss: float
    notes: str
    time: datetime
    order_type: Optional[OrderType] = None
    bid_price: Optional[float] = 0.00
    investment_strategy_data: Optional[str] = None

    def serialize(self) -> Dict[str, Any]:
        data: Dict[str, Any] = deepcopy(self.__dict__)

        data["execution_type"] = self.execution_type.value()
        data["time"] = datetime_to_str(self.time)

        if self.order_type is not None:
            data["order_type"] = self.order_type.value()

        return data

    @classmethod
    def deserialize(cls, input_data: Dict[str, Any]) -> Execution:
        return Execution(**cls.clean(input_data=input_data))

    @classmethod
    def clean(cls, input_data: Dict[str, Any]) -> Dict[str, Any]:
        data = deepcopy(input_data)

        data["execution_type"] = ExecutionType.to_enum(data["execution_type"])
        data = convert_floats(data, ["shares", "purchase_price", "sell_price", "profit_loss"])
        data = convert_dates(data, "time")

        if "order_type" in data and data["order_type"] is not None:
            data["order_type"] = OrderType.to_enum(data["order_type"])

        return data
