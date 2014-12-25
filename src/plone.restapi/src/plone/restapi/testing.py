from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class PlonerestapiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.restapi
        xmlconfig.file(
            'configure.zcml',
            plone.restapi,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.restapi:default')

PLONE_RESTAPI_FIXTURE = PlonerestapiLayer()
PLONE_RESTAPI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_RESTAPI_FIXTURE,),
    name="PlonerestapiLayer:Integration"
)
PLONE_RESTAPI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_RESTAPI_FIXTURE, z2.ZSERVER_FIXTURE),
    name="PlonerestapiLayer:Functional"
)