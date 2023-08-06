# -*- coding: utf-8 -*-
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""HWInfo test."""

import unittest
from unittest.mock import MagicMock, patch

from lpot.ux.utils.hw_info import HWInfo


class TestHWInfo(unittest.TestCase):
    """HWInfo tests."""

    def __init__(self, *args: str, **kwargs: str) -> None:
        """Hardware Info tests constructor."""
        super().__init__(*args, **kwargs)

    def test_HWInfo_type(self) -> None:
        """Test if hardware info collects."""
        hw_info_expected_types = {
            "bios_version": str,
            "cores": int,
            "cores_per_socket": int,
            "hyperthreading_enabled": bool,
            "ip": str,
            "kernel": str,
            "max_cpu_freq": str,
            "min_cpu_freq": str,
            "platform": str,
            "sockets": int,
            "system": str,
            "threads_per_socket": int,
            "total_memory": str,
            "turboboost_enabled": (bool, str),
        }
        hw_info = HWInfo()
        hw_info_dict = vars(hw_info)
        self.assertSetEqual(set(hw_info_dict.keys()), set(hw_info_expected_types.keys()))
        for key, value in hw_info_dict.items():
            if key in hw_info_expected_types:
                expected_type = hw_info_expected_types[key]
                if isinstance(expected_type, (type, tuple)):
                    if isinstance(value, expected_type):
                        continue
            raise Exception(
                f"Wrong type for key: {key} value: {value}. "
                f"Recived {type(value)}, expected {hw_info_expected_types.get(key)}.",
            )

    @patch("psutil.cpu_count")
    def test_cores_num(self, mock_cpu_count: MagicMock) -> None:
        """Test if hw info uses psutil cpu_count to get number of cores."""
        mock_cpu_count.return_value = 8

        hw_info = HWInfo()
        self.assertEqual(hw_info.cores, 8)

    @patch("subprocess.Popen")
    def test_sockets_num(self, mock_subprocess: MagicMock) -> None:
        """Test getting number of sockets."""
        mock_subprocess.return_value.stdout = [b"           4\n"]

        hw_info = HWInfo()
        self.assertEqual(hw_info.sockets, 4)

    @patch("lpot.ux.utils.hw_info.get_number_of_sockets")
    @patch("platform.release")
    @patch("platform.system")
    @patch("psutil.LINUX", False)
    @patch("psutil.WINDOWS", True)
    def test_get_windows_distribution(
        self,
        mock_platform_system: MagicMock,
        mock_platform_release: MagicMock,
        mock_get_number_of_sockets: MagicMock,
    ) -> None:
        """Test getting windows system distribution."""
        mock_platform_system.return_value = "Windows"
        mock_platform_release.return_value = "10"
        mock_get_number_of_sockets.return_value = 2

        hw_info = HWInfo()
        self.assertEqual(hw_info.system, "Windows 10")

    @patch("platform.dist", create=True)
    @patch("psutil.LINUX", True)
    @patch("psutil.WINDOWS", False)
    def test_get_linux_distribution(
        self,
        mock_platform_dist: MagicMock,
    ) -> None:
        """Test getting linux system distribution."""
        mock_platform_dist.return_value = (
            "DistroName",
            "DistroVerID",
            "DistroVerCodename",
        )

        hw_info = HWInfo()
        self.assertEqual(hw_info.system, "DistroName DistroVerID DistroVerCodename")

    @patch("platform.release")
    @patch("platform.system")
    @patch("platform.dist", create=True)
    @patch("psutil.LINUX", True)
    @patch("psutil.WINDOWS", False)
    def test_get_linux_distribution_without_dist(
        self,
        mock_platform_dist: MagicMock,
        mock_platform_system: MagicMock,
        mock_platform_release: MagicMock,
    ) -> None:
        """Test getting linux system distribution."""
        mock_platform_dist.configure_mock(side_effect=AttributeError)
        mock_platform_system.return_value = "Linux"
        mock_platform_release.return_value = "kernel_ver-88-generic"

        hw_info = HWInfo()
        self.assertEqual(hw_info.system, "Linux kernel_ver-88-generic")

    @patch("lpot.ux.utils.hw_info.get_number_of_sockets")
    @patch("platform.platform")
    @patch("psutil.LINUX", False)
    @patch("psutil.WINDOWS", False)
    def test_get_unknown_os_distribution(
        self,
        mock_platform_platform: MagicMock,
        mock_get_number_of_sockets: MagicMock,
    ) -> None:
        """Test getting unknown system distribution."""
        mock_platform_platform.return_value = "SystemName-Version-Arch"
        mock_get_number_of_sockets.return_value = 2

        hw_info = HWInfo()
        self.assertEqual(hw_info.system, "SystemName-Version-Arch")


if __name__ == "__main__":
    unittest.main()
