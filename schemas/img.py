def ImgEntity(item) -> dict:
    return {
        "id": item["id"],
        "file": {
            "id": item["id"],
            "name": item["name"]
        },
        "pictures": [
            {
                "metadata": item['[:],[:],[:]'],
                "descrip": item["des"]
            }
        ]
    }