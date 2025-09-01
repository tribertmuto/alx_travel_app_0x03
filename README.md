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

## Features

- **Background Task Management**: Uses Celery with RabbitMQ for asynchronous task processing.
- **Email Notifications**: Sends booking confirmation emails asynchronously upon booking creation.

## API Endpoints

- POST /api/bookings/ - Create a new booking (triggers email notification asynchronously)

## Email Task Details

The `send_booking_confirmation_email` task in `listings/tasks.py`:
- Retrieves booking details from the database
- Sends a personalized email with booking information
- Includes error handling for missing bookings

## Testing

To test the background task:
1. Ensure RabbitMQ is running and Celery worker is started
2. Create a booking via the API (POST /api/bookings/)
3. Check Celery worker logs for task execution
4. Verify that the confirmation email is sent to the provided email address

