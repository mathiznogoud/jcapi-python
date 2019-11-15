# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.system_insights_api import SystemInsightsApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestSystemInsightsApi(unittest.TestCase):
    """SystemInsightsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.system_insights_api.SystemInsightsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_systeminsights_list_apps(self):
        """Test case for systeminsights_list_apps

        List System Insights Apps  # noqa: E501
        """
        pass

    def test_systeminsights_list_battery(self):
        """Test case for systeminsights_list_battery

        List System Insights Battery  # noqa: E501
        """
        pass

    def test_systeminsights_list_bitlocker_info(self):
        """Test case for systeminsights_list_bitlocker_info

        List System Insights Bitlocker Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_browser_plugins(self):
        """Test case for systeminsights_list_browser_plugins

        List System Insights Browser Plugins  # noqa: E501
        """
        pass

    def test_systeminsights_list_chrome_extensions(self):
        """Test case for systeminsights_list_chrome_extensions

        List System Insights Chrome Extensions  # noqa: E501
        """
        pass

    def test_systeminsights_list_crashes(self):
        """Test case for systeminsights_list_crashes

        List System Insights Crashes  # noqa: E501
        """
        pass

    def test_systeminsights_list_disk_encryption(self):
        """Test case for systeminsights_list_disk_encryption

        List System Insights Disk Encryption  # noqa: E501
        """
        pass

    def test_systeminsights_list_disk_info(self):
        """Test case for systeminsights_list_disk_info

        List System Insights Disk Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_etc_hosts(self):
        """Test case for systeminsights_list_etc_hosts

        List System Insights Etc Hosts  # noqa: E501
        """
        pass

    def test_systeminsights_list_firefox_addons(self):
        """Test case for systeminsights_list_firefox_addons

        List System Insights Firefox Addons  # noqa: E501
        """
        pass

    def test_systeminsights_list_groups(self):
        """Test case for systeminsights_list_groups

        List System Insights Groups  # noqa: E501
        """
        pass

    def test_systeminsights_list_ie_extensions(self):
        """Test case for systeminsights_list_ie_extensions

        List System Insights IE Extensions  # noqa: E501
        """
        pass

    def test_systeminsights_list_interface_addresses(self):
        """Test case for systeminsights_list_interface_addresses

        List System Insights Interface Addresses  # noqa: E501
        """
        pass

    def test_systeminsights_list_kernel_info(self):
        """Test case for systeminsights_list_kernel_info

        List System Insights Kernel Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_launchd(self):
        """Test case for systeminsights_list_launchd

        List System Insights Launchd  # noqa: E501
        """
        pass

    def test_systeminsights_list_logged_in_users(self):
        """Test case for systeminsights_list_logged_in_users

        List System Insights Logged-In Users  # noqa: E501
        """
        pass

    def test_systeminsights_list_logical_drives(self):
        """Test case for systeminsights_list_logical_drives

        List System Insights Logical Drives  # noqa: E501
        """
        pass

    def test_systeminsights_list_mounts(self):
        """Test case for systeminsights_list_mounts

        List System Insights Mounts  # noqa: E501
        """
        pass

    def test_systeminsights_list_os_version(self):
        """Test case for systeminsights_list_os_version

        List System Insights OS Version  # noqa: E501
        """
        pass

    def test_systeminsights_list_patches(self):
        """Test case for systeminsights_list_patches

        List System Insights Patches  # noqa: E501
        """
        pass

    def test_systeminsights_list_programs(self):
        """Test case for systeminsights_list_programs

        List System Insights Programs  # noqa: E501
        """
        pass

    def test_systeminsights_list_safari_extensions(self):
        """Test case for systeminsights_list_safari_extensions

        List System Insights Safari Extensions  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_apps(self):
        """Test case for systeminsights_list_system_apps

        List System Insights System Apps  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_bitlocker_info(self):
        """Test case for systeminsights_list_system_bitlocker_info

        List System Insights System Bitlocker Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_browser_plugins(self):
        """Test case for systeminsights_list_system_browser_plugins

        List System Insights System Browser Plugins  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_chrome_extensions(self):
        """Test case for systeminsights_list_system_chrome_extensions

        List System Insights System Chrome Extensions  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_controls(self):
        """Test case for systeminsights_list_system_controls

        List System Insights System Control  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_disk_encryption(self):
        """Test case for systeminsights_list_system_disk_encryption

        List System Insights System Disk Encryption  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_disk_info(self):
        """Test case for systeminsights_list_system_disk_info

        List System Insights System Disk Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_etc_hosts(self):
        """Test case for systeminsights_list_system_etc_hosts

        List System Insights System Etc Hosts  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_firefox_addons(self):
        """Test case for systeminsights_list_system_firefox_addons

        List System Insights System Firefox Addons  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_groups(self):
        """Test case for systeminsights_list_system_groups

        List System Insights System Groups  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_info(self):
        """Test case for systeminsights_list_system_info

        List System Insights System Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_interface_addresses(self):
        """Test case for systeminsights_list_system_interface_addresses

        List System Insights System Interface Addresses  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_kernel_info(self):
        """Test case for systeminsights_list_system_kernel_info

        List System Insights System Kernel Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_logical_drives(self):
        """Test case for systeminsights_list_system_logical_drives

        List System Insights System Logical Drives  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_mounts(self):
        """Test case for systeminsights_list_system_mounts

        List System Insights System Mounts  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_os_version(self):
        """Test case for systeminsights_list_system_os_version

        List System Insights System OS Version  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_patches(self):
        """Test case for systeminsights_list_system_patches

        List System Insights System Patches  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_programs(self):
        """Test case for systeminsights_list_system_programs

        List System Insights System Programs  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_safari_extensions(self):
        """Test case for systeminsights_list_system_safari_extensions

        List System Insights System Safari Extensions  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_system_controls(self):
        """Test case for systeminsights_list_system_system_controls

        List System Insights System System Controls  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_system_info(self):
        """Test case for systeminsights_list_system_system_info

        List System Insights System System Info  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_uptime(self):
        """Test case for systeminsights_list_system_uptime

        List System Insights System Uptime  # noqa: E501
        """
        pass

    def test_systeminsights_list_system_users(self):
        """Test case for systeminsights_list_system_users

        List System Insights System Users  # noqa: E501
        """
        pass

    def test_systeminsights_list_uptime(self):
        """Test case for systeminsights_list_uptime

        List System Insights Uptime  # noqa: E501
        """
        pass

    def test_systeminsights_list_usb_devices(self):
        """Test case for systeminsights_list_usb_devices

        List System Insights USB Devices  # noqa: E501
        """
        pass

    def test_systeminsights_list_user_groups(self):
        """Test case for systeminsights_list_user_groups

        List System Insights User Groups  # noqa: E501
        """
        pass

    def test_systeminsights_list_users(self):
        """Test case for systeminsights_list_users

        List System Insights Users  # noqa: E501
        """
        pass

    def test_systeminsights_list_windows_crashes(self):
        """Test case for systeminsights_list_windows_crashes

        List System Insights Windows Crashes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
