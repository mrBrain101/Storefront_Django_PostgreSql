"""
Run with: docker compose --profile loadtest up
Access UI at: http://localhost:8089
"""
from locust import HttpUser, task, between, events
from random import randint
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_products(self):
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}', 
            name='/store/products')

    @task(4)
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(f'/store/products/{product_id}/', 
                        name='/store/products/:id/')
    
    @task(1)
    def add_to_cart(self):
        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/', 
                         name='/store/carts/items',
                         json={'product_id': product_id, 'quantity': 1})
    
    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Called when load test starts."""
    logger.info("=" * 60)
    logger.info("LOAD TEST STARTING")
    logger.info(f"Target: {environment.host}")
    logger.info("=" * 60)


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Called when load test stops."""
    stats = environment.stats.total
    logger.info("=" * 60)
    logger.info("LOAD TEST COMPLETED")
    logger.info(f"Total Requests: {stats.num_requests}")
    logger.info(f"Total Failures: {stats.num_failures}")
    logger.info(f"Average Response Time: {stats.avg_response_time:.2f}ms")
    logger.info(f"Requests/sec: {stats.total_rps:.2f}")
    logger.info("=" * 60)