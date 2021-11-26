from environs import Env

env = Env()
env.read_env()


class Settings:
    AIRTABLE_BASE: str = env("AIRTABLE_BASE")
    AIRTABLE_TABLE: str = env("AIRTABLE_TABLE")
    AIRTABLE_API_KEY: str = env("AIRTABLE_API_KEY")
