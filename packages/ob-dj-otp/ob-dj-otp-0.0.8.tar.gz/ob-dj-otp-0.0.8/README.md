## OBytes Django OTP App

OTP is a Django app to conduct Web-based one true pairing, for authentication, registration and changing phone number.

## Quick start

1. Install `ob_dj_otp` latest version `pip install ob_dj_otp`

2. Add "ob_dj_otp" to your `INSTALLED_APPS` setting like this:

```python
   # settings.py
   INSTALLED_APPS = [
        ...
        "ob_dj_otp",
   ]
   # Setting Twilio as SMS Provider
   OTP_PROVIDER = os.environ.get("OTP_PROVIDER", "twilio")
   # Passing Twilio Verify Service-ID
   OTP_TWILIO_SERVICE = os.environ.get("OTP_PROVIDER")
```


3. Include the OTP URLs in your project urls.py like this::

```python
    path("otp/", include("ob_dj_otp.apis.otp.urls")),
```

4. Run ``python manage.py migrate`` to create the otp models.


## Developer Guide

After cloning the repo locally, install all dependencies using `pipenv install --dev`, run `pytest` to run all tests.

Developers can also use `docker-compose` to run the project locally, `docker-compose build && docker-compose run app bash`
