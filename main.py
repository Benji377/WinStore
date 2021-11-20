import database_controller

database = database_controller.Database()

appl = database.get_app_by_id(1)

print(appl[0])
