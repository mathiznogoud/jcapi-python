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


class AuthInfo(object):
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
        'expiry': 'str',
        'is_valid': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'expiry': 'expiry',
        'is_valid': 'isValid',
        'message': 'message'
    }

    def __init__(self, expiry=None, is_valid=None, message=None):  # noqa: E501
        """AuthInfo - a model defined in Swagger"""  # noqa: E501

        self._expiry = None
        self._is_valid = None
        self._message = None
        self.discriminator = None

        if expiry is not None:
            self.expiry = expiry
        if is_valid is not None:
            self.is_valid = is_valid
        if message is not None:
            self.message = message

    @property
    def expiry(self):
        """Gets the expiry of this AuthInfo.  # noqa: E501


        :return: The expiry of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this AuthInfo.


        :param expiry: The expiry of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._expiry = expiry

    @property
    def is_valid(self):
        """Gets the is_valid of this AuthInfo.  # noqa: E501


        :return: The is_valid of this AuthInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this AuthInfo.


        :param is_valid: The is_valid of this AuthInfo.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def message(self):
        """Gets the message of this AuthInfo.  # noqa: E501


        :return: The message of this AuthInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AuthInfo.


        :param message: The message of this AuthInfo.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, AuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
