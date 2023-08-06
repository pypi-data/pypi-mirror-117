# TODO: <Alex>ALEX -- Uncomment later (if needed for SparkDFExecutionEngine and/or SqlAlchemyExecutionEngine) or delete.</Alex>
# import copy
# from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd

from great_expectations.execution_engine import (
    PandasExecutionEngine,
    SqlAlchemyExecutionEngine,
)

# TODO: <Alex>ALEX -- Uncomment later (if needed for SparkDFExecutionEngine and/or SqlAlchemyExecutionEngine) or delete.</Alex>
# from great_expectations.execution_engine import (
#     SparkDFExecutionEngine,
# )
# from great_expectations.execution_engine.execution_engine import (
#     MetricDomainTypes,
#     MetricPartialFunctionTypes,
# )
from great_expectations.expectations.metrics.import_manager import sa
from great_expectations.expectations.metrics.map_metric_provider import (
    ColumnPairMapMetricProvider,
    column_pair_condition_partial,
)


class ColumnPairValuesInSet(ColumnPairMapMetricProvider):
    condition_metric_name = "column_pair_values.in_set"
    condition_value_keys = ("value_pairs_set",)
    condition_domain_keys = (
        "batch_id",
        "table",
        "column_A",
        "column_B",
        "ignore_row_if",
    )

    # TODO: <Alex>ALEX -- temporarily only Pandas and SQL Alchemy implementations are provided (Spark to follow).</Alex>
    # noinspection PyPep8Naming
    @column_pair_condition_partial(engine=PandasExecutionEngine)
    def _pandas(cls, column_A, column_B, **kwargs):
        value_pairs_set = kwargs.get("value_pairs_set")

        if value_pairs_set is None:
            # vacuously true
            return np.ones(len(column_A), dtype=np.bool_)

        temp_df = pd.DataFrame({"A": column_A, "B": column_B})
        value_pairs_set = {(x, y) for x, y in value_pairs_set}

        results = []
        for i, t in temp_df.iterrows():
            if pd.isnull(t["A"]):
                a = None
            else:
                a = t["A"]

            if pd.isnull(t["B"]):
                b = None
            else:
                b = t["B"]

            results.append((a, b) in value_pairs_set)

        return pd.Series(results)

    @column_pair_condition_partial(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(cls, column_A, column_B, **kwargs):
        value_pairs_set = kwargs.get("value_pairs_set")

        if value_pairs_set is None:
            # vacuously true
            return sa.case([(column_A == column_B, True)], else_=True)

        value_pairs_set = [(x, y) for x, y in value_pairs_set]

        # or_ implementation was required due to mssql issues with in_
        cond = sa.or_()
        for x, y in value_pairs_set:
            cond = sa.or_(cond, sa.and_(column_A == x, column_B == y))

        return sa.case([(cond, True)], else_=False)

    # # TODO: <Alex>ALEX -- Note: The Spark implementation below is a temporary placeholder.</Alex>
    # @metric_partial(
    #     engine=SparkDFExecutionEngine,
    #     partial_fn_type=MetricPartialFunctionTypes.WINDOW_CONDITION_FN,
    #     domain_type=MetricDomainTypes.COLUMN_PAIR,
    # )
    # def _spark(
    #     cls,
    #     execution_engine: "SparkDFExecutionEngine",
    #     metric_domain_kwargs: Dict,
    #     metric_value_kwargs: Dict,
    #     metrics: Dict[Tuple, Any],
    #     runtime_configuration: Dict,
    # ):
    #     ignore_row_if = metric_value_kwargs["ignore_row_if"]
    #     compute_domain_kwargs = copy.deepcopy(metric_domain_kwargs)
    #
    #     if ignore_row_if == "both_values_are_missing":
    #         compute_domain_kwargs["row_condition"] = (
    #             F.col(metric_domain_kwargs["column_A"]).isNotNull()
    #             & F.col(metric_domain_kwargs["column_B"]).isNotNull()
    #         )
    #         compute_domain_kwargs["condition_parser"] = "spark"
    #     elif ignore_row_if == "either_value_is_missing":
    #         compute_domain_kwargs["row_condition"] = (
    #             F.col(metric_domain_kwargs["column_A"]).isNotNull()
    #             | F.col(metric_domain_kwargs["column_B"]).isNotNull()
    #         )
    #         compute_domain_kwargs["condition_parser"] = "spark"
    #
    #     (
    #         df,
    #         compute_domain_kwargs,
    #         accessor_domain_kwargs,
    #     ) = execution_engine.get_compute_domain(
    #         compute_domain_kwargs, domain_type=MetricDomainTypes.COLUMN_PAIR
    #     )
    #
    #     df = df.withColumn(
    #         "combined",
    #         F.array(
    #             F.col(metric_domain_kwargs["column_A"]),
    #             F.col(metric_domain_kwargs["column_A"]),
    #         ),
    #     )
    #
    #     value_set_df = (
    #         SQLContext(df._sc)
    #         .createDataFrame(metric_value_kwargs["value_pairs_set"], ["col_A", "col_B"])
    #         .select(F.array("col_A", "col_B").alias("set_AB"))
    #     )
    #
    #     df = df.join(
    #         value_set_df, df["combined"] == value_set_df["set_AB"], "left"
    #     ).withColumn(
    #         "__success",
    #         F.when(F.col("set_AB").isNull(), F.lit(False)).otherwise(F.lit(True)),
    #     )
    #     return df["__success"], compute_domain_kwargs, accessor_domain_kwargs
