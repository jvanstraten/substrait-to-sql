import google.protobuf.json_format
import pytest

import substrait_to_sql as sts


def test_version():
    assert sts.__version__ == "0.1.0"


def test_broken_json():
    with pytest.raises(google.protobuf.json_format.ParseError):
        sts.plan_from_json("not json")


def test_empty_plan():
    with pytest.raises(ValueError):
        sts.plan_from_dict({})


def test_h01():
    read = {
        "read": {
            "common": {"direct": {}},
            "base_schema": {
                "names": [
                    # TODO
                ],
                "struct": {
                    "types": [
                        # TODO
                    ],
                    "type_variation_reference": 1,
                    "nullability": "NULLABILITY_NULLABLE",
                },
            },
        }
    }

    group = {
        "aggregate": {
            "common": {"direct": {}},
            "groupings": [
                # TODO
            ],
            "measures": [
                # TODO
            ],
            "input": read,
        }
    }

    sort = {
        "sort": {
            "common": {"direct": {}},
            "sorts": [
                {
                    "expr": {
                        "selection": {
                            "direct_reference": {"struct_field": {"field": 0}}
                        }
                    },
                    "direction": "SORT_DIRECTION_ASC_NULLS_FIRST",
                },
                {
                    "expr": {
                        "selection": {
                            "direct_reference": {"struct_field": {"field": 1}}
                        }
                    },
                    "direction": "SORT_DIRECTION_ASC_NULLS_FIRST",
                },
            ],
            "input": group,
        }
    }

    sts.plan_from_dict(
        {
            "relations": [
                {
                    "root": {
                        "names": [
                            "l_returnflag",
                            "l_linestatus",
                            "sum_qty",
                            "sum_base_price",
                            "sum_disc_price",
                            "sum_charge",
                            "avg_qty",
                            "avg_price",
                            "avg_disc",
                            "count_order",
                        ],
                        "input": sort,
                    }
                }
            ]
        }
    )
