#!/usr/bin/python3
"""Rebel Int class"""


class MyInt(int):
    """Rebel Int class"""
    def __eq__(self, other) -> bool:
        """Check if reverse"""
        return int(self) != int(other)

    def __ne__(self, other) -> bool:
        return int(self) == int(other)

