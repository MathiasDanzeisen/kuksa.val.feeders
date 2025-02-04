#!/usr/bin/env python3

#################################################################################
# Copyright (c) 2023 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License 2.0 which is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
#################################################################################

import logging
from typing import Any

from abc import ABC, abstractmethod

log = logging.getLogger(__name__)


class ClientWrapper(ABC):
    """
    Wraps client-specific functionality so that that main dbcfeeder does not need to care about it.
    This acts as a base class, each client (type and/or technology) shall be in a separate file
    This file shall be feeder/provider independent, and can possibly be moved to kuksa.val/kuksa-client
    """
    def __init__(self, ip: str, port: int, token_path: str, tls: bool = True):
        """
        This init method is only supposed to be called by subclassed __init__ functions
        """
        self._ip = ip
        self._port = port
        self._token_path = token_path
        self._tls = tls
        self._registered = False

    def set_ip(self, ip: str):
        """ Set IP address to use """
        self._ip = ip

    def set_port(self, port: int):
        """ Set port to use """
        self._port = port

    def set_tls(self, tls: bool):
        """
        Set if TLS shall be used (including server auth).
        Currently we rely on default location for root cert as defined by kuksa-client
        """
        self._tls = tls

    def set_token_path(self, token_path: str):
        self._token_path = token_path

    # Abstract methods to implement
    @abstractmethod
    def get_client_specific_configs(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def is_signal_defined(self, vss_name: str) -> bool:
        pass

    @abstractmethod
    def update_datapoint(self, name: str, value: Any) -> bool:
        pass

    @abstractmethod
    def stop(self):
        pass
