from api.items import routers as item_routers


def apply_router(app):
    app.include_router(item_routers.router)
