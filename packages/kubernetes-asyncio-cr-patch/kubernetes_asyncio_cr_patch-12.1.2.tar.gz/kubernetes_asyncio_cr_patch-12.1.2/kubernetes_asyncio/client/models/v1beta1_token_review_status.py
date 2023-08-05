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


class V1beta1TokenReviewStatus(object):
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
        'audiences': 'list[str]',
        'authenticated': 'bool',
        'error': 'str',
        'user': 'V1beta1UserInfo'
    }

    attribute_map = {
        'audiences': 'audiences',
        'authenticated': 'authenticated',
        'error': 'error',
        'user': 'user'
    }

    def __init__(self, audiences=None, authenticated=None, error=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1TokenReviewStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audiences = None
        self._authenticated = None
        self._error = None
        self._user = None
        self.discriminator = None

        if audiences is not None:
            self.audiences = audiences
        if authenticated is not None:
            self.authenticated = authenticated
        if error is not None:
            self.error = error
        if user is not None:
            self.user = user

    @property
    def audiences(self):
        """Gets the audiences of this V1beta1TokenReviewStatus.  # noqa: E501

        Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \"true\", the token is valid against the audience of the Kubernetes API server.  # noqa: E501

        :return: The audiences of this V1beta1TokenReviewStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this V1beta1TokenReviewStatus.

        Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \"true\", the token is valid against the audience of the Kubernetes API server.  # noqa: E501

        :param audiences: The audiences of this V1beta1TokenReviewStatus.  # noqa: E501
        :type: list[str]
        """

        self._audiences = audiences

    @property
    def authenticated(self):
        """Gets the authenticated of this V1beta1TokenReviewStatus.  # noqa: E501

        Authenticated indicates that the token was associated with a known user.  # noqa: E501

        :return: The authenticated of this V1beta1TokenReviewStatus.  # noqa: E501
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """Sets the authenticated of this V1beta1TokenReviewStatus.

        Authenticated indicates that the token was associated with a known user.  # noqa: E501

        :param authenticated: The authenticated of this V1beta1TokenReviewStatus.  # noqa: E501
        :type: bool
        """

        self._authenticated = authenticated

    @property
    def error(self):
        """Gets the error of this V1beta1TokenReviewStatus.  # noqa: E501

        Error indicates that the token couldn't be checked  # noqa: E501

        :return: The error of this V1beta1TokenReviewStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1beta1TokenReviewStatus.

        Error indicates that the token couldn't be checked  # noqa: E501

        :param error: The error of this V1beta1TokenReviewStatus.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def user(self):
        """Gets the user of this V1beta1TokenReviewStatus.  # noqa: E501


        :return: The user of this V1beta1TokenReviewStatus.  # noqa: E501
        :rtype: V1beta1UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1beta1TokenReviewStatus.


        :param user: The user of this V1beta1TokenReviewStatus.  # noqa: E501
        :type: V1beta1UserInfo
        """

        self._user = user

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
        if not isinstance(other, V1beta1TokenReviewStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1TokenReviewStatus):
            return True

        return self.to_dict() != other.to_dict()
