# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv2.models.auth_input import AuthInput  # noqa: F401,E501


class WorkdayInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'report_url': 'str',
        'name': 'str',
        'auth': 'AuthInput'
    }

    attribute_map = {
        'report_url': 'reportUrl',
        'name': 'name',
        'auth': 'auth'
    }

    def __init__(self, report_url=None, name=None, auth=None):  # noqa: E501
        """WorkdayInput - a model defined in Swagger"""  # noqa: E501

        self._report_url = None
        self._name = None
        self._auth = None
        self.discriminator = None

        if report_url is not None:
            self.report_url = report_url
        if name is not None:
            self.name = name
        if auth is not None:
            self.auth = auth

    @property
    def report_url(self):
        """Gets the report_url of this WorkdayInput.  # noqa: E501


        :return: The report_url of this WorkdayInput.  # noqa: E501
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this WorkdayInput.


        :param report_url: The report_url of this WorkdayInput.  # noqa: E501
        :type: str
        """

        self._report_url = report_url

    @property
    def name(self):
        """Gets the name of this WorkdayInput.  # noqa: E501


        :return: The name of this WorkdayInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkdayInput.


        :param name: The name of this WorkdayInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def auth(self):
        """Gets the auth of this WorkdayInput.  # noqa: E501


        :return: The auth of this WorkdayInput.  # noqa: E501
        :rtype: AuthInput
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this WorkdayInput.


        :param auth: The auth of this WorkdayInput.  # noqa: E501
        :type: AuthInput
        """

        self._auth = auth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkdayInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
