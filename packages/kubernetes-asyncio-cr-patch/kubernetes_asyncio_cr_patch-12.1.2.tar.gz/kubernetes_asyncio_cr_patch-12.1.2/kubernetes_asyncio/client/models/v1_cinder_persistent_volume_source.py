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


class V1CinderPersistentVolumeSource(object):
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
        'fs_type': 'str',
        'read_only': 'bool',
        'secret_ref': 'V1SecretReference',
        'volume_id': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'volume_id': 'volumeID'
    }

    def __init__(self, fs_type=None, read_only=None, secret_ref=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """V1CinderPersistentVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fs_type = None
        self._read_only = None
        self._secret_ref = None
        self._volume_id = None
        self.discriminator = None

        if fs_type is not None:
            self.fs_type = fs_type
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref
        self.volume_id = volume_id

    @property
    def fs_type(self):
        """Gets the fs_type of this V1CinderPersistentVolumeSource.  # noqa: E501

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :return: The fs_type of this V1CinderPersistentVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this V1CinderPersistentVolumeSource.

        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :param fs_type: The fs_type of this V1CinderPersistentVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def read_only(self):
        """Gets the read_only of this V1CinderPersistentVolumeSource.  # noqa: E501

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :return: The read_only of this V1CinderPersistentVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1CinderPersistentVolumeSource.

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :param read_only: The read_only of this V1CinderPersistentVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1CinderPersistentVolumeSource.  # noqa: E501


        :return: The secret_ref of this V1CinderPersistentVolumeSource.  # noqa: E501
        :rtype: V1SecretReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1CinderPersistentVolumeSource.


        :param secret_ref: The secret_ref of this V1CinderPersistentVolumeSource.  # noqa: E501
        :type: V1SecretReference
        """

        self._secret_ref = secret_ref

    @property
    def volume_id(self):
        """Gets the volume_id of this V1CinderPersistentVolumeSource.  # noqa: E501

        volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :return: The volume_id of this V1CinderPersistentVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this V1CinderPersistentVolumeSource.

        volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md  # noqa: E501

        :param volume_id: The volume_id of this V1CinderPersistentVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

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
        if not isinstance(other, V1CinderPersistentVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CinderPersistentVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
