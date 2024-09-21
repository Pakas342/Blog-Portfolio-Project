dev_cors_resources = {
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "http://127.0.0.1:5000",
            "http://localhost:8000"
            ]
    }
}

prod_cors_resources = {
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "http://127.0.0.1:5000",
            "http://localhost:8000"
            ]
    }
}
