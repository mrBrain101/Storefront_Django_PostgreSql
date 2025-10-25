from django.dispatch import receiver
from apps.store.signals import order_created

@receiver(order_created)
def on_order_created(sender, **kwargs) -> None:
    print(kwargs['order'])