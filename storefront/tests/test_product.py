from rest_framework import status
import pytest

default_product = {'title': 'a', 'slug': 'a', 'unit_price': 1,
                   'inventory': 1, 'collection': 'a'}

@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product(default_product)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_product, 
                                              authenticate):
        authenticate(is_staff=False)

        response = create_product(default_product)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_any_required_field_is_invalid_returns_400(
            self, create_product, authenticate):
        authenticate(is_staff=True)

        for field in default_product.keys():
            response = create_product(default_product)
            response[field] = ''

            assert response.status_code == status.HTTP_400_BAD_REQUEST