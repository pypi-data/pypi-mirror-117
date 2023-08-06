==========
Ideler MFA
==========

Die Multi-Faktor Authentisierung wird automatisch in das Admin-Interface von Django
eingesetzt. Oben rechts, in der nähe des Logou-Links lässt sich der Kram einrichten.


============
Installation
============

Aus dem git-Repository installieren::

    pip install --index-url https://__token__:<token>@git.ideler.de/api/v4/projects/476/packages/pypi/simple --no-deps django-ideler-mfa

Nach der Installation, ``ideler_mfa`` den ``INSTALLED_APPS`` in der settings.py hinzufügen::

    INSTALLED_APPS = (
        ...
        'ideler_mfa',
    )

URLs hinzufügen::

    urlpatterns = [
        ...
        path("mfa/", include("ideler_mfa.urls")),
        ...
    ]

Die Middleware nach der ``AuthenticationMiddleware`` hinzufügen::

    MIDDLEWARE = (
        ...
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "ideler_mfa.middleware.MFAMiddleware",
        ...
    )


=============
Konfiguration
=============

In der settings.py::

    IDELER_MFA = {
        "ISSUER_NAME": "Ideler MFA Demo",
        "CONFIGURATION_REDIRECT_URL": "/",
    }

Templates zum überschreiben::

    'ideler_mfa/select.html'
    'ideler_mfa/configure.html'
    'ideler_mfa/verify.html'
    'ideler_mfa/disable.html'
