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

from jcapiv2.models.group_type import GroupType  # noqa: F401,E501


class Group(object):
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
        'id': 'str',
        'type': 'GroupType',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, id=None, type=None, name=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        ObjectId uniquely identifying a Group.  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        ObjectId uniquely identifying a Group.  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Group.  # noqa: E501


        :return: The type of this Group.  # noqa: E501
        :rtype: GroupType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Group.


        :param type: The type of this Group.  # noqa: E501
        :type: GroupType
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        Display name of a Group.  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        Display name of a Group.  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
