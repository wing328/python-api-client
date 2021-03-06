# coding: utf-8

"""
    Quant Trading Network API

    This API will use JSON.         JSON looks like this:                {         \"key\": \"value\",         \"anotherKey\": \"anotherValue\"       }  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@quant-trading.network
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ExecPositionManagerAlgoRequest(object):
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
        'long_stake_state': 'StakeState',
        'short_stake_state': 'StakeState',
        'current_position_pct': 'CurrentPositionPct',
        'current_unrealised_pct': 'CurrentUnrealisedPct',
        'avg_open_position_hours': 'AvgOpenPositionHours',
        'last_open_stake_hours': 'LastOpenStakeHours',
        'closed_position_hours': 'ClosedPositionHours'
    }

    attribute_map = {
        'long_stake_state': 'longStakeState',
        'short_stake_state': 'shortStakeState',
        'current_position_pct': 'currentPositionPct',
        'current_unrealised_pct': 'currentUnrealisedPct',
        'avg_open_position_hours': 'avgOpenPositionHours',
        'last_open_stake_hours': 'lastOpenStakeHours',
        'closed_position_hours': 'closedPositionHours'
    }

    def __init__(self, long_stake_state=None, short_stake_state=None, current_position_pct=None, current_unrealised_pct=None, avg_open_position_hours=None, last_open_stake_hours=None, closed_position_hours=None):  # noqa: E501
        """ExecPositionManagerAlgoRequest - a model defined in Swagger"""  # noqa: E501
        self._long_stake_state = None
        self._short_stake_state = None
        self._current_position_pct = None
        self._current_unrealised_pct = None
        self._avg_open_position_hours = None
        self._last_open_stake_hours = None
        self._closed_position_hours = None
        self.discriminator = None
        self.long_stake_state = long_stake_state
        self.short_stake_state = short_stake_state
        self.current_position_pct = current_position_pct
        self.current_unrealised_pct = current_unrealised_pct
        self.avg_open_position_hours = avg_open_position_hours
        self.last_open_stake_hours = last_open_stake_hours
        self.closed_position_hours = closed_position_hours

    @property
    def long_stake_state(self):
        """Gets the long_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The long_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: StakeState
        """
        return self._long_stake_state

    @long_stake_state.setter
    def long_stake_state(self, long_stake_state):
        """Sets the long_stake_state of this ExecPositionManagerAlgoRequest.


        :param long_stake_state: The long_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: StakeState
        """
        if long_stake_state is None:
            raise ValueError("Invalid value for `long_stake_state`, must not be `None`")  # noqa: E501

        self._long_stake_state = long_stake_state

    @property
    def short_stake_state(self):
        """Gets the short_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The short_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: StakeState
        """
        return self._short_stake_state

    @short_stake_state.setter
    def short_stake_state(self, short_stake_state):
        """Sets the short_stake_state of this ExecPositionManagerAlgoRequest.


        :param short_stake_state: The short_stake_state of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: StakeState
        """
        if short_stake_state is None:
            raise ValueError("Invalid value for `short_stake_state`, must not be `None`")  # noqa: E501

        self._short_stake_state = short_stake_state

    @property
    def current_position_pct(self):
        """Gets the current_position_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The current_position_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: CurrentPositionPct
        """
        return self._current_position_pct

    @current_position_pct.setter
    def current_position_pct(self, current_position_pct):
        """Sets the current_position_pct of this ExecPositionManagerAlgoRequest.


        :param current_position_pct: The current_position_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: CurrentPositionPct
        """
        if current_position_pct is None:
            raise ValueError("Invalid value for `current_position_pct`, must not be `None`")  # noqa: E501

        self._current_position_pct = current_position_pct

    @property
    def current_unrealised_pct(self):
        """Gets the current_unrealised_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The current_unrealised_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: CurrentUnrealisedPct
        """
        return self._current_unrealised_pct

    @current_unrealised_pct.setter
    def current_unrealised_pct(self, current_unrealised_pct):
        """Sets the current_unrealised_pct of this ExecPositionManagerAlgoRequest.


        :param current_unrealised_pct: The current_unrealised_pct of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: CurrentUnrealisedPct
        """
        if current_unrealised_pct is None:
            raise ValueError("Invalid value for `current_unrealised_pct`, must not be `None`")  # noqa: E501

        self._current_unrealised_pct = current_unrealised_pct

    @property
    def avg_open_position_hours(self):
        """Gets the avg_open_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The avg_open_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: AvgOpenPositionHours
        """
        return self._avg_open_position_hours

    @avg_open_position_hours.setter
    def avg_open_position_hours(self, avg_open_position_hours):
        """Sets the avg_open_position_hours of this ExecPositionManagerAlgoRequest.


        :param avg_open_position_hours: The avg_open_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: AvgOpenPositionHours
        """
        if avg_open_position_hours is None:
            raise ValueError("Invalid value for `avg_open_position_hours`, must not be `None`")  # noqa: E501

        self._avg_open_position_hours = avg_open_position_hours

    @property
    def last_open_stake_hours(self):
        """Gets the last_open_stake_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The last_open_stake_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: LastOpenStakeHours
        """
        return self._last_open_stake_hours

    @last_open_stake_hours.setter
    def last_open_stake_hours(self, last_open_stake_hours):
        """Sets the last_open_stake_hours of this ExecPositionManagerAlgoRequest.


        :param last_open_stake_hours: The last_open_stake_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: LastOpenStakeHours
        """
        if last_open_stake_hours is None:
            raise ValueError("Invalid value for `last_open_stake_hours`, must not be `None`")  # noqa: E501

        self._last_open_stake_hours = last_open_stake_hours

    @property
    def closed_position_hours(self):
        """Gets the closed_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501


        :return: The closed_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :rtype: ClosedPositionHours
        """
        return self._closed_position_hours

    @closed_position_hours.setter
    def closed_position_hours(self, closed_position_hours):
        """Sets the closed_position_hours of this ExecPositionManagerAlgoRequest.


        :param closed_position_hours: The closed_position_hours of this ExecPositionManagerAlgoRequest.  # noqa: E501
        :type: ClosedPositionHours
        """
        if closed_position_hours is None:
            raise ValueError("Invalid value for `closed_position_hours`, must not be `None`")  # noqa: E501

        self._closed_position_hours = closed_position_hours

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
        if issubclass(ExecPositionManagerAlgoRequest, dict):
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
        if not isinstance(other, ExecPositionManagerAlgoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
