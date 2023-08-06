# python-sparkpost-async
An asynchronous SparkPost email backend for Django; currently only supports
Dramatiq (not Celery).


## Quickstart
1. Install django-theme via pip:
   ```
   pip install sparkpost-async
   ```

1. Set the `EMAIL_BACKEND` setting in settings.py:
   ```python
   EMAIL_BACKEND = 'sparkpost_async.email_backend.AsyncSparkPostEmailBackend'
   ```

1. Make sure all other settings required by `python-sparkpost` are set.
   See the [python-sparkpost docs][1] for more info.




## Compatibility
- Compatible with Python 3.8 and above.
- Compatible with Django 3.2 and above.


## Versioning
This project follows [semantic versioning][200] (SemVer).


## License and code of conduct
Check the root of the repo for these files.








[//]: # (Links)

[1]: https://github.com/SparkPost/python-sparkpost
[200]: https://semver.org/
