# alx_travel_app_0x03

This is a Django travel app with Celery background task management and email notifications.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up RabbitMQ (for Celery broker):
   - Install RabbitMQ from https://www.rabbitmq.com/download.html
   - Start RabbitMQ server

3. Configure email settings in `alx_travel_app/settings.py`:
   - Update `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` with your email credentials.

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start Celery worker:
   ```
   celery -A alx_travel_app worker --loglevel=info
   ```

6. Run the Django server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- POST /api/bookings/ - Create a new booking (triggers email notification asynchronously)

## Testing

To test the background task:
1. Create a booking via the API.
2. The email confirmation should be sent asynchronously via Celery.

