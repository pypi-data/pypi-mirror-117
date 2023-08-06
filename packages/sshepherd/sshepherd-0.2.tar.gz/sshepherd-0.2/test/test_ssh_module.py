"""
test_ssh_module.py - Part of SSHepherd

:author: George <drpresq@gmail.com>
:description: SSHepherd SSH Test Module - Consists of pytest unit tests of the sshepherd.ssh Module
:license: GPL3
:donation:
    BTC - 15wRP3NGm2zQwsC36gYAMf8ZaBNuDP6BiR
    LTC - LQANeFg6qhEUCftCGpXTdgCKnPkBMR5Ems
"""

import getpass
import pathlib
import paramiko
import pytest
from typing import Optional
from sshepherd import errors
from sshepherd import ssh

password: str = getpass.getpass(prompt="\n\nPlease enter the ssh key password for these tests: ")


def test_ssh_client_init():
    """sshepherd.ssh.Client.__init__() tests"""
    # Empty Init
    ssh.getpass.getpass = lambda prompt: password
    client = ssh.Client()
    ssh.getpass.getpass = getpass.getpass
    assert client.ssh_user == getpass.getuser()

    # User provided username
    client = ssh.Client(ssh_user=getpass.getuser(), ssh_key_password=password)
    assert client.ssh_user == getpass.getuser()

    # Incorrect SSH Key Password
    with pytest.raises(errors.SSHKeyException) as key_error:
        ssh.getpass.getpass = lambda prompt: 'a'
        client = ssh.Client()
    assert key_error.type == errors.SSHKeyException


def test_ssh_client_actions():
    """sshepherd.ssh.Client.(list_users, add_users, run_commands) tests"""

    # Common Mockups
    class OmniClass:
        def __init__(self, readlines: Optional[list] = None):
            self.readline = readlines if readlines else ["success\n"]

        def readlines(self, *args, **kwargs):
            for line in self.readline:
                yield line

        @staticmethod
        def put(*args, **kwargs):
            return None

    ssh.Client.connect = lambda self, hostname, username, pkey: None
    ssh.Client.exec_command = lambda self, command: ("", OmniClass(), "")
    target_hosts: list = ["192.168.1.1"]

    # List Users
    client = ssh.Client(ssh_key_password=password)
    assert client.get_users_by_system(target_group=target_hosts) == {target_hosts[0]: ["success"]}

    # Add Users
    ssh.SCPClient = lambda transport: OmniClass()
    assert client.add_users(target_group=target_hosts, new_users={"user1": "some/path"}) == {target_hosts[0]: ["success"]}

    # Run Commands
    commands: list = ["whoami"]
    ssh.Client.exec_command = lambda self, command: ("", OmniClass(commands), "")
    assert client.run_command(target_group=target_hosts, command=str(commands)) is None


def test_ssh__locate_ssh_key():
    ssh.Path.exists = lambda path: True
    assert isinstance(ssh._locate_ssh_key("some/path"), pathlib.Path)

    ssh.Path.exists = lambda path: False
    with pytest.raises(errors.SSHKeyException) as key_error:
        ssh._locate_ssh_key("some/path")
    assert key_error.type == errors.SSHKeyException
    assert "SShepherd Error: There was an error processing the ssh keyfile -> some/path" in str(key_error.value)


def test_ssh__unlock_ssh_key():
    with pytest.raises(errors.SSHKeyException) as key_error:
        ssh.getpass.getpass = lambda prompt: 'a'
        ssh._unlock_ssh_key(f'{pathlib.Path.home()}/.ssh/id_rsa')
    assert "Password incorrect" in str(key_error.value)

    with pytest.raises(errors.SSHKeyException) as key_error:
        ssh.getpass.getpass = lambda prompt: ''
        ssh._unlock_ssh_key(f'{pathlib.Path.home()}/.ssh/id_rsa')

    paramiko.RSAKey.from_private_key_file = lambda path: "sshkey"
    assert ssh._unlock_ssh_key("some/path") == "sshkey"






