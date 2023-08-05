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


class V1StatusDetails(object):
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
        'causes': 'list[V1StatusCause]',
        'group': 'str',
        'kind': 'str',
        'name': 'str',
        'retry_after_seconds': 'int',
        'uid': 'str'
    }

    attribute_map = {
        'causes': 'causes',
        'group': 'group',
        'kind': 'kind',
        'name': 'name',
        'retry_after_seconds': 'retryAfterSeconds',
        'uid': 'uid'
    }

    def __init__(self, causes=None, group=None, kind=None, name=None, retry_after_seconds=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """V1StatusDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._causes = None
        self._group = None
        self._kind = None
        self._name = None
        self._retry_after_seconds = None
        self._uid = None
        self.discriminator = None

        if causes is not None:
            self.causes = causes
        if group is not None:
            self.group = group
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if retry_after_seconds is not None:
            self.retry_after_seconds = retry_after_seconds
        if uid is not None:
            self.uid = uid

    @property
    def causes(self):
        """Gets the causes of this V1StatusDetails.  # noqa: E501

        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.  # noqa: E501

        :return: The causes of this V1StatusDetails.  # noqa: E501
        :rtype: list[V1StatusCause]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """Sets the causes of this V1StatusDetails.

        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.  # noqa: E501

        :param causes: The causes of this V1StatusDetails.  # noqa: E501
        :type: list[V1StatusCause]
        """

        self._causes = causes

    @property
    def group(self):
        """Gets the group of this V1StatusDetails.  # noqa: E501

        The group attribute of the resource associated with the status StatusReason.  # noqa: E501

        :return: The group of this V1StatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1StatusDetails.

        The group attribute of the resource associated with the status StatusReason.  # noqa: E501

        :param group: The group of this V1StatusDetails.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this V1StatusDetails.  # noqa: E501

        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1StatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1StatusDetails.

        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1StatusDetails.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1StatusDetails.  # noqa: E501

        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).  # noqa: E501

        :return: The name of this V1StatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1StatusDetails.

        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).  # noqa: E501

        :param name: The name of this V1StatusDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def retry_after_seconds(self):
        """Gets the retry_after_seconds of this V1StatusDetails.  # noqa: E501

        If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.  # noqa: E501

        :return: The retry_after_seconds of this V1StatusDetails.  # noqa: E501
        :rtype: int
        """
        return self._retry_after_seconds

    @retry_after_seconds.setter
    def retry_after_seconds(self, retry_after_seconds):
        """Sets the retry_after_seconds of this V1StatusDetails.

        If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.  # noqa: E501

        :param retry_after_seconds: The retry_after_seconds of this V1StatusDetails.  # noqa: E501
        :type: int
        """

        self._retry_after_seconds = retry_after_seconds

    @property
    def uid(self):
        """Gets the uid of this V1StatusDetails.  # noqa: E501

        UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids  # noqa: E501

        :return: The uid of this V1StatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1StatusDetails.

        UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids  # noqa: E501

        :param uid: The uid of this V1StatusDetails.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, V1StatusDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1StatusDetails):
            return True

        return self.to_dict() != other.to_dict()
