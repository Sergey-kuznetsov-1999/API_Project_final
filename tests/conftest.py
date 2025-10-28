import pytest

from endpoints.delete_meme import DeleteMeme
from endpoints.get_check_authorize import CheckAuthorize
from endpoints.get_check_meme import CheckMeme
from endpoints.get_check_meme_id import CheckMemeId
from endpoints.post_create_meme import PostCreateMeme
from endpoints.put_update_meme import PutUpdateMeme


@pytest.fixture()
def get_check_authorize_endpoint():
    return CheckAuthorize()


@pytest.fixture()
def get_check_meme_endpoint():
    return CheckMeme()


@pytest.fixture()
def get_check_meme_id_endpoint():
    return CheckMemeId()


@pytest.fixture()
def post_create_meme_endpoint():
    return PostCreateMeme()


@pytest.fixture()
def put_update_meme_endpoint():
    return PutUpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
