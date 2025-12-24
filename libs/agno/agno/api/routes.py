from dataclasses import dataclass


from dataclasses import dataclass

@dataclass
class ApiRoutes:
    """API routes disabled in agno-dinesh offline fork."""

    # Disabled telemetry routes
    RUN_CREATE: str = ""
    EVAL_RUN_CREATE: str = ""
    AGENT_OS_LAUNCH: str = ""















# @dataclass
# class ApiRoutes:
#     """API routes for telemetry recordings"""

#     # Runs
#     RUN_CREATE: str = "/telemetry/runs"
#     EVAL_RUN_CREATE: str = "/telemetry/evals"

#     # OS launch
#     AGENT_OS_LAUNCH: str = "/telemetry/os"
