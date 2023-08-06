"""
errors.py - Part of SSHepherd

:author: George <drpresq@gmail.com>
:description: SSHepherd Error module - Consists of objects that define the SSHepherdError class
:license: GPL3
:donation:
    BTC - 15wRP3NGm2zQwsC36gYAMf8ZaBNuDP6BiR
    LTC - LQANeFg6qhEUCftCGpXTdgCKnPkBMR5Ems
"""
from typing import Union, Optional
from pathlib import Path


class SSHepherdError(Exception):
    message = "SShepherd Error:"

    def __init__(self, message: str):
        self.message = f'{self.message} {message}'
        super().__init__(self.message)


class UnexpectedError(SSHepherdError):
    def __init__(self, error_target: Optional[str] = None,  message: str = "An unexpected error was encountered"):
        self.error_target = f'-> with {error_target}.' if error_target else f'.'
        super().__init__(message)

    def __str__(self):
        return f'{self.message} {self.error_target}'


class SSHKeyException(SSHepherdError):
    def __init__(self, keyfile_path: Union[str, Path], message: str = "There was an error processing the ssh keyfile"):
        self.keyfile_path = keyfile_path
        super().__init__(message)

    def __str__(self):
        return f'{self.message} -> {self.keyfile_path}'
