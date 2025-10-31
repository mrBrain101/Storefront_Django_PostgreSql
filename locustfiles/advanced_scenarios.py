# """
# Advanced Locust scenarios for comprehensive load testing.
# """
# from locust import HttpUser, TaskSet, task, between, SequentialTaskSet
# import random


# class BrowseAndPurchase(SequentialTaskSet):
#     """Sequential user journey: browse -> add to cart -> checkout."""
    
#     @task
#     def browse_products(self):
#         """Step 1: Browse products."""
#         self.client.get("/store/products/")
#         self.wait()
    
#     @task
#     def view_product(self):
#         """Step 2: View product details."""
#         product_id = random.randint(1, 50)
#         self.client.get(f"/store/products/{product_id}/")
#         self.wait()
    
#     @task
#     def add_to_cart(self):
#         """Step 3: Add product to cart."""
#         product_id = random.randint(1, 50)
#         self.client.post(
#             "/store/cart/add/",
#             json={"product_id": product_id, "quantity": 1}
#         )
#         self.wait()
    
#     @task
#     def view_cart(self):
#         """Step 4: View cart."""
#         self.client.get("/store/cart/")
#         self.wait()
    
#     @task
#     def stop(self):
#         """Complete the journey."""
#         self.interrupt()


# class PowerUser(HttpUser):
#     """Simulates power users with complex behavior."""
    
#     tasks = [BrowseAndPurchase]
#     wait_time = between(2, 5)
#     weight = 2


# class MobileUser(HttpUser):
#     """Simulates mobile users with different patterns."""
    
#     wait_time = between(3, 8)  # Slower interactions
#     weight = 2
    
#     @task(3)
#     def quick_browse(self):
#         """Mobile users browse quickly."""
#         self.client.get("/store/products/")
    
#     @task(1)
#     def search(self):
#         """Mobile users search more."""
#         terms = ["phone", "tablet", "mobile"]
#         self.client.get(f"/store/products/?search={random.choice(terms)}")