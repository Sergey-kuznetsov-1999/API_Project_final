import pytest

def test_check_authorize(get_check_authorize_endpoint, auth_token):

    result = get_check_authorize_endpoint.check_authorize(auth_token)

    assert result  == 200, f"Expected status 200, received {result}"


def test_check_authorize_invalid(get_check_authorize_endpoint):
    result = get_check_authorize_endpoint.check_authorize("invalid_token")

    assert result  == 404, f"Expected status 404, received {result}"

def test_check_authorize_non_token(get_check_authorize_endpoint):
    result = get_check_authorize_endpoint.check_authorize('')

    assert result  == 404, f"Expected status 404, received {result}"


def test_get_check_meme(auth_token, get_check_meme_endpoint):

    result = get_check_meme_endpoint.check_meme(auth_token)
    print(result)


def test_get_check_meme_id_correct(auth_token, created_id, get_check_meme_id_endpoint):

    result = get_check_meme_id_endpoint.check_meme_id_correct(auth_token, created_id)
    print(result)


def test_get_check_meme_id_incorrect(auth_token, get_check_meme_id_endpoint):

    result = get_check_meme_id_endpoint.check_meme_id_incorrect(auth_token)

    assert result == 404, f"Expected status 404, received {result}"


def test_post_create_meme_valid(auth_token, post_create_meme_endpoint):

    result = post_create_meme_endpoint.create_meme_valid(auth_token)
    print(result)

@pytest.mark.parametrize("test_data, name_field", [
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
])
def test_post_create_meme_without_fields(auth_token, post_create_meme_endpoint, test_data, name_field):

    post_create_meme_endpoint.create_meme_valid(auth_token, test_data)
    status_code = post_create_meme_endpoint.status_code
    assert status_code == 400


def test_put_update_meme_valid(auth_token, put_update_meme_endpoint, created_id):
    result = put_update_meme_endpoint.put_update_meme_valid(auth_token, created_id)
    print(result)


def test_put_update_meme_not_found(auth_token, put_update_meme_endpoint):

    result = put_update_meme_endpoint.put_update_meme_not_found(auth_token)

    assert result == 404, f"Expected status 404, received {result}"


def test_put_update_meme_method_not_allowed(auth_token, put_update_meme_endpoint):

    result = put_update_meme_endpoint.put_update_meme_invalid(auth_token)

    assert result == 405, f"Expected status 405, received {result}"


def test_post_create_meme_id(auth_token, post_create_meme_endpoint):

    result = post_create_meme_endpoint.create_meme_id(auth_token)
    assert result > 0
    print(f'Id is created - {result}')


def test_delete_meme_valid(auth_token, delete_meme_endpoint, created_id):

    result = delete_meme_endpoint.delete_meme_valid(auth_token, created_id)
    assert result == 200, f"Expected status 200, received {result}"



def test_delete_meme_invalid(auth_token, delete_meme_endpoint):

    result = delete_meme_endpoint.delete_meme_invalid(auth_token)
    assert result == 404, f"Expected status 404, received {result}"
