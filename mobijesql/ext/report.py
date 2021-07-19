import datetime as dt
import glob
import sys
from dataclasses import dataclass
from typing import Any
from xml.etree import ElementTree


@dataclass
class TestResult:
    success: int = 0
    failure: int = 0
    errors: int = 0
    skipped: int = 0


@dataclass
class FailTest:
    name: str
    type: str
    message: str
    traceback: str
    occurred_at: dt.datetime


@dataclass
class ErrorTest:
    name: str
    type: str
    message: str
    traceback: str
    occurred_at: dt.datetime


class JUnitXMLReportParser:
    def __init__(self, xml: str):
        self.root = ElementTree.parse(xml).getroot()
        self.suites = list(self.root.iter('testsuite'))

    def errors(self) -> list[ErrorTest]:
        r = []

        for suite in self.suites:
            if (start_time := suite.get('timestamp')) is None:
                start_time = dt.datetime.now()
            else:
                start_time = dt.datetime.fromisoformat(start_time)

            for case in suite.iter('testcase'):
                if (error := case.find('error')) is None:
                    continue

                occurred_at = start_time + dt.timedelta(
                    seconds=int(float(case.get('time')))
                )

                r.append(
                    ErrorTest(
                        name=case.get('name'),
                        type=error.get('type'),
                        message=error.get('message'),
                        traceback=error.text,
                        occurred_at=occurred_at
                    )
                )

        return r

    def failures(self) -> list[FailTest]:
        r = []

        for suite in self.suites:
            if (start_time := suite.get('timestamp')) is None:
                start_time = dt.datetime.now()
            else:
                start_time = dt.datetime.fromisoformat(start_time)

            for case in suite.iter('testcase'):
                if (failure := case.find('failure')) is None:
                    continue

                occurred_at = start_time + dt.timedelta(
                    seconds=int(float(case.get('time')))
                )

                r.append(
                    FailTest(
                        name=case.get('name'),
                        type=failure.get('type'),
                        message=failure.get('message'),
                        traceback=failure.text,
                        occurred_at=occurred_at
                    )
                )

        return r
                

    def result(self) -> TestResult:
        failure = int(self.root.get('failures') or 0)
        errors = int(self.root.get('errors') or 0)
        skipped = int(self.root.get('skipped') or 0)
        success = int(self.root.get('tests')) - failure - skipped

        return TestResult(
            success=success,
            failure=failure,
            errors=errors,
            skipped=skipped
        )


class JenkinsTestReportParser:
    def __init__(self, report: dict[str, Any]):
        self.report = report

    def count(self):
        return {
            'success': self.report['passCount'],
            'fail': self.report['failCount'],
            'skip': self.report['skipCount']
        }    


if __name__ == '__main__':
    import datetime as dt
    import glob

    files = glob.glob('./*.xml')
    for file in files:
        parser = JUnitXMLReportParser(file)
        errors = parser.errors()
        failures = parser.failures()

        print(file)
        print(f'= = = Errors {len(errors)} = = =')
        print(f'= = = Failures {len(failures)} = = =')
        print(parser.result())
        print()
