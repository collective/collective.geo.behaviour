#!/bin/bash
cd "`dirname $0`/.."
PRODUCT=collective.geo.behaviour
i18ndude rebuild-pot --pot locales/${PRODUCT}.pot --create $PRODUCT  .
i18ndude sync --pot locales/${PRODUCT}.pot locales/*/LC_MESSAGES/${PRODUCT}.po
# Ok, now poedit is your friend!
    
