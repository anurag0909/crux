from selenium import webdriver
from Data import variables
from Data import genericFunctions
from functionSteps import Crux
import pytest


@pytest.yield_fixture()
def Case1():
    print("**Starting the execution**")
    yield
    print("Executed Properly....")


@pytest.mark.skipif(genericFunctions.getFlagValue("TC_001") == 'N', reason="Flag value is N, so skipped the test case")
def testCase01(Case1):
    Crux.basicCase()


@pytest.yield_fixture()
def Case2():
    print("Starting with another case....")
    yield
    print("App store links working properly...")


@pytest.mark.skipif(genericFunctions.getFlagValue("TC_002") == 'N', reason="Flag value is N, so skipped the test case")
def testCase02(Case2):
    Crux.check_aboutUs()


@pytest.yield_fixture()
def Case3():
    print("Schedule demo...")
    if len(variables.driver.window_handles) > 1 and (variables.driver.current_window_handle != 1):
        print("Move to main window for home page of the application...")
        variables.driver.switch_to.window(window_name=variables.driver.window_handles[0])
    else:
        print("application in correct tab")
    yield
    print("Demo scheduled successfully..")


@pytest.mark.skipif(genericFunctions.getFlagValue("TC_003") == 'N', reason="Flag value is N, so skipped the test case")
def testCase03(Case3):
    Crux.scheduleDemo()