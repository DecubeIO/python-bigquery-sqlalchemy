from sqlalchemy.sql.schema import Column, SchemaItem
from sqlalchemy.sql.functions import Function


class Partition(SchemaItem):
    __visit_name__ = "partition" 
    
    def __init__(
        self, expr: str | Column | Function, 
        partition_expiration_days: int | None = None, 
        require_partition_filter: bool = False, 
    ):
        self.expr = expr
        self.partition_expiration_days = partition_expiration_days
        self.require_partition_filter = require_partition_filter

    def __repr__(self) -> str:
        return f"Partition({self.expr})"

    def __str__(self) -> str:
        if isinstance(self.expr, str):
            return self.expr
        elif isinstance(self.expr, Function):
            return str(self.expr)
        else:
            return self.expr.name