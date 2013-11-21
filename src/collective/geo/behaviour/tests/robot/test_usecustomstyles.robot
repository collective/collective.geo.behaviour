*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5  run_on_failure=Capture Page Screenshot

Resource  keywords.robot

Variables  plone/app/testing/interfaces.py
Variables  collective/geo/behaviour/tests/variables.py

Suite Setup  Suite Setup
Suite Teardown  Suite Teardown

*** Variables ***

${PORT} =  55001
${ZOPE_URL} =  http://localhost:${PORT}
${PLONE_URL} =  ${ZOPE_URL}/plone
${BROWSER} =  Firefox

${front-page}  http://localhost:55001/plone/
${test-folder}  http://localhost:55001/plone/acceptance-test-folder


*** Test Cases ***

Test using custom styles tab
    Log in as site owner
    Go to  ${test-folder}
    Create dexterity test content with geo behaviour  Test-content-with-behaviour
    Go to Custom map styles tab
    Select Checkbox  id=form-widgets-ICoordinates-use_custom_styles-0
    Click Button  Save
    Page Should Contain  Changes saved
    Go to Custom map styles tab
    Checkbox Should Be Selected  id=form-widgets-ICoordinates-use_custom_styles-0
