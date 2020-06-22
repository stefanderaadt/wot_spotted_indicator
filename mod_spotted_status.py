"""
Main entry point for mods.
World of Tanks will load any module from a wotmod package, as long as:
 - module is in res/scripts/client/gui/mods,
 - module's name starts with 'mod_', and
 - module has extension 'pyc'.

Once loaded, the game will call several functions from the module if they are
defined, most notably init() and fini().
"""

from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap import plugins
from constants import IS_DEVELOPMENT


class CustomArenaVehiclesPlugin(plugins.ArenaVehiclesPlugin):
    def __init__(self, parent):
        super(CustomArenaVehiclesPlugin, self).__init__(parent)

    def start(self):
        super(CustomArenaVehiclesPlugin, self).start()
        ctrl = super(CustomArenaVehiclesPlugin,
                     self).sessionProvider.shared.feedback

        if ctrl is not None:
            ctrl.onMinimapVehicleAdded += self.__onMinimapVehicleAdded
            ctrl.onMinimapVehicleRemoved += self.__onMinimapVehicleRemoved

    def stop(self):
        super(CustomArenaVehiclesPlugin, self).stop()
        ctrl = super(CustomArenaVehiclesPlugin,
                     self).sessionProvider.shared.feedback

        if ctrl is not None:
            ctrl.onMinimapVehicleAdded -= self.__onMinimapVehicleAdded
            ctrl.onMinimapVehicleRemoved -= self.__onMinimapVehicleRemoved

    def __onMinimapVehicleAdded(self, vProxy, vInfo, guiProps):
        vehicleID = vInfo.vehicleID
        entry = super(CustomArenaVehiclesPlugin, self)._entries[vehicleID]

        print 'Vehicle added. Entry: %s' % str(entry)

    def __onMinimapVehicleRemoved(self, vehicleID):
        entry = super(CustomArenaVehiclesPlugin, self)._entries[vehicleID]

        print 'Vehicle removed. Entry: %s' % str(entry)


def _setupPlugins(self, arenaVisitor):
    setup = parent__setupPlugins(self, arenaVisitor)
    setup['teleport'] = CustomArenaVehiclesPlugin

    print dir(arenaVisitor)

    return setup


parent__setupPlugins = MinimapComponent._setupPlugins
MinimapComponent._setupPlugins = _setupPlugins


# from gui.Scaleform.daapi.view.battle.classic import players_panel
# from gui.shared import event_bus, EVENT_BUS_SCOPE


# def test(self, vehicleID):
#     parent(self, vehicleID)

#     print 'switch to player %s' % str(vehicleID)


# parent = players_panel.PlayersPanel.switchToOtherPlayer
# players_panel.PlayersPanel.switchToOtherPlayer = test


# def handleEvent(self, event, scope=EVENT_BUS_SCOPE.DEFAULT):
#     parent_handleEvent(self, event, scope)

#     print 'event: %s' % str(event)


# parent_handleEvent = event_bus.EventBus.handleEvent
# event_bus.EventBus.handleEvent = handleEvent


# addSettings(ViewSettings(BATTLE_VIEW_ALIASES.PLAYERS_PANEL, CustomPlayersPanel,
#                          None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))

# from helloworld import resources


# def dict_from_module(module):
#     context = {}
#     for setting in dir(module):
#         # you can write your filter here
#         if setting.islower() and setting.isalpha():
#             context[setting] = getattr(module, setting)

#     return context


# def init():
#     """
#     Mod initialization function.
#     Called by World of Tanks when the game starts up.
#     """
#     name = resources.read_file('mods/klokklokz.spotted_status/data/name.txt')
#     # Print statements end up to python.log in game's root directory
#     print 'Hello %s!' % name
#     # BigWorld.wg_openWebBrowser('https://google.com')
#     print dict_from_module(BigWorld)
#     print dir(g_playerEvents)


# def fini():
#     """
#     Mod deinitialization function.
#     Called by World of Tanks when the game shuts down.
#     """
#     name = resources.read_file('mods/klokklokz.spotted_status/data/name.txt')
#     print 'Bye bye %s!' % name
