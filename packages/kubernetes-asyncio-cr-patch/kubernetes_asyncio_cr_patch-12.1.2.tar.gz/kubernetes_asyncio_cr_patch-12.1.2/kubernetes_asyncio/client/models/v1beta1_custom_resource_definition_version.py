# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1beta1CustomResourceDefinitionVersion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'additional_printer_columns': 'list[V1beta1CustomResourceColumnDefinition]',
        'name': 'str',
        'schema': 'V1beta1CustomResourceValidation',
        'served': 'bool',
        'storage': 'bool',
        'subresources': 'V1beta1CustomResourceSubresources'
    }

    attribute_map = {
        'additional_printer_columns': 'additionalPrinterColumns',
        'name': 'name',
        'schema': 'schema',
        'served': 'served',
        'storage': 'storage',
        'subresources': 'subresources'
    }

    def __init__(self, additional_printer_columns=None, name=None, schema=None, served=None, storage=None, subresources=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1CustomResourceDefinitionVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_printer_columns = None
        self._name = None
        self._schema = None
        self._served = None
        self._storage = None
        self._subresources = None
        self.discriminator = None

        if additional_printer_columns is not None:
            self.additional_printer_columns = additional_printer_columns
        self.name = name
        if schema is not None:
            self.schema = schema
        self.served = served
        self.storage = storage
        if subresources is not None:
            self.subresources = subresources

    @property
    def additional_printer_columns(self):
        """Gets the additional_printer_columns of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501

        additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead). If no top-level or per-version columns are specified, a single column displaying the age of the custom resource is used.  # noqa: E501

        :return: The additional_printer_columns of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: list[V1beta1CustomResourceColumnDefinition]
        """
        return self._additional_printer_columns

    @additional_printer_columns.setter
    def additional_printer_columns(self, additional_printer_columns):
        """Sets the additional_printer_columns of this V1beta1CustomResourceDefinitionVersion.

        additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead). If no top-level or per-version columns are specified, a single column displaying the age of the custom resource is used.  # noqa: E501

        :param additional_printer_columns: The additional_printer_columns of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: list[V1beta1CustomResourceColumnDefinition]
        """

        self._additional_printer_columns = additional_printer_columns

    @property
    def name(self):
        """Gets the name of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501

        name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true.  # noqa: E501

        :return: The name of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1CustomResourceDefinitionVersion.

        name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true.  # noqa: E501

        :param name: The name of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501


        :return: The schema of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: V1beta1CustomResourceValidation
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this V1beta1CustomResourceDefinitionVersion.


        :param schema: The schema of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: V1beta1CustomResourceValidation
        """

        self._schema = schema

    @property
    def served(self):
        """Gets the served of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501

        served is a flag enabling/disabling this version from being served via REST APIs  # noqa: E501

        :return: The served of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: bool
        """
        return self._served

    @served.setter
    def served(self, served):
        """Sets the served of this V1beta1CustomResourceDefinitionVersion.

        served is a flag enabling/disabling this version from being served via REST APIs  # noqa: E501

        :param served: The served of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and served is None:  # noqa: E501
            raise ValueError("Invalid value for `served`, must not be `None`")  # noqa: E501

        self._served = served

    @property
    def storage(self):
        """Gets the storage of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501

        storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.  # noqa: E501

        :return: The storage of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: bool
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this V1beta1CustomResourceDefinitionVersion.

        storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.  # noqa: E501

        :param storage: The storage of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and storage is None:  # noqa: E501
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def subresources(self):
        """Gets the subresources of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501


        :return: The subresources of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: V1beta1CustomResourceSubresources
        """
        return self._subresources

    @subresources.setter
    def subresources(self, subresources):
        """Sets the subresources of this V1beta1CustomResourceDefinitionVersion.


        :param subresources: The subresources of this V1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: V1beta1CustomResourceSubresources
        """

        self._subresources = subresources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1beta1CustomResourceDefinitionVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1CustomResourceDefinitionVersion):
            return True

        return self.to_dict() != other.to_dict()
