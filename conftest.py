import pytest

from database_controller import DataBaseController


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' or (result.when == 'setup' and result.failed):
        case_name = result.nodeid
        path = result.fspath

        if result.failed:
            stack_trace = result.longreprtext + "\n" + result.capstdout
        else:
            stack_trace = result.capstdout

        status = result.outcome
        duration = result.duration

        DataBaseController.insert_data(status)
