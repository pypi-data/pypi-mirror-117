import os
from typing import Dict, List

import pandas as pd
import pytest

try:
    sqlalchemy = pytest.importorskip("sqlalchemy")
except ImportError:
    sqlalchemy = None

from ruamel.yaml import YAML

import great_expectations.exceptions as ge_exceptions
from great_expectations.core.batch import (
    Batch,
    BatchDefinition,
    IDDict,
    RuntimeBatchRequest,
)
from great_expectations.data_context.util import (
    file_relative_path,
    instantiate_class_from_config,
)
from great_expectations.datasource.new_datasource import Datasource

yaml = YAML()


@pytest.fixture
def basic_datasource_with_runtime_data_connector():
    basic_datasource: Datasource = instantiate_class_from_config(
        yaml.load(
            f"""
    class_name: Datasource

    execution_engine:
        class_name: PandasExecutionEngine

    data_connectors:
        test_runtime_data_connector:
            module_name: great_expectations.datasource.data_connector
            class_name: RuntimeDataConnector
            batch_identifiers:
                - pipeline_stage_name
                - airflow_run_id
                - custom_key_0
        """,
        ),
        runtime_environment={"name": "my_datasource"},
        config_defaults={"module_name": "great_expectations.datasource"},
    )
    return basic_datasource


def test_basic_datasource_runtime_data_connector_self_check(
    basic_datasource_with_runtime_data_connector,
):
    report = basic_datasource_with_runtime_data_connector.self_check()
    assert report == {
        "data_connectors": {
            "count": 1,
            "test_runtime_data_connector": {
                "class_name": "RuntimeDataConnector",
                "data_asset_count": 0,
                "data_assets": {},
                "example_data_asset_names": [],
                "example_unmatched_data_references": [],
                "note": "RuntimeDataConnector will not have data_asset_names until they are passed in through RuntimeBatchRequest",
                "unmatched_data_reference_count": 0,
            },
        },
        "execution_engine": {
            "boto3_options": {},
            "azure_options": {},
            "gcs_options": {},
            "caching": True,
            "class_name": "PandasExecutionEngine",
            "discard_subset_failing_expectations": False,
            "module_name": "great_expectations.execution_engine.pandas_execution_engine",
        },
    }


def test_basic_datasource_runtime_data_connector_error_checking_unknown_datasource(
    basic_datasource_with_runtime_data_connector,
):
    # Test for an unknown datasource
    with pytest.raises(ValueError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name="non_existent_datasource",
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
            )
        )


def test_basic_datasource_runtime_data_connector_error_checking_unknown_dataconnector(
    basic_datasource_with_runtime_data_connector,
):
    # Test for an unknown data_connector
    with pytest.raises(ValueError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=basic_datasource_with_runtime_data_connector.name,
                data_connector_name="non_existent_data_connector",
                data_asset_name="my_data_asset",
            )
        )


def test_basic_datasource_runtime_data_connector_error_checking_no_batch_idenfitiers(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # Test for illegal absence of batch_identifiers when batch_data is specified
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=basic_datasource_with_runtime_data_connector.name,
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
                runtime_parameters={"batch_data": test_df},
                batch_identifiers=None,
            )
        )


def test_basic_datasource_runtime_data_connector_error_checking_incorrect_batch_idenfitiers(
    basic_datasource_with_runtime_data_connector,
):

    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    # Test for illegal falsiness of batch_identifiers when batch_data is specified
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=basic_datasource_with_runtime_data_connector.name,
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
                runtime_parameters={"batch_data": test_df},
                batch_identifiers=dict(),
            )
        )


#########################################
# Tests with data passed in as batch_data
#########################################


def test_batch_identifiers_and_batch_identifiers_success_all_keys_present(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
    }

    # Verify that all keys in batch_identifiers are acceptable as batch_identifiers (using batch count).
    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "IN_MEMORY_DATA_ASSET",
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    assert len(batch_list) == 1


