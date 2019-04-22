# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.9.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProcessorDTO(object):
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
        'versioned_component_id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'name': 'str',
        'type': 'str',
        'bundle': 'BundleDTO',
        'state': 'str',
        'style': 'dict(str, str)',
        'relationships': 'list[RelationshipDTO]',
        'description': 'str',
        'supports_parallel_processing': 'bool',
        'supports_event_driven': 'bool',
        'supports_batching': 'bool',
        'persists_state': 'bool',
        'restricted': 'bool',
        'deprecated': 'bool',
        'execution_node_restricted': 'bool',
        'multiple_versions_available': 'bool',
        'input_requirement': 'str',
        'config': 'ProcessorConfigDTO',
        'validation_errors': 'list[str]',
        'validation_status': 'str',
        'extension_missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'type': 'type',
        'bundle': 'bundle',
        'state': 'state',
        'style': 'style',
        'relationships': 'relationships',
        'description': 'description',
        'supports_parallel_processing': 'supportsParallelProcessing',
        'supports_event_driven': 'supportsEventDriven',
        'supports_batching': 'supportsBatching',
        'persists_state': 'persistsState',
        'restricted': 'restricted',
        'deprecated': 'deprecated',
        'execution_node_restricted': 'executionNodeRestricted',
        'multiple_versions_available': 'multipleVersionsAvailable',
        'input_requirement': 'inputRequirement',
        'config': 'config',
        'validation_errors': 'validationErrors',
        'validation_status': 'validationStatus',
        'extension_missing': 'extensionMissing'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, name=None, type=None, bundle=None, state=None, style=None, relationships=None, description=None, supports_parallel_processing=None, supports_event_driven=None, supports_batching=None, persists_state=None, restricted=None, deprecated=None, execution_node_restricted=None, multiple_versions_available=None, input_requirement=None, config=None, validation_errors=None, validation_status=None, extension_missing=None):
        """
        ProcessorDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._type = None
        self._bundle = None
        self._state = None
        self._style = None
        self._relationships = None
        self._description = None
        self._supports_parallel_processing = None
        self._supports_event_driven = None
        self._supports_batching = None
        self._persists_state = None
        self._restricted = None
        self._deprecated = None
        self._execution_node_restricted = None
        self._multiple_versions_available = None
        self._input_requirement = None
        self._config = None
        self._validation_errors = None
        self._validation_status = None
        self._extension_missing = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if bundle is not None:
          self.bundle = bundle
        if state is not None:
          self.state = state
        if style is not None:
          self.style = style
        if relationships is not None:
          self.relationships = relationships
        if description is not None:
          self.description = description
        if supports_parallel_processing is not None:
          self.supports_parallel_processing = supports_parallel_processing
        if supports_event_driven is not None:
          self.supports_event_driven = supports_event_driven
        if supports_batching is not None:
          self.supports_batching = supports_batching
        if persists_state is not None:
          self.persists_state = persists_state
        if restricted is not None:
          self.restricted = restricted
        if deprecated is not None:
          self.deprecated = deprecated
        if execution_node_restricted is not None:
          self.execution_node_restricted = execution_node_restricted
        if multiple_versions_available is not None:
          self.multiple_versions_available = multiple_versions_available
        if input_requirement is not None:
          self.input_requirement = input_requirement
        if config is not None:
          self.config = config
        if validation_errors is not None:
          self.validation_errors = validation_errors
        if validation_status is not None:
          self.validation_status = validation_status
        if extension_missing is not None:
          self.extension_missing = extension_missing

    @property
    def id(self):
        """
        Gets the id of this ProcessorDTO.
        The id of the component.

        :return: The id of this ProcessorDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessorDTO.
        The id of the component.

        :param id: The id of this ProcessorDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this ProcessorDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this ProcessorDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this ProcessorDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this ProcessorDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ProcessorDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ProcessorDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ProcessorDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ProcessorDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this ProcessorDTO.
        The position of this component in the UI if applicable.

        :return: The position of this ProcessorDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ProcessorDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this ProcessorDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """
        Gets the name of this ProcessorDTO.
        The name of the processor.

        :return: The name of this ProcessorDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessorDTO.
        The name of the processor.

        :param name: The name of this ProcessorDTO.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ProcessorDTO.
        The type of the processor.

        :return: The type of this ProcessorDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProcessorDTO.
        The type of the processor.

        :param type: The type of this ProcessorDTO.
        :type: str
        """

        self._type = type

    @property
    def bundle(self):
        """
        Gets the bundle of this ProcessorDTO.
        The details of the artifact that bundled this processor type.

        :return: The bundle of this ProcessorDTO.
        :rtype: BundleDTO
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """
        Sets the bundle of this ProcessorDTO.
        The details of the artifact that bundled this processor type.

        :param bundle: The bundle of this ProcessorDTO.
        :type: BundleDTO
        """

        self._bundle = bundle

    @property
    def state(self):
        """
        Gets the state of this ProcessorDTO.
        The state of the processor

        :return: The state of this ProcessorDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ProcessorDTO.
        The state of the processor

        :param state: The state of this ProcessorDTO.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "DISABLED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def style(self):
        """
        Gets the style of this ProcessorDTO.
        Styles for the processor (background-color : #eee).

        :return: The style of this ProcessorDTO.
        :rtype: dict(str, str)
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Sets the style of this ProcessorDTO.
        Styles for the processor (background-color : #eee).

        :param style: The style of this ProcessorDTO.
        :type: dict(str, str)
        """

        self._style = style

    @property
    def relationships(self):
        """
        Gets the relationships of this ProcessorDTO.
        The available relationships that the processor currently supports.

        :return: The relationships of this ProcessorDTO.
        :rtype: list[RelationshipDTO]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this ProcessorDTO.
        The available relationships that the processor currently supports.

        :param relationships: The relationships of this ProcessorDTO.
        :type: list[RelationshipDTO]
        """

        self._relationships = relationships

    @property
    def description(self):
        """
        Gets the description of this ProcessorDTO.
        The description of the processor.

        :return: The description of this ProcessorDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProcessorDTO.
        The description of the processor.

        :param description: The description of this ProcessorDTO.
        :type: str
        """

        self._description = description

    @property
    def supports_parallel_processing(self):
        """
        Gets the supports_parallel_processing of this ProcessorDTO.
        Whether the processor supports parallel processing.

        :return: The supports_parallel_processing of this ProcessorDTO.
        :rtype: bool
        """
        return self._supports_parallel_processing

    @supports_parallel_processing.setter
    def supports_parallel_processing(self, supports_parallel_processing):
        """
        Sets the supports_parallel_processing of this ProcessorDTO.
        Whether the processor supports parallel processing.

        :param supports_parallel_processing: The supports_parallel_processing of this ProcessorDTO.
        :type: bool
        """

        self._supports_parallel_processing = supports_parallel_processing

    @property
    def supports_event_driven(self):
        """
        Gets the supports_event_driven of this ProcessorDTO.
        Whether the processor supports event driven scheduling.

        :return: The supports_event_driven of this ProcessorDTO.
        :rtype: bool
        """
        return self._supports_event_driven

    @supports_event_driven.setter
    def supports_event_driven(self, supports_event_driven):
        """
        Sets the supports_event_driven of this ProcessorDTO.
        Whether the processor supports event driven scheduling.

        :param supports_event_driven: The supports_event_driven of this ProcessorDTO.
        :type: bool
        """

        self._supports_event_driven = supports_event_driven

    @property
    def supports_batching(self):
        """
        Gets the supports_batching of this ProcessorDTO.
        Whether the processor supports batching. This makes the run duration settings available.

        :return: The supports_batching of this ProcessorDTO.
        :rtype: bool
        """
        return self._supports_batching

    @supports_batching.setter
    def supports_batching(self, supports_batching):
        """
        Sets the supports_batching of this ProcessorDTO.
        Whether the processor supports batching. This makes the run duration settings available.

        :param supports_batching: The supports_batching of this ProcessorDTO.
        :type: bool
        """

        self._supports_batching = supports_batching

    @property
    def persists_state(self):
        """
        Gets the persists_state of this ProcessorDTO.
        Whether the processor persists state.

        :return: The persists_state of this ProcessorDTO.
        :rtype: bool
        """
        return self._persists_state

    @persists_state.setter
    def persists_state(self, persists_state):
        """
        Sets the persists_state of this ProcessorDTO.
        Whether the processor persists state.

        :param persists_state: The persists_state of this ProcessorDTO.
        :type: bool
        """

        self._persists_state = persists_state

    @property
    def restricted(self):
        """
        Gets the restricted of this ProcessorDTO.
        Whether the processor requires elevated privileges.

        :return: The restricted of this ProcessorDTO.
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this ProcessorDTO.
        Whether the processor requires elevated privileges.

        :param restricted: The restricted of this ProcessorDTO.
        :type: bool
        """

        self._restricted = restricted

    @property
    def deprecated(self):
        """
        Gets the deprecated of this ProcessorDTO.
        Whether the processor has been deprecated.

        :return: The deprecated of this ProcessorDTO.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this ProcessorDTO.
        Whether the processor has been deprecated.

        :param deprecated: The deprecated of this ProcessorDTO.
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def execution_node_restricted(self):
        """
        Gets the execution_node_restricted of this ProcessorDTO.
        Indicates if the execution node of a processor is restricted to run only on the primary node

        :return: The execution_node_restricted of this ProcessorDTO.
        :rtype: bool
        """
        return self._execution_node_restricted

    @execution_node_restricted.setter
    def execution_node_restricted(self, execution_node_restricted):
        """
        Sets the execution_node_restricted of this ProcessorDTO.
        Indicates if the execution node of a processor is restricted to run only on the primary node

        :param execution_node_restricted: The execution_node_restricted of this ProcessorDTO.
        :type: bool
        """

        self._execution_node_restricted = execution_node_restricted

    @property
    def multiple_versions_available(self):
        """
        Gets the multiple_versions_available of this ProcessorDTO.
        Whether the processor has multiple versions available.

        :return: The multiple_versions_available of this ProcessorDTO.
        :rtype: bool
        """
        return self._multiple_versions_available

    @multiple_versions_available.setter
    def multiple_versions_available(self, multiple_versions_available):
        """
        Sets the multiple_versions_available of this ProcessorDTO.
        Whether the processor has multiple versions available.

        :param multiple_versions_available: The multiple_versions_available of this ProcessorDTO.
        :type: bool
        """

        self._multiple_versions_available = multiple_versions_available

    @property
    def input_requirement(self):
        """
        Gets the input_requirement of this ProcessorDTO.
        The input requirement for this processor.

        :return: The input_requirement of this ProcessorDTO.
        :rtype: str
        """
        return self._input_requirement

    @input_requirement.setter
    def input_requirement(self, input_requirement):
        """
        Sets the input_requirement of this ProcessorDTO.
        The input requirement for this processor.

        :param input_requirement: The input_requirement of this ProcessorDTO.
        :type: str
        """

        self._input_requirement = input_requirement

    @property
    def config(self):
        """
        Gets the config of this ProcessorDTO.
        The configuration details for the processor. These details will be included in a response if the verbose flag is included in a request.

        :return: The config of this ProcessorDTO.
        :rtype: ProcessorConfigDTO
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this ProcessorDTO.
        The configuration details for the processor. These details will be included in a response if the verbose flag is included in a request.

        :param config: The config of this ProcessorDTO.
        :type: ProcessorConfigDTO
        """

        self._config = config

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this ProcessorDTO.
        The validation errors for the processor. These validation errors represent the problems with the processor that must be resolved before it can be started.

        :return: The validation_errors of this ProcessorDTO.
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this ProcessorDTO.
        The validation errors for the processor. These validation errors represent the problems with the processor that must be resolved before it can be started.

        :param validation_errors: The validation_errors of this ProcessorDTO.
        :type: list[str]
        """

        self._validation_errors = validation_errors

    @property
    def validation_status(self):
        """
        Gets the validation_status of this ProcessorDTO.
        Indicates whether the Processor is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the Processor is valid)

        :return: The validation_status of this ProcessorDTO.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this ProcessorDTO.
        Indicates whether the Processor is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the Processor is valid)

        :param validation_status: The validation_status of this ProcessorDTO.
        :type: str
        """
        allowed_values = ["VALID", "INVALID", "VALIDATING"]
        if validation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `validation_status` ({0}), must be one of {1}"
                .format(validation_status, allowed_values)
            )

        self._validation_status = validation_status

    @property
    def extension_missing(self):
        """
        Gets the extension_missing of this ProcessorDTO.
        Whether the underlying extension is missing.

        :return: The extension_missing of this ProcessorDTO.
        :rtype: bool
        """
        return self._extension_missing

    @extension_missing.setter
    def extension_missing(self, extension_missing):
        """
        Sets the extension_missing of this ProcessorDTO.
        Whether the underlying extension is missing.

        :param extension_missing: The extension_missing of this ProcessorDTO.
        :type: bool
        """

        self._extension_missing = extension_missing

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
        if not isinstance(other, ProcessorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
