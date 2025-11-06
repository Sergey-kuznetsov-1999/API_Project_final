import pytest
from endpoints.get_check_meme_id import CheckMemeId


def test_check_authorize(get_check_authorize_endpoint, auth_token):
    status_code = get_check_authorize_endpoint.check_authorize(auth_token)
    get_check_authorize_endpoint.check_status_code_endpoint(status_code, 200)



def test_check_authorize_invalid(get_check_authorize_endpoint):
    status_code = get_check_authorize_endpoint.check_authorize("invalid_token")
    get_check_authorize_endpoint.check_status_code_endpoint(status_code, 404)


def test_check_authorize_non_token(get_check_authorize_endpoint):
    status_code = get_check_authorize_endpoint.check_authorize('')
    get_check_authorize_endpoint.check_status_code_endpoint(status_code, 404)



def test_get_check_meme(auth_token, get_check_meme_endpoint):
    status_code = get_check_meme_endpoint.check_meme(auth_token)
    get_check_meme_endpoint.check_status_code_endpoint(status_code, 200)





def test_get_check_meme_id_correct(auth_token, created_id, get_check_meme_id_endpoint):
    status_code = get_check_meme_id_endpoint.check_meme_id(auth_token, created_id)
    get_check_meme_id_endpoint.check_status_code_endpoint(status_code, 200)


def test_get_check_meme_id_incorrect(auth_token, created_id, get_check_meme_id_endpoint):
    status_code = get_check_meme_id_endpoint.check_meme_id(auth_token, 0)
    get_check_meme_id_endpoint.check_status_code_endpoint(status_code, 404)



def test_post_create_meme_valid(auth_token, post_create_meme_endpoint):
    result = post_create_meme_endpoint.create_meme_valid(auth_token)
    assert 'id' in result and result["id"] > 0
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
    status_code = post_create_meme_endpoint.create_meme_valid(auth_token, test_data)
    post_create_meme_endpoint.check_status_code_endpoint(status_code, 400)


def test_put_update_meme_valid(auth_token, put_update_meme_endpoint, created_id):
    update_data = {
        "id": created_id,
        "text": "Update meme",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
        "tags": ["wow", "monkey"],
        "info": {"author": "it's me", "color": "black"}
    }

    result = put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    assert result.status_code == 200
    assert update_data['id'] == created_id



def test_put_update_meme_not_found(auth_token, put_update_meme_endpoint, created_id):

    update_data = {
        "id": 0,
        "text": "Update meme",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
        "tags": ["wow", "monkey"],
        "info": {"author": "it's me", "color": "black"}
    }

    result = put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    assert result.status_code == 400


def test_put_update_meme_method_without_field(auth_token, put_update_meme_endpoint, created_id):

    update_data = {
        "text": "Update meme",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
        "tags": ["wow", "monkey"],
        "info": {"author": "it's me", "color": "black"}
    }

    result = put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    assert result.status_code == 400



def test_post_create_meme_id(created_id):
    assert created_id > 0
    print(f'Id is created - {created_id}')



def test_delete_meme_valid(auth_token, delete_meme_endpoint, created_id):

    check = CheckMemeId()

    meme_data = check.check_meme_id(auth_token, created_id)
    assert meme_data is not None
    status_code = delete_meme_endpoint.delete_meme(auth_token, created_id)
    delete_meme_endpoint.check_status_code_endpoint(status_code, 200)




def test_delete_meme_invalid(auth_token, delete_meme_endpoint):
    status_code = delete_meme_endpoint.delete_meme(auth_token)
    delete_meme_endpoint.check_status_code_endpoint(status_code, 404)
