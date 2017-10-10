# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Detail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cpe_uri=None, package=None, min_affected_version=None, max_affected_version=None, severity_name=None, description=None, fixed_location=None):
        """
        Detail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cpe_uri': 'str',
            'package': 'str',
            'min_affected_version': 'Version',
            'max_affected_version': 'Version',
            'severity_name': 'str',
            'description': 'str',
            'fixed_location': 'VulnerabilityLocation'
        }

        self.attribute_map = {
            'cpe_uri': 'cpeUri',
            'package': 'package',
            'min_affected_version': 'minAffectedVersion',
            'max_affected_version': 'maxAffectedVersion',
            'severity_name': 'severityName',
            'description': 'description',
            'fixed_location': 'fixedLocation'
        }

        self._cpe_uri = cpe_uri
        self._package = package
        self._min_affected_version = min_affected_version
        self._max_affected_version = max_affected_version
        self._severity_name = severity_name
        self._description = description
        self._fixed_location = fixed_location

    @property
    def cpe_uri(self):
        """
        Gets the cpe_uri of this Detail.
        The cpe_uri in [cpe format] (https://cpe.mitre.org/specification/) in which the vulnerability manifests.  Examples include distro or storage location for vulnerable jar. This field can be used as a filter in list requests.

        :return: The cpe_uri of this Detail.
        :rtype: str
        """
        return self._cpe_uri

    @cpe_uri.setter
    def cpe_uri(self, cpe_uri):
        """
        Sets the cpe_uri of this Detail.
        The cpe_uri in [cpe format] (https://cpe.mitre.org/specification/) in which the vulnerability manifests.  Examples include distro or storage location for vulnerable jar. This field can be used as a filter in list requests.

        :param cpe_uri: The cpe_uri of this Detail.
        :type: str
        """

        self._cpe_uri = cpe_uri

    @property
    def package(self):
        """
        Gets the package of this Detail.
        The name of the package where the vulnerability was found. This field can be used as a filter in list requests.

        :return: The package of this Detail.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """
        Sets the package of this Detail.
        The name of the package where the vulnerability was found. This field can be used as a filter in list requests.

        :param package: The package of this Detail.
        :type: str
        """

        self._package = package

    @property
    def min_affected_version(self):
        """
        Gets the min_affected_version of this Detail.
        The min version of the package in which the vulnerability exists.

        :return: The min_affected_version of this Detail.
        :rtype: Version
        """
        return self._min_affected_version

    @min_affected_version.setter
    def min_affected_version(self, min_affected_version):
        """
        Sets the min_affected_version of this Detail.
        The min version of the package in which the vulnerability exists.

        :param min_affected_version: The min_affected_version of this Detail.
        :type: Version
        """

        self._min_affected_version = min_affected_version

    @property
    def max_affected_version(self):
        """
        Gets the max_affected_version of this Detail.
        The max version of the package in which the vulnerability exists. This field can be used as a filter in list requests.

        :return: The max_affected_version of this Detail.
        :rtype: Version
        """
        return self._max_affected_version

    @max_affected_version.setter
    def max_affected_version(self, max_affected_version):
        """
        Sets the max_affected_version of this Detail.
        The max version of the package in which the vulnerability exists. This field can be used as a filter in list requests.

        :param max_affected_version: The max_affected_version of this Detail.
        :type: Version
        """

        self._max_affected_version = max_affected_version

    @property
    def severity_name(self):
        """
        Gets the severity_name of this Detail.
        The severity (eg: distro assigned severity) for this vulnerability.

        :return: The severity_name of this Detail.
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        """
        Sets the severity_name of this Detail.
        The severity (eg: distro assigned severity) for this vulnerability.

        :param severity_name: The severity_name of this Detail.
        :type: str
        """

        self._severity_name = severity_name

    @property
    def description(self):
        """
        Gets the description of this Detail.
        A vendor-specific description of this note.

        :return: The description of this Detail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Detail.
        A vendor-specific description of this note.

        :param description: The description of this Detail.
        :type: str
        """

        self._description = description

    @property
    def fixed_location(self):
        """
        Gets the fixed_location of this Detail.
        The fix for this specific package version.

        :return: The fixed_location of this Detail.
        :rtype: VulnerabilityLocation
        """
        return self._fixed_location

    @fixed_location.setter
    def fixed_location(self, fixed_location):
        """
        Sets the fixed_location of this Detail.
        The fix for this specific package version.

        :param fixed_location: The fixed_location of this Detail.
        :type: VulnerabilityLocation
        """

        self._fixed_location = fixed_location

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other