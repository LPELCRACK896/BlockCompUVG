from components.utils.Config import Config


mongo_db = Config(
    path="./components/env/mongo.env",
    required_fields=[
        "MONGODB_URI",

    ]
)
mongo_db.setup()