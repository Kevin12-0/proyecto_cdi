import os

settings = {
    "host": os.environ.get(
        "ACCOUNT_HOST", "https://kevinlopezmendoza.documents.azure.com:443/"
    ),
    "master_key": os.environ.get(
        "ACCOUNT_KEY",
        "4CX6sgiSshwHb5wDTxoCmzmdrtiV4AFrbXrNV9dD3xHSTShMH1UR3o3QlVq63UXuKsXFGk9Qn6OCACDbMaWQqg==",
    ),
    "database_id": os.environ.get("COSMOS_DATABASE", "ToDoList"),
    "container_id": os.environ.get("COSMOS_CONTAINER", "Items"),
}
