"""Virtual printer services for slicer integration."""

from backend.app.services.virtual_printer.constants import (
    DEFAULT_VIRTUAL_PRINTER_MODEL,
    DEFAULT_VIRTUAL_PRINTER_VERSION,
)
from backend.app.services.virtual_printer.manager import (
    VIRTUAL_PRINTER_MODELS,
    virtual_printer_manager,
)

__all__ = [
    "virtual_printer_manager",
    "VIRTUAL_PRINTER_MODELS",
    "DEFAULT_VIRTUAL_PRINTER_MODEL",
    "DEFAULT_VIRTUAL_PRINTER_VERSION",
]
