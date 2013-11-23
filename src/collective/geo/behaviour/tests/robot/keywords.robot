
*** Keywords ***

Suite Setup
    Open Browser  ${front-page}  browser=${BROWSER}  desired_capabilities=Capture Page Screenshot

Suite Teardown
    Close All Browsers

Log in
    [Documentation]  Log in to the site as ${userid} using ${password}. There
    ...              is no guarantee of where in the site you are once this is
    ...              done. (You are responsible for knowing where you are and
    ...              where you want to be)
    [Arguments]  ${userid}  ${password}

    Go to  ${PLONE_URL}/login_form
    Page should contain element  __ac_name
    Page should contain element  __ac_password
    Page should contain button  Log in
    Input text  __ac_name  ${userid}
    Input text  __ac_password  ${password}
    Click Button  Log in

Log in as site owner
    [Documentation]  Log in as the SITE_OWNER provided by plone.app.testing,
    ...              with all the rights and privileges of that user.
    Log in  ${SITE_OWNER_NAME}  ${SITE_OWNER_PASSWORD}

Open Menu
    [Arguments]  ${elementId}
    Element Should Not Be Visible  css=dl#${elementId} dd.actionMenuContent
    Click link  css=dl#${elementId} dt.actionMenuHeader a
    Wait until keyword succeeds  1  5  Element Should Be Visible  css=dl#${elementId} dd.actionMenuContent

Open Add New Menu
    Open Menu  plone-contentmenu-factories

Create dexterity test content with geo behaviour
    [Arguments]  ${title}
    Open Add New Menu
    Click Link  link=dexterity content with geo behavior
    Input text  name=form.widgets.IBasic.title  ${title}
    Click Button  Save
    Page Should Contain  Item created

Go to Custom map styles tab
    Click Link  link=Edit
    Click Link  link=Custom map styles

Check use custom styles field
    Go to Custom map styles tab
    Select Checkbox  id=form-widgets-ICoordinates-use_custom_styles-0
    Click Button  Save
    Page Should Contain  Changes saved
    Go to Custom map styles tab
    Checkbox Should Be Selected  id=form-widgets-ICoordinates-use_custom_styles-0

Check text field on Custom map styles tab
    [Arguments]  ${name}  ${value}
    Go to Custom map styles tab
    Input text  name=${name}  ${value}
    Click Button  Save
    Page Should Contain  Changes saved
    Go to Custom map styles tab
    Page Should Contain Textfield  name=${name}  message=${value}

Check marker image field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.marker_image  string:\${portal_url}/img/new_marker.png

Check map position field
    Go to Custom map styles tab
    Select From List By Value  name=form.widgets.ICoordinates.map_viewlet_position:list  plone.belowcontentbody
    Click Button  Save
    Page Should Contain  Changes saved
    Go to Custom map styles tab
    List Selection Should Be  name=form.widgets.ICoordinates.map_viewlet_position:list  plone.belowcontentbody

Check marker image size field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.marker_image_size  0.8

Check map width field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.map_width  450px

Check line color field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.linecolor  ff00aa77

Check map height field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.map_height  450px

Check poligon color field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.polygoncolor  0033aa22

Check ballon details field
    Go to Custom map styles tab
    Select From List By Value  name=form.widgets.ICoordinates.display_properties.from  id
    Click Button  name=from2toButton
    Click Button  Save
    Page Should Contain  Changes saved
    Go to Custom map styles tab
    Select From List By Value  name=form.widgets.ICoordinates.display_properties.to  id
    Click Button  name=to2fromButton
    Click Button  Save

Check line width field
    Check text field on Custom map styles tab  form.widgets.ICoordinates.linewidth  0.3
