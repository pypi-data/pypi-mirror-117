"""Tests of the Bank module."""

import json
import unittest
from unittest.mock import patch

from bank import BankRestClient
from cosm.tests.helpers import MockQueryRestClient
from cosmos.bank.v1beta1.bank_pb2 import Metadata, Params
from cosmos.bank.v1beta1.query_pb2 import (
    QueryAllBalancesRequest,
    QueryAllBalancesResponse,
    QueryBalanceRequest,
    QueryBalanceResponse,
    QueryDenomMetadataRequest,
    QueryDenomMetadataResponse,
    QueryDenomsMetadataRequest,
    QueryDenomsMetadataResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QuerySupplyOfRequest,
    QuerySupplyOfResponse,
    QueryTotalSupplyRequest,
    QueryTotalSupplyResponse,
)
from cosmos.base.query.v1beta1.pagination_pb2 import PageResponse
from cosmos.base.v1beta1.coin_pb2 import Coin


class BankTests(unittest.TestCase):
    """Test case of Bank module."""

    @staticmethod
    def test_query_balance():
        """Test query balance for the positive result."""
        expected_response = QueryBalanceResponse(
            balance=Coin(denom="stake", amount="1234")
        )
        content = {"balance": {"denom": "stake", "amount": "1234"}}
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert (
                bank.Balance(QueryBalanceRequest(address="account", denom="denom"))
                == expected_response  # noqa W503
            )
            assert (
                mock_client.last_request
                == "/cosmos/bank/v1beta1/balances/account/denom"  # noqa W503
            )

    @staticmethod
    def test_query_all_balances():
        """Test query all balances for the positive result."""
        expected_response = QueryAllBalancesResponse(
            balances=[Coin(denom="stake", amount="1234")],
            pagination=PageResponse(next_key=None, total=0),
        )
        content = {
            "balances": [{"denom": "stake", "amount": "1234"}],
            "pagination": {"next_key": None, "total": 0},
        }
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert (
                bank.AllBalances(QueryAllBalancesRequest(address="account"))
                == expected_response  # noqa W503
            )
            assert mock_client.last_request == "/cosmos/bank/v1beta1/balances/account"

    @staticmethod
    def test_query_total_supply():
        """Test query total supply for the positive result."""
        expected_response = QueryTotalSupplyResponse(
            supply=[Coin(denom="stake", amount="1234")]
        )
        content = {"supply": [{"denom": "stake", "amount": "1234"}]}
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert bank.TotalSupply(QueryTotalSupplyRequest()) == expected_response
            assert mock_client.last_request == "/cosmos/bank/v1beta1/supply"

    @staticmethod
    def test_query_supply_of():
        """Test query supply for the positive result."""
        expected_response = QuerySupplyOfResponse(
            amount=Coin(denom="stake", amount="1234")
        )
        content = {"amount": {"denom": "stake", "amount": "1234"}}
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert (
                bank.SupplyOf(QuerySupplyOfRequest(denom="denom")) == expected_response
            )
            assert mock_client.last_request == "/cosmos/bank/v1beta1/supply/denom"

    @staticmethod
    def test_query_params():
        """Test query params for the positive result."""
        expected_response = QueryParamsResponse(
            params=Params(default_send_enabled=True)
        )
        content = {"params": {"default_send_enabled": True}}
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert bank.Params(QueryParamsRequest()) == expected_response
            assert mock_client.last_request == "/cosmos/bank/v1beta1/params"

    @staticmethod
    def test_query_denoms_metadata():
        """Test query denoms metadata for the positive result."""
        expected_response = QueryDenomsMetadataResponse(
            pagination=PageResponse(next_key=None, total=0)
        )
        content = {"metadatas": [], "pagination": {"next_key": None, "total": 0}}
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert (
                bank.DenomsMetadata(QueryDenomsMetadataRequest()) == expected_response
            )
            assert mock_client.last_request == "/cosmos/bank/v1beta1/denoms_metadata"

    @staticmethod
    def test_query_denom_metadata():
        """Test query denom metadata for the positive result."""
        expected_response = QueryDenomMetadataResponse(metadata=Metadata())
        content = {
            "metadata": {
                "base": "",
                "denom_units": [],
                "description": "",
                "display": "",
            }
        }
        mock_client = MockQueryRestClient(json.dumps(content))

        bank = BankRestClient(mock_client)

        with patch.object(bank, "_rest_api", mock_client):
            assert (
                bank.DenomMetadata(QueryDenomMetadataRequest(denom="denom"))
                == expected_response  # noqa W503
            )
            assert (
                mock_client.last_request
                == "/cosmos/bank/v1beta1/denoms_metadata/denom"  # noqa W503
            )
