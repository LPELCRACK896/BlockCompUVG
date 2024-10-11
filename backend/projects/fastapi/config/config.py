from components.utils.Config import Config


mongo_db = Config(
    path="./components/env/mongo.env",
    required_fields=[
        "MONGODB_URI",

    ]
)
mongo_db.setup()

block_chain_network = Config(
    path="./components/env/blockchain.env",
    required_fields=[
        "URL"
    ]
)
block_chain_network.setup()

jwt_config = Config(

    path="./components/env/jwt.env",
    required_fields=[
        "SECRET",
        "ALGORITHM"
    ]
)
jwt_config.setup()
block_chain_network.setup()
