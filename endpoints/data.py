default_put_meme_data = {
    "text": "Update meme",
    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
    "tags": ["wow", "monkey"],
    "info": {"author": "it's me", "color": "black"}
}

get_incorrect_memes_date = [
    (
        {
            "url": "https://example.com/meme.jpg",
            "tags": ["cool", "happy"],
            "info": {"author": "noname", "color": "gray"}
        },
        "text"
    ),
    (
        {
            "text": "new meme",
            "tags": ["cool", "happy"],
            "info": {"author": "noname", "color": "gray"}
        },
        "url"
    ),
    (
        {
            "text": "new meme",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
            "info": {"author": "noname", "color": "gray"}
        },
        "tags"
    ),
    (
        {
            "text": "new meme",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
            "tags": ["cool", "happy"]
        },
        "info"
    )
]
