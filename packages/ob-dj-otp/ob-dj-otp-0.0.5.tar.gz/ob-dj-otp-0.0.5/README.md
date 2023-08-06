## OBytes Django OTP App

OTP is a Django app to conduct Web-based one true pairing, for authentication, registration and changing phone number.

## Quick start

1. Add "ob_dj_otp" to your INSTALLED_APPS setting like this::

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


2. Include the polls URLconf in your project urls.py like this::

```python
    path("otp/", include("ob_dj_otp.apis.otp.urls")),
```

3. Run ``python manage.py migrate`` to create the otp models.

