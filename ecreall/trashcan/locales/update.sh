domain='ecreall.trashcan'

# Synchronise the templates and scripts with the .pot file for ecreall.trashcan domain.
i18ndude rebuild-pot --pot ./$domain.pot --create $domain ../

# Synchronise the ecreall.trashcan's pot file (Used for the workflows)
i18ndude sync --pot ./$domain.pot ./*/LC_MESSAGES/$domain.po

# Synchronise the templates and scripts with the .pot file for plone domain.
i18ndude rebuild-pot --pot ./plone.pot --merge ./plone-manual.pot --create plone ../

# Synchronise the plone's pot file (Used for the workflows)
i18ndude sync --pot ./plone.pot ./*/LC_MESSAGES/plone.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or"
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir"

rm ./rebuild_i18n.log

touch ./rebuild_i18n.log

find ../ -name "*pt" | xargs i18ndude find-untranslated > ./rebuild_i18n.log