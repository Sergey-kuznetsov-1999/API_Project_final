def test_check_authorize(get_check_authorize_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]

    result = get_check_authorize_endpoint.check_authorize(valid_token)

    assert result is True


def test_check_authorize_invalid(get_check_authorize_endpoint):
    result = get_check_authorize_endpoint.check_authorize("invalid_token")

    assert result is False


def test_check_authorize_non_token(get_check_authorize_endpoint):
    result = get_check_authorize_endpoint.check_authorize("")

    assert result is False


def test_get_check_meme(get_check_authorize_endpoint, get_check_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = get_check_meme_endpoint.check_meme(valid_token)

    assert result is True


def test_get_check_meme_id_correct(get_check_authorize_endpoint, get_check_meme_id_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = get_check_meme_id_endpoint.check_meme_id_correct(valid_token)

    assert result is True


def test_get_check_meme_id_incorrect(get_check_authorize_endpoint, get_check_meme_id_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = get_check_meme_id_endpoint.check_meme_id_incorrect(valid_token)

    assert result is True


def test_post_create_meme_valid(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_valid(valid_token)
    print(result)


def test_post_create_meme_without_text(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_without_text_fild(valid_token)

    assert result is True


def test_post_create_meme_without_url(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_without_url_filed(valid_token)

    assert result is True


def test_post_create_meme_without_tags(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_without_tags_filed(valid_token)

    assert result is True


def test_post_create_meme_without_info(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_without_info_filed(valid_token)

    assert result is True


def test_put_update_meme_valid(get_check_authorize_endpoint, put_update_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = put_update_meme_endpoint.put_update_meme_valid(valid_token)
    print(result)


def test_put_update_meme_not_found(get_check_authorize_endpoint, put_update_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = put_update_meme_endpoint.put_update_meme_not_found(valid_token)

    assert result is True


def test_put_update_meme_invalid(get_check_authorize_endpoint, put_update_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = put_update_meme_endpoint.put_update_meme_invalid(valid_token)

    assert result is True


def test_post_create_meme_id(get_check_authorize_endpoint, post_create_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = post_create_meme_endpoint.create_meme_id(valid_token)
    print(result)


def test_delete_meme_valid(get_check_authorize_endpoint, delete_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = delete_meme_endpoint.delete_meme_valid(valid_token)
    print(result)


def test_delete_meme_invalid(get_check_authorize_endpoint, delete_meme_endpoint):
    auth_data = get_check_authorize_endpoint.authorize()
    valid_token = auth_data["token"]
    result = delete_meme_endpoint.delete_meme_invalid(valid_token)
    print(result)
