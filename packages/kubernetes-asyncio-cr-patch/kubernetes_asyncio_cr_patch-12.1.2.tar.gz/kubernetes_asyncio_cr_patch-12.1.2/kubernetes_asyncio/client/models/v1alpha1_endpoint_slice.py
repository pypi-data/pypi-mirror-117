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


class V1alpha1EndpointSlice(object):
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
        'address_type': 'str',
        'api_version': 'str',
        'endpoints': 'list[V1alpha1Endpoint]',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'ports': 'list[V1alpha1EndpointPort]'
    }

    attribute_map = {
        'address_type': 'addressType',
        'api_version': 'apiVersion',
        'endpoints': 'endpoints',
        'kind': 'kind',
        'metadata': 'metadata',
        'ports': 'ports'
    }

    def __init__(self, address_type=None, api_version=None, endpoints=None, kind=None, metadata=None, ports=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1EndpointSlice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_type = None
        self._api_version = None
        self._endpoints = None
        self._kind = None
        self._metadata = None
        self._ports = None
        self.discriminator = None

        if address_type is not None:
            self.address_type = address_type
        if api_version is not None:
            self.api_version = api_version
        self.endpoints = endpoints
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if ports is not None:
            self.ports = ports

    @property
    def address_type(self):
        """Gets the address_type of this V1alpha1EndpointSlice.  # noqa: E501

        addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. Default is IP  # noqa: E501

        :return: The address_type of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this V1alpha1EndpointSlice.

        addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. Default is IP  # noqa: E501

        :param address_type: The address_type of this V1alpha1EndpointSlice.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def api_version(self):
        """Gets the api_version of this V1alpha1EndpointSlice.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1alpha1EndpointSlice.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1alpha1EndpointSlice.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def endpoints(self):
        """Gets the endpoints of this V1alpha1EndpointSlice.  # noqa: E501

        endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.  # noqa: E501

        :return: The endpoints of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: list[V1alpha1Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this V1alpha1EndpointSlice.

        endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.  # noqa: E501

        :param endpoints: The endpoints of this V1alpha1EndpointSlice.  # noqa: E501
        :type: list[V1alpha1Endpoint]
        """
        if self.local_vars_configuration.client_side_validation and endpoints is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def kind(self):
        """Gets the kind of this V1alpha1EndpointSlice.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1EndpointSlice.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1alpha1EndpointSlice.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1EndpointSlice.  # noqa: E501


        :return: The metadata of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1EndpointSlice.


        :param metadata: The metadata of this V1alpha1EndpointSlice.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def ports(self):
        """Gets the ports of this V1alpha1EndpointSlice.  # noqa: E501

        ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates \"all ports\". Each slice may include a maximum of 100 ports.  # noqa: E501

        :return: The ports of this V1alpha1EndpointSlice.  # noqa: E501
        :rtype: list[V1alpha1EndpointPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1alpha1EndpointSlice.

        ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates \"all ports\". Each slice may include a maximum of 100 ports.  # noqa: E501

        :param ports: The ports of this V1alpha1EndpointSlice.  # noqa: E501
        :type: list[V1alpha1EndpointPort]
        """

        self._ports = ports

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
        if not isinstance(other, V1alpha1EndpointSlice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1EndpointSlice):
            return True

        return self.to_dict() != other.to_dict()
