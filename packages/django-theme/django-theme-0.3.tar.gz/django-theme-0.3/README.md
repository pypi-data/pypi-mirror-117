# django-theme
Allow a Django user to set a theme preference.


## Quickstart
1. Install django-theme via pip:
   ```
   pip install django-theme
   ```

1. Add `theme` to your `INSTALLED_APPS` in your project settings.py file:
   ```python
   INSTALLED_APPS = [
       '...',
       'theme',
   ]
   ```

1. Run migrate:
   ```
   python manage.py migrate
   ```

1. Add the following to your `context_processors` setting:
   ```python
   TEMPLATES = [
       {
           'BACKEND': '...',
           'OPTIONS': {
               'context_processors': [
                   '...',
                   '...',
                   'theme.context_processors.theme',
               ],
           },
       },
   ]
   ```

1. In your template, you can then use the following snippet (theme options
   are 'system', 'dark' and 'light'):
   ```
   <body class="{% spaceless %}
           {% if theme == 'dark' %}
                   dark-theme
           {% endif %}
   {% endspaceless %}">
   ```

1. The `Theme` model defines a one-to-one relationship with the `User` model.
   Therefore, the theme object for a user can be retrieved by using:
   ```python
   theme = user.theme
   ```




## Compatibility
- Compatible with Python 3.8 and above.
- Compatible with Django 3.2 and above.


## Versioning
This project follows [semantic versioning][200] (SemVer).


## License and code of conduct
Check the root of the repo for these files.








[//]: # (Links)

[200]: https://semver.org/
