"""
Qryma Python SDK

A Python SDK for the Qryma Search API.
"""

from .client import QrymaClient
from .version import __version__

__all__ = [
    "QrymaClient",
    "__version__",
]
