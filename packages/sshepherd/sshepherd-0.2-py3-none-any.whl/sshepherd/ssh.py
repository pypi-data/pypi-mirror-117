"""
ssh.py - Part of SSHepherd

:author: George <drpresq@gmail.com>
:description: SSHepherd SSH module - Consists of objects that define communication with ssh hosts
:license: GPL3
:donation:
    BTC - 15wRP3NGm2zQwsC36gYAMf8ZaBNuDP6BiR
    LTC - LQANeFg6qhEUCftCGpXTdgCKnPkBMR5Ems
"""

import getpass
import time
import paramiko
from sshepherd import errors
from scp import SCPClient
from typing import Union, Optional
from pathlib import Path


def _locate_ssh_key(ssh_key: Optional[str] = None) -> Path:
    candidate_path: Path = Path(f'{Path.home()}/.ssh/{ssh_key}') if Path(f'{Path.home()}/.ssh/{ssh_key}').exists() \
        else Path(f'{Path.home()}/.ssh/id_rsa')
    if not candidate_path.exists():
        raise errors.SSHKeyException(candidate_path if not ssh_key else ssh_key)
    return candidate_path


def _unlock_ssh_key(ssh_key: Union[str, Path], password: Optional[str] = None) -> paramiko.pkey.PKey:
    try:
        ret = paramiko.RSAKey.from_private_key_file(str(ssh_key))
    except paramiko.PasswordRequiredException:
        try_count: int = 0
        while True:
            try:
                ret = paramiko.RSAKey.from_private_key_file(filename=str(ssh_key),
                                                            password=(
                                                                getpass.getpass(
                                                                    prompt=f"Password incorrect. "
                                                                    f"Please enter ssh key password again: ")
                                                                if try_count != 0 else
                                                                getpass.getpass(
                                                                    prompt=f"Please enter ssh Key password: ")
                                                                if try_count > 0 or not password else
                                                                password
                                                                )
                                                            )
                break
            except (ValueError, paramiko.SSHException) as err:
                if "OpenSSH private key file checkints do not match" not in err.__str__() and not isinstance(err, ValueError):
                    raise errors.UnexpectedError(err.__str())
                elif try_count >= 2:
                    raise errors.SSHKeyException(f'{ssh_key}: Password incorrect')
                try_count += 1
    except paramiko.SSHException as err:
        raise errors.UnexpectedError(err.__str__())
    return ret


class Client(paramiko.client.SSHClient):
    ssh_user: str
    ssh_key: paramiko.PKey
    current_users: dict

    def __init__(self,
                 ssh_user: Optional[str] = None,
                 ssh_key: Optional[Union[str, Path]] = None,
                 ssh_key_password: Optional[str] = None) -> None:

        self.ssh_user = ssh_user if ssh_user else getpass.getuser()

        ssh_key: Path = Path(ssh_key) if ssh_key \
            and Path(ssh_key).exists() \
            else _locate_ssh_key(ssh_key)

        self.ssh_key = _unlock_ssh_key(ssh_key=ssh_key,
                                       password=(ssh_key_password if ssh_key_password else None)
                                       )
        super().__init__()
        self.load_system_host_keys()

    def get_users_by_system(self, target_group: Union[list, str]) -> dict:
        command: str = "$(which ls) /home/"
        current_users: dict = {}
        if not isinstance(target_group, list):
            target_group = [target_group]
        for system in target_group:
            self.connect(hostname=system, username=self.ssh_user, pkey=self.ssh_key)
            # self.exec_command returns tuple: (stdin, stdout, stderr)
            _, stdout, _ = self.exec_command(command=command)
            current_users.update({system: [line.strip("\n") for line in stdout.readlines() if line != "\n"]})
        self.current_users = current_users
        return current_users

    def add_users(self, target_group: Union[list, str], new_users: dict) -> dict:
        new_users = {users: key for users, key in new_users.items() if Path(key).exists()}
        _ = self.get_users_by_system(target_group)
        if not isinstance(target_group, list):
            target_group = [target_group]
        for system in target_group:
            user_delta: list = [user for user in new_users.keys() if user not in self.current_users[system]]
            for user in user_delta:
                self.connect(hostname=system, username=self.ssh_user, pkey=self.ssh_key)
                scp = SCPClient(self.get_transport())
                scp.put(files=new_users[user], remote_path=f'/home/{self.ssh_user}/')
                command: str = f'sudo useradd -s /bin/bash {user};' \
                               f'sudo mkdir /home/{user};' \
                               f'sudo cp -r /etc/skel/. /home/{user};' \
                               f'sudo mkdir /home/{user}/.ssh;' \
                               f'sudo mv {user}_id_rsa.pub /home/{user}/.ssh/authorized_keys;' \
                               f'sudo chown -R {user} /home/{user};' \
                               f'sudo chgrp -R {user} /home/{user};'
                # self.exec_command returns tuple: (stdin, stdout, stderr)
                _, _, _ = self.exec_command(command=command)
                time.sleep(10)
        return self.get_users_by_system(target_group)

    def run_command(self, target_group: Union[list, str], command: str) -> None:
        if not isinstance(target_group, list):
            target_group = [target_group]
        for system in target_group:
            self.connect(hostname=system, username=self.ssh_user, pkey=self.ssh_key)
            # self.exec_command returns tuple: (stdin, stdout, stderr)
            _, stdout, _ = self.exec_command(command=command)
            for line in [line.strip("\n") for line in stdout.readlines() if line != "\n"]:
                print(f'{system} output:\t{line}')
