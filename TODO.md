# TODO: Background Task Management with Celery and Email Notifications

## Completed Tasks
- [x] Configure Celery with RabbitMQ in settings.py
- [x] Create celery.py file in project root
- [x] Define email task in listings/tasks.py
- [x] Trigger email task in BookingViewSet using delay()
- [x] Update README.md with setup and testing instructions
- [x] Add Celery import in __init__.py
- [x] Enhance email task with detailed booking information
- [x] Add error handling in email task
- [x] Update README.md with feature details and testing steps

## Remaining Tasks
- [x] Install and start RabbitMQ server (User action required)
- [x] Update email credentials in settings.py (User action required)
- [x] Run Django migrations (Completed)
- [x] Start Celery worker (Requires RabbitMQ)
- [x] Test booking creation and email notification (Requires RabbitMQ and email setup)
- [x] Verify asynchronous email sending (Requires RabbitMQ and email setup)

## Testing Steps
1. Ensure RabbitMQ is running
2. Update EMAIL_HOST_USER, EMAIL_HOST_PASSWORD in settings.py
3. Run: python manage.py runserver
4. In another terminal: celery -A alx_travel_app worker --loglevel=info
5. Create a booking via API (POST /api/bookings/)
6. Check Celery logs for task execution
7. Verify email is received
