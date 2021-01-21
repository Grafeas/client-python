# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from grafeas.models.api_build_signature import ApiBuildSignature  # noqa: F401,E501


class ApiBuildType(object):
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
        'builder_version': 'str',
        'signature': 'ApiBuildSignature'
    }

    attribute_map = {
        'builder_version': 'builder_version',
        'signature': 'signature'
    }

    def __init__(self, builder_version=None, signature=None):  # noqa: E501
        """ApiBuildType - a model defined in Swagger"""  # noqa: E501

        self._builder_version = None
        self._signature = None
        self.discriminator = None

        if builder_version is not None:
            self.builder_version = builder_version
        if signature is not None:
            self.signature = signature

    @property
    def builder_version(self):
        """Gets the builder_version of this ApiBuildType.  # noqa: E501

        Version of the builder which produced this Note.  # noqa: E501

        :return: The builder_version of this ApiBuildType.  # noqa: E501
        :rtype: str
        """
        return self._builder_version

    @builder_version.setter
    def builder_version(self, builder_version):
        """Sets the builder_version of this ApiBuildType.

        Version of the builder which produced this Note.  # noqa: E501

        :param builder_version: The builder_version of this ApiBuildType.  # noqa: E501
        :type: str
        """

        self._builder_version = builder_version

    @property
    def signature(self):
        """Gets the signature of this ApiBuildType.  # noqa: E501

        Signature of the build in Occurrences pointing to the Note containing this `BuilderDetails`.  # noqa: E501

        :return: The signature of this ApiBuildType.  # noqa: E501
        :rtype: ApiBuildSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ApiBuildType.

        Signature of the build in Occurrences pointing to the Note containing this `BuilderDetails`.  # noqa: E501

        :param signature: The signature of this ApiBuildType.  # noqa: E501
        :type: ApiBuildSignature
        """

        self._signature = signature

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
        if not isinstance(other, ApiBuildType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
