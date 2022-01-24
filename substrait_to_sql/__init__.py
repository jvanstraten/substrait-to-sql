"""
Substrait to SQL converter.

Simple logic to turn (a small subset of) Substrait plans into equivalent
SQL queries.
"""

__version__ = "0.1.0"

import json

from google.protobuf import json_format

from substrait_to_sql.substrait.plan_pb2 import Plan


def _check_plan(plan: Plan) -> None:
    if not plan.IsInitialized():
        raise ValueError("plan is missing required fields")
    if len(plan.relations) < 1:
        raise ValueError("plan must contain a relation")
    if len(plan.relations) > 1:
        raise NotImplementedError("only one root relation is supported")
    plan_rel = plan.relations[0]
    if not plan_rel.HasField("root"):
        raise NotImplementedError("toplevel relation in plan must be a root relation")
    root = plan_rel.root
    if not root.HasField("input"):
        raise NotImplementedError("root relation is incomplete")


def plan_from_json(data: str) -> Plan:
    """Load a Substrait plan from its JSON string representation."""
    plan = json_format.Parse(data, Plan())
    _check_plan(plan)
    return plan


def plan_from_dict(data: dict) -> Plan:
    """Load a Substrait plan from its Python object JSON representation."""
    return plan_from_json(json.dumps(data))