def test_batch_identifiers_and_batch_identifiers_error_mostly_legal_keys(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
        "i_am_illegal_key": "i_am_illegal_value",
    }

    # Insure that keys in batch_identifiers that are not among batch_identifiers declared in
    # configuration are not accepted.  In this test, all legal keys plus a single illegal key are present.
    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "IN_MEMORY_DATA_ASSET",
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_batch_identifiers_and_batch_identifiers_error_one_illegal_key(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_identifiers = {"unknown_key": "some_value"}
    # Insure that keys in batch_identifiers that are not among batch_identifiers declared in
    # configuration are not accepted.  In this test, a single illegal key is present.
    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "IN_MEMORY_DATA_ASSET",
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_set_data_asset_name_for_runtime_data(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
    }

    # set : my_runtime_data_asset
    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "my_runtime_data_asset",
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    assert batch_list[0].batch_definition.data_asset_name == "my_runtime_data_asset"


def test_get_available_data_asset_names(basic_datasource_with_runtime_data_connector):
    expected_available_data_asset_names: Dict[List[str]] = {
        "test_runtime_data_connector": []
    }
    available_data_asset_names: Dict[
        List[str]
    ] = basic_datasource_with_runtime_data_connector.get_available_data_asset_names()
    assert available_data_asset_names == expected_available_data_asset_names


def test_get_batch_definition_list_from_batch_request_length_one(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    batch_identifiers = {
        "airflow_run_id": 1234567890,
    }

    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "my_data_asset",
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    # batches are a little bit more difficult to test because of batch_markers
    # they are ones that uniquely identify the data
    assert len(batch_list) == 1
    my_batch_1 = batch_list[0]

    assert my_batch_1.batch_spec is not None
    assert my_batch_1.batch_definition["data_asset_name"] == "my_data_asset"
    assert isinstance(my_batch_1.data.dataframe, pd.DataFrame)
    assert my_batch_1.data.dataframe.shape == (2, 2)
    assert my_batch_1.data.dataframe["col2"].values[1] == 4
    assert (
        my_batch_1.batch_markers["pandas_data_fingerprint"]
        == "1e461a0df5fe0a6db2c3bc4ef88ef1f0"
    )


def test_get_batch_with_pipeline_style_batch_request_missing_batch_identifiers_error(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    data_connector_name: str = "test_runtime_data_connector"
    data_asset_name: str = "test_asset_1"

    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": data_connector_name,
        "data_asset_name": data_asset_name,
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": None,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = basic_datasource_with_runtime_data_connector.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_get_batch_definitions_and_get_batch_basics(
    basic_datasource_with_runtime_data_connector,
):
    test_df: pd.DataFrame = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})

    data_connector_name: str = "test_runtime_data_connector"
    data_asset_name: str = "test_asset_1"

    batch_request: dict = {
        "datasource_name": basic_datasource_with_runtime_data_connector.name,
        "data_connector_name": data_connector_name,
        "data_asset_name": data_asset_name,
        "runtime_parameters": {
            "batch_data": test_df,
        },
        "batch_identifiers": {
            "airflow_run_id": 1234567890,
        },
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    assert (
        len(
            basic_datasource_with_runtime_data_connector.get_available_batch_definitions(
                batch_request=batch_request
            )
        )
        == 1
    )

    my_df: pd.DataFrame = pd.DataFrame({"x": range(10), "y": range(10)})
    batch: Batch = (
        basic_datasource_with_runtime_data_connector.get_batch_from_batch_definition(
            batch_definition=BatchDefinition(
                "my_datasource",
                "_pipeline",
                "_pipeline",
                batch_identifiers=IDDict({"some_random_id": 1}),
            ),
            batch_data=my_df,
        )
    )
    assert batch.batch_request == {}


####################################
# Tests with data passed in as query
####################################


@pytest.fixture
def db_file():
    return file_relative_path(
        __file__,
        os.path.join("..", "test_sets", "test_cases_for_sql_data_connector.db"),
    )


@pytest.fixture
def datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine(db_file, sa):
    basic_datasource: Datasource = instantiate_class_from_config(
        yaml.load(
            f"""
    class_name: Datasource

    execution_engine:
        class_name: SqlAlchemyExecutionEngine
        connection_string: sqlite:///{db_file}

    data_connectors:
        test_runtime_data_connector:
            module_name: great_expectations.datasource.data_connector
            class_name: RuntimeDataConnector
            batch_identifiers:
                - pipeline_stage_name
                - airflow_run_id
                - custom_key_0
        """,
        ),
        runtime_environment={"name": "my_datasource"},
        config_defaults={"module_name": "great_expectations.datasource"},
    )
    return basic_datasource


def test_datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine_self_check(
    db_file, datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    report = (
        datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.self_check()
    )

    assert report == {
        "execution_engine": {
            "connection_string": f"sqlite:///{db_file}",
            "module_name": "great_expectations.execution_engine.sqlalchemy_execution_engine",
            "class_name": "SqlAlchemyExecutionEngine",
        },
        "data_connectors": {
            "count": 1,
            "test_runtime_data_connector": {
                "class_name": "RuntimeDataConnector",
                "data_asset_count": 0,
                "example_data_asset_names": [],
                "data_assets": {},
                "note": "RuntimeDataConnector will not have data_asset_names until they are passed in through RuntimeBatchRequest",
                "unmatched_data_reference_count": 0,
                "example_unmatched_data_references": [],
            },
        },
    }


def test_datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine_unknown_datasource(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):

    # Test for an unknown datasource
    with pytest.raises(ValueError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name="non_existent_datasource",
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
            )
        )


def test_datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine_unknown_dataconnector(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # Test for an unknown data_connector
    with pytest.raises(ValueError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
                data_connector_name="non_existent_data_connector",
                data_asset_name="my_data_asset",
            )
        )


def test_datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine_no_batch_identifiers(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"

    # Test for illegal absence of batch_identifiers when batch_data is specified
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
                runtime_parameters={"query": test_query},
                batch_identifiers=None,
            )
        )


