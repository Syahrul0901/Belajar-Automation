from faker import Faker


class Testdata:
    fake = Faker(["id_ID"])

    BASE_URL = "https://www.amazon.com"
    SEARCH_FIELD_DATA = '32 inches & under'
