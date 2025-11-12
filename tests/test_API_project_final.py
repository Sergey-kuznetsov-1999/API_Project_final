import pytest
from endpoints.get_check_meme_id import CheckMemeId
from tests.conftest import put_update_meme_endpoint
from endpoints.data import default_put_meme_data, get_incorrect_memes_date


def test_check_authorize(get_check_authorize_endpoint, auth_token):
    get_check_authorize_endpoint.check_authorize(auth_token)
    get_check_authorize_endpoint.check_status_code_endpoint(200)


def test_check_authorize_invalid(get_check_authorize_endpoint):
    get_check_authorize_endpoint.check_authorize("invalid_token")
    get_check_authorize_endpoint.check_status_code_endpoint(404)


def test_check_authorize_non_token(get_check_authorize_endpoint):
    get_check_authorize_endpoint.check_authorize('')
    get_check_authorize_endpoint.check_status_code_endpoint(404)


def test_get_check_meme(auth_token, get_check_meme_endpoint):
    get_check_meme_endpoint.check_meme(auth_token)
    get_check_meme_endpoint.check_status_code_endpoint(200)
    get_check_meme_endpoint.check_response_not_empty()


def test_get_check_meme_id_correct(auth_token, created_id, get_check_meme_id_endpoint):
    get_check_meme_id_endpoint.check_meme_id(auth_token, created_id)
    get_check_meme_id_endpoint.check_status_code_endpoint(200)
    get_check_meme_id_endpoint.check_id_is_correct(created_id)


def test_get_check_meme_id_incorrect(auth_token, created_id, get_check_meme_id_endpoint):
    get_check_meme_id_endpoint.check_meme_id(auth_token, 0)
    get_check_meme_id_endpoint.check_status_code_endpoint(404)


def test_post_create_meme_valid(auth_token, post_create_meme_endpoint):
    data = post_create_meme_endpoint.default_meme_data()
    post_create_meme_endpoint.create_meme_valid(auth_token)
    post_create_meme_endpoint.check_status_code_endpoint(200)
    post_create_meme_endpoint.check_meme_same_created(data)


@pytest.mark.parametrize("test_data, name_field", get_incorrect_memes_date)
def test_post_create_meme_without_fields(auth_token, post_create_meme_endpoint, test_data, name_field):
    post_create_meme_endpoint.create_meme_valid(auth_token, test_data)
    post_create_meme_endpoint.check_status_code_endpoint(400)


def test_put_update_meme_valid(auth_token, put_update_meme_endpoint, created_id):
    update_data = default_put_meme_data.copy()
    update_data["id"] = created_id
    put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    put_update_meme_endpoint.check_status_code_endpoint(200)
    put_update_meme_endpoint.check_id_is_correct(created_id)
    put_update_meme_endpoint.check_meme_same_created(update_data)


def test_put_update_meme_not_found(auth_token, put_update_meme_endpoint, created_id):
    update_data = default_put_meme_data.copy()
    update_data["id"] = 0
    put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    put_update_meme_endpoint.check_status_code_endpoint(400)


def test_put_update_meme_method_without_field(auth_token, put_update_meme_endpoint, created_id):
    update_data = default_put_meme_data.copy()
    update_data["id"] = None
    put_update_meme_endpoint.put_update_meme(auth_token, created_id, update_data)
    put_update_meme_endpoint.check_status_code_endpoint(400)


def test_delete_meme_valid(auth_token, delete_meme_endpoint, created_id, get_check_meme_id_endpoint):
    delete_meme_endpoint.delete_meme(auth_token, created_id)
    delete_meme_endpoint.check_status_code_endpoint(200)
    get_check_meme_id_endpoint.check_meme_id(auth_token, created_id)
    get_check_meme_id_endpoint.check_status_code_endpoint(404)


def test_delete_meme_invalid(auth_token, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(auth_token)
    delete_meme_endpoint.check_status_code_endpoint(404)
