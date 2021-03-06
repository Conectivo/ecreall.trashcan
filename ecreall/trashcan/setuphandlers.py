import logging
from Products.CMFCore.utils import getToolByName
from ecreall.trashcan import HAS_BOOLEANINDEX

# The profile id of your package:
PROFILE_ID = 'profile-ecreall.trashcan:default'

def add_catalog_indexes(context, logger=None):
    """Method to add our wanted indexes to the portal_catalog.

    @parameters:

    When called from the import_various method below, 'context' is
    the plone site and 'logger' is the portal_setup logger.  But
    this method can also be used as upgrade step, in which case
    'context' will be portal_setup and 'logger' will be None.
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('ecreall.trashcan')

    # Run the catalog.xml step as that may have defined new metadata
    # columns.  We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.
    # Remove these lines when you have no catalog.xml file.
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    if HAS_BOOLEANINDEX:
        wanted = (('trashed', 'FieldIndex'),)
    else:
        wanted = (('trashed', 'BooleanIndex'),)

    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def import_various(context):
    """Import step for configuration that is not handled in xml files.
    """
    # Only run step if a flag file is present
    marker = context.readDataFile('trashcan.txt')
    if marker is None:
        return
    logger = context.getLogger('ecreall.trashcan')
    site = context.getSite()
    add_catalog_indexes(site, logger)
from Products.CMFCore.utils import getToolByName


def upgrade_index(context):
    if not HAS_BOOLEANINDEX:
        return
    else:
        catalog = getToolByName(context, 'portal_catalog')
        if catalog.Indexes['trashed'].__class__.__name__ == 'FieldIndex':
            catalog.delIndex('trashed')
        if 'trashed' not in catalog.indexes():
            catalog.addIndex('trashed', 'BooleanIndex')
            catalog.reindexIndex('trashed', context.REQUEST)

def v4(context):
    context.runAllImportStepsFromProfile('profile-ecreall.trashcan:v4', purge_old=0)