def test_datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine_illegal_batch_identifiers(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"

    # Test for illegal falsiness of batch_identifiers when batch_data is specified
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=RuntimeBatchRequest(
                datasource_name=datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
                data_connector_name="test_runtime_data_connector",
                data_asset_name="my_data_asset",
                runtime_parameters={"query": test_query},
                batch_identifiers=dict(),
            )
        )


def test_batch_identifiers_and_batch_identifiers_success_all_keys_present_with_query(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
    }

    # Verify that all keys in batch_identifiers are acceptable as batch_identifiers (using batch count).
    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "TEMP_QUERY_DATA_ASSET",
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    assert len(batch_list) == 1


def test_batch_identifiers_and_batch_identifiers_error_illegal_key_with_query_mostly_legal_keys(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
        "i_am_illegal_key": "i_am_illegal_value",
    }

    # Insure that keys in batch_identifiers that are not among batch_identifiers declared in
    # configuration are not accepted.  In this test, all legal keys plus a single illegal key are present.
    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "TEMP_QUERY_DATA_ASSET",
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_batch_identifiers_and_batch_identifiers_error_illegal_key_with_query_single_illegal_key(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"
    batch_identifiers = {"unknown_key": "some_value"}
    # Insure that keys in batch_identifiers that are not among batch_identifiers declared in
    # configuration  are not accepted.  In this test, a single illegal key is present.
    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "TEMP_QUERY_DATA_ASSET",
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_set_data_asset_name_for_runtime_query_data(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    test_query: str = "SELECT * FROM table_full__I;"
    batch_identifiers = {
        "pipeline_stage_name": "core_processing",
        "airflow_run_id": 1234567890,
        "custom_key_0": "custom_value_0",
    }

    # set : my_runtime_data_asset
    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "my_runtime_data_asset",
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    assert batch_list[0].batch_definition.data_asset_name == "my_runtime_data_asset"


def test_get_batch_definition_list_from_batch_request_length_one_from_query(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"

    batch_identifiers = {
        "airflow_run_id": 1234567890,
    }

    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": "test_runtime_data_connector",
        "data_asset_name": "my_data_asset",
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": batch_identifiers,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    batch_list: List[
        Batch
    ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
        batch_request=batch_request
    )
    # batches are a little bit more difficult to test because of batch_markers
    # they are ones that uniquely identify the data
    assert len(batch_list) == 1
    my_batch_1 = batch_list[0]
    assert my_batch_1.batch_spec is not None
    assert my_batch_1.batch_definition["data_asset_name"] == "my_data_asset"
    assert isinstance(my_batch_1.data.selectable, sqlalchemy.Table)


def test_get_batch_with_pipeline_style_batch_request_missing_batch_identifiers_error(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"

    data_connector_name: str = "test_runtime_data_connector"
    data_asset_name: str = "test_asset_1"

    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": data_connector_name,
        "data_asset_name": data_asset_name,
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": None,
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)
    with pytest.raises(ge_exceptions.DataConnectorError):
        # noinspection PyUnusedLocal
        batch_list: List[
            Batch
        ] = datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_batch_list_from_batch_request(
            batch_request=batch_request
        )


def test_get_batch_definitions_and_get_batch_basics_from_query(
    datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine, sa
):
    # interacting with the database using query
    test_query: str = "SELECT * FROM table_full__I;"

    data_connector_name: str = "test_runtime_data_connector"
    data_asset_name: str = "test_asset_1"

    batch_request: dict = {
        "datasource_name": datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.name,
        "data_connector_name": data_connector_name,
        "data_asset_name": data_asset_name,
        "runtime_parameters": {
            "query": test_query,
        },
        "batch_identifiers": {
            "airflow_run_id": 1234567890,
        },
    }
    batch_request: RuntimeBatchRequest = RuntimeBatchRequest(**batch_request)

    assert (
        len(
            datasource_with_runtime_data_connector_and_sqlalchemy_execution_engine.get_available_batch_definitions(
                batch_request=batch_request
            )
        )
        == 1
    )
