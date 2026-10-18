import os


def _required_env(name):
	value = os.environ.get(name)
	if not value:
		raise RuntimeError(f"Required environment variable {name} is not set.")
	return value


DB_HOST='localhost'
DB_PORT=3306
DB_USER = _required_env("DB_USER")
DB_PASSWORD = _required_env("DB_PASSWORD")
DB_NAME='vehicle_maintenance_db'
