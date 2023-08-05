# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HostValidationId(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CONNECTED = "connected"
    HAS_INVENTORY = "has-inventory"
    HAS_MIN_CPU_CORES = "has-min-cpu-cores"
    HAS_MIN_VALID_DISKS = "has-min-valid-disks"
    HAS_MIN_MEMORY = "has-min-memory"
    MACHINE_CIDR_DEFINED = "machine-cidr-defined"
    HAS_CPU_CORES_FOR_ROLE = "has-cpu-cores-for-role"
    HAS_MEMORY_FOR_ROLE = "has-memory-for-role"
    HOSTNAME_UNIQUE = "hostname-unique"
    HOSTNAME_VALID = "hostname-valid"
    BELONGS_TO_MACHINE_CIDR = "belongs-to-machine-cidr"
    API_VIP_CONNECTED = "api-vip-connected"
    BELONGS_TO_MAJORITY_GROUP = "belongs-to-majority-group"
    VALID_PLATFORM = "valid-platform"
    NTP_SYNCED = "ntp-synced"
    CONTAINER_IMAGES_AVAILABLE = "container-images-available"
    LSO_REQUIREMENTS_SATISFIED = "lso-requirements-satisfied"
    OCS_REQUIREMENTS_SATISFIED = "ocs-requirements-satisfied"
    SUFFICIENT_INSTALLATION_DISK_SPEED = "sufficient-installation-disk-speed"
    CNV_REQUIREMENTS_SATISFIED = "cnv-requirements-satisfied"
    SUFFICIENT_NETWORK_LATENCY_REQUIREMENT_FOR_ROLE = "sufficient-network-latency-requirement-for-role"
    SUFFICIENT_PACKET_LOSS_REQUIREMENT_FOR_ROLE = "sufficient-packet-loss-requirement-for-role"
    HAS_DEFAULT_ROUTE = "has-default-route"
    API_DOMAIN_NAME_RESOLVED_CORRECTLY = "api-domain-name-resolved-correctly"
    API_INT_DOMAIN_NAME_RESOLVED_CORRECTLY = "api-int-domain-name-resolved-correctly"
    APPS_DOMAIN_NAME_RESOLVED_CORRECTLY = "apps-domain-name-resolved-correctly"
    COMPATIBLE_WITH_CLUSTER_PLATFORM = "compatible-with-cluster-platform"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """HostValidationId - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(HostValidationId, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HostValidationId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
