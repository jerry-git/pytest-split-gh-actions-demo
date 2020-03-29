# Pytest-split + GitHub actions demo

[![build](https://github.com/jerry-git/pytest-split-gh-actions-demo/workflows/Run%20tests/badge.svg)](https://github.com/jerry-git/pytest-split-gh-actions-demo/actions?query=branch%3Amaster)
[![codecov](https://codecov.io/gh/jerry-git/pytest-split-gh-actions-demo/branch/master/graph/badge.svg)](https://codecov.io/gh/jerry-git/pytest-split-gh-actions-demo)

This demo repository highlights the power of [`pytest-split`](https://github.com/jerry-git/pytest-split) when it's combined with [GitHub Actions](https://github.com/features/actions) with parallelism in mind. 
`pytest-split` makes it possible to split Python (pytest) test suite to multiple "sub suites". The splitting logic takes into account execution time of each individual test which makes it possible to split the tests in close to optimal manner considering the total execution time.
When `pytest-split` is combined with parallel execution features of GitHub Actions (or any other CI which has parallelization support), the benefits can be significant vs running all tests sequentially. 

## The example project
* [my_project/some_functionality](./my_project/some_functionality.py) contains 10 dummy functions. First 6 execute in around 10 seconds each while last 4 take around 60 seconds to execute each.  
* [tests](./tests/test_my_project.py) contain 10 tests: one for each dummy function.
* If we execute the tests sequentially, the total execution time is around 5 minutes (6 * 10 seconds + 4 * 60 seconds).
* By using parallel execution via [matrix strategy](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategymatrix) and `pytest-split` splitting feature, we can get significant boost to total execution time of CI.
* This example is using parallelization level 5 which basically means that the whole test suite is split to 5 sub suites. When the split is done optimally, one sub suite contains 6 fast tests (around 10 seconds per test) and the other 4 sub suites contain one test which each take around 60 seconds to execute. Meaning that all tests finish in around 1 minute.
* Additionally, the example collects coverage from each "sub suite" run, combines the coverage information after all "sub suites" are run, and finally, fails the build if coverage is below 100%.
* [The workflow configuration is here.](./.github/workflows/test.yml)


While writing this, the [usage limits](https://help.github.com/en/actions/getting-started-with-github-actions/about-github-actions#usage-limits) of GitHub actions are quite generous:
e.g. free GitHub plan lets you run 20 concurrent jobs simultaneously.
