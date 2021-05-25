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
    skipped: int = 0


@dataclass
class FailTest:
    name: str
    type: str
    message: str
    traceback: str
    occurred_at: dt.datetime


class JUnitXMLReportParser:
    def __init__(self, xml: str):
        self.root = ElementTree.parse(xml).getroot()

    def failures(self) -> list[FailTest]:
        r = []
        suites = self.root.iter('testsuite')
        for suite in suites:
            start_time = dt.datetime.fromisoformat(
                suite.get('timestamp')
            )

            cases = suite.iter('testcase')
            for case in cases:
                if (failure := case.find('failure')) is None:
                    continue

                occurred_at = start_time + dt.timedelta(
                    seconds=int(float(case.get('time')))
                )

                r.append(FailTest(
                    name=case.get('name'),
                    type=failure.get('type'),
                    message=failure.get('message'),
                    traceback=failure.text,
                    occurred_at=occurred_at
                ))

        return r
                

    def result(self) -> TestResult:
        failure = int(self.root.get('failures'))
        skipped = 0
        success = int(self.root.get('tests')) - failure - skipped

        return TestResult(
            success=success,
            failure=failure,
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
    parser = JUnitXMLReportParser('test-report/GALLERY_REGULAR_ENG.xml')
    testsuites = parser.root.iter('testsuite')
    for testsuite in testsuites:
        suitetime = testsuite.get('timestamp')
        suitetime = dt.datetime.fromisoformat(suitetime)
        print(suitetime)
