from context_menu import menus

def install():    
    cm = menus.ContextMenu('DTM Converter', type='FILES')
    cm.add_items([
        menus.ContextCommand('Datapack to Mod', command="dtm ?", command_vars=["FILENAME"]),
        menus.ContextCommand('Datapack to CCPacks', command="dtc ?", command_vars=["FILENAME"]),
        menus.ContextCommand('Datapack to Origins', command="dto ?", command_vars=["FILENAME"]),
        menus.ContextCommand('Datapack to Both', command="dtb ?", command_vars=["FILENAME"])
    ])
    cm.compile()

def uninstall():
    menus.removeMenu('DTM Converter', type='FILES')
