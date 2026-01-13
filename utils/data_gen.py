from faker import Faker

fake = Faker()

class DataGenerator:
    @staticmethod
    def generate_user_data():
        return{
            "name": fake.name(),
            "email": fake.email(),
            "gender": fake.random_element(elements=("male", "female")),
            "status": "active"
        }