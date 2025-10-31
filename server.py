import os
import sys
import logging

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      os.getenv('DJANGO_SETTINGS_MODULE', 
                                'storefront.settings.dev'))

# Import Django WSGI application
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    logger.info("Django WSGI application loaded successfully")
except Exception as e:
    logger.error(f"Failed to load Django application: {e}")
    raise

if __name__ == '__main__':
    from waitress import serve
    
    # Configuration
    host = os.getenv('WAITRESS_HOST', '0.0.0.0')
    port = int(os.getenv('WAITRESS_PORT', 8000))
    threads = int(os.getenv('WAITRESS_THREADS', 6))
    
    logger.info("=" * 60)
    logger.info("Starting Waitress WSGI Server")
    logger.info(f"Host: {host}")
    logger.info(f"Port: {port}")
    logger.info(f"Threads: {threads}")
    logger.info(f"Django Settings: {os.getenv('DJANGO_SETTINGS_MODULE')}")
    logger.info("=" * 60)
    
    try:
        serve(
            application,
            host=host,
            port=port,
            threads=threads,
            channel_timeout=120,
            cleanup_interval=30,
            connection_limit=1000,
            backlog=2048,
            recv_bytes=65536,
            send_bytes=65536,
            url_scheme='http',
            ident='Waitress-Django-Storefront',
            expose_tracebacks=False,
            ipv6=False
        )
    except KeyboardInterrupt:
        logger.info("Shutting down Waitress server...")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise