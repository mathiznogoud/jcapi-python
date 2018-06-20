# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'description': 'str',
        'display_name': 'str',
        'os_meta_family': 'str',
        'activation': 'str',
        'behavior': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'display_name': 'displayName',
        'os_meta_family': 'osMetaFamily',
        'activation': 'activation',
        'behavior': 'behavior'
    }

    def __init__(self, id=None, name=None, description=None, display_name=None, os_meta_family=None, activation=None, behavior=None):
        """
        PolicyTemplate - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._display_name = None
        self._os_meta_family = None
        self._activation = None
        self._behavior = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if display_name is not None:
          self.display_name = display_name
        if os_meta_family is not None:
          self.os_meta_family = os_meta_family
        if activation is not None:
          self.activation = activation
        if behavior is not None:
          self.behavior = behavior

    @property
    def id(self):
        """
        Gets the id of this PolicyTemplate.
        ObjectId uniquely identifying a Policy Template.

        :return: The id of this PolicyTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PolicyTemplate.
        ObjectId uniquely identifying a Policy Template.

        :param id: The id of this PolicyTemplate.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PolicyTemplate.
        The unique name for the Policy Template.

        :return: The name of this PolicyTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyTemplate.
        The unique name for the Policy Template.

        :param name: The name of this PolicyTemplate.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PolicyTemplate.
        The default description for the Policy.

        :return: The description of this PolicyTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PolicyTemplate.
        The default description for the Policy.

        :param description: The description of this PolicyTemplate.
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this PolicyTemplate.
        The default display name for the Policy.

        :return: The display_name of this PolicyTemplate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PolicyTemplate.
        The default display name for the Policy.

        :param display_name: The display_name of this PolicyTemplate.
        :type: str
        """

        self._display_name = display_name

    @property
    def os_meta_family(self):
        """
        Gets the os_meta_family of this PolicyTemplate.

        :return: The os_meta_family of this PolicyTemplate.
        :rtype: str
        """
        return self._os_meta_family

    @os_meta_family.setter
    def os_meta_family(self, os_meta_family):
        """
        Sets the os_meta_family of this PolicyTemplate.

        :param os_meta_family: The os_meta_family of this PolicyTemplate.
        :type: str
        """
        allowed_values = ["linux", "darwin", "windows"]
        if os_meta_family not in allowed_values:
            raise ValueError(
                "Invalid value for `os_meta_family` ({0}), must be one of {1}"
                .format(os_meta_family, allowed_values)
            )

        self._os_meta_family = os_meta_family

    @property
    def activation(self):
        """
        Gets the activation of this PolicyTemplate.
        Requirements before the policy can be activated.

        :return: The activation of this PolicyTemplate.
        :rtype: str
        """
        return self._activation

    @activation.setter
    def activation(self, activation):
        """
        Sets the activation of this PolicyTemplate.
        Requirements before the policy can be activated.

        :param activation: The activation of this PolicyTemplate.
        :type: str
        """

        self._activation = activation

    @property
    def behavior(self):
        """
        Gets the behavior of this PolicyTemplate.
        Specifics about the behavior of the policy.

        :return: The behavior of this PolicyTemplate.
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """
        Sets the behavior of this PolicyTemplate.
        Specifics about the behavior of the policy.

        :param behavior: The behavior of this PolicyTemplate.
        :type: str
        """

        self._behavior = behavior

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PolicyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
