import re
from retreat import substitute, REGEX_UPTICK, REGEX_AT, Link, Manual


def test_regex_correctness():
    assert re.findall(REGEX_UPTICK, "[JetBrain survey (2021) on testing](^sde)") == [
        "sde"
    ]
    assert re.findall(REGEX_AT, "Frameworks: @pytest @unittest") == [
        "pytest",
        "unittest",
    ]


def test_on_uptick():
    assert (
        substitute(
            text="[JetBrain survey (2021) on testing](^sde)",
            ref_dict=dict(
                sde=Link(
                    "State of Developper Ecosystem (2021). Testing.",
                    "https://www.jetbrains.com/lp/devecosystem-2021/testing/",
                )
            ),
        )
        == "[JetBrain survey (2021) on testing](https://www.jetbrains.com/lp/devecosystem-2021/testing/)"
    )


def test_on_at():
    assert substitute(
        "Unit-testing frameworks. @pytest @unittest",
        ref_dict=dict(
            pytest=Manual(
                "pytest!",
                "https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test",
            ),
            unittest=Manual(
                "unittest!", "https://docs.python.org/3/library/unittest.html"
            ),
        ),
    ) == (
        "Unit-testing frameworks. [pytest!](https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test) "
        "[unittest!](https://docs.python.org/3/library/unittest.html)"
    )
