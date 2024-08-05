import typing as t

from flask import Flask


class FlaskConfig:
    DEBUG: t.Optional[bool]
    PROPAGATE_EXCEPTIONS: t.Optional[bool]
    TRAP_HTTP_EXCEPTIONS: t.Optional[bool]
    TRAP_BAD_REQUEST_ERRORS: t.Optional[bool]
    SECRET_KEY: t.Optional[str]
    SESSION_COOKIE_NAME: t.Optional[str]
    SESSION_COOKIE_DOMAIN: t.Optional[str]
    SESSION_COOKIE_PATH: t.Optional[str]
    SESSION_COOKIE_HTTPONLY: t.Optional[bool]
    SESSION_COOKIE_SECURE: t.Optional[bool]
    SESSION_COOKIE_SAMESITE: t.Optional[t.Literal["Lax", "Strict"]]
    PERMANENT_SESSION_LIFETIME: t.Optional[int]
    SESSION_REFRESH_EACH_REQUEST: t.Optional[bool]
    USE_X_SENDFILE: t.Optional[bool]
    SEND_FILE_MAX_AGE_DEFAULT: t.Optional[int]
    ERROR_404_HELP: t.Optional[bool]
    SERVER_NAME: t.Optional[str]
    APPLICATION_ROOT: t.Optional[str]
    PREFERRED_URL_SCHEME: t.Optional[str]
    MAX_CONTENT_LENGTH: t.Optional[int]
    TEMPLATES_AUTO_RELOAD: t.Optional[bool]
    EXPLAIN_TEMPLATE_LOADING: t.Optional[bool]
    MAX_COOKIE_SIZE: t.Optional[int]

    _flask_config_keys = {
        "DEBUG",
        "PROPAGATE_EXCEPTIONS",
        "TRAP_HTTP_EXCEPTIONS",
        "TRAP_BAD_REQUEST_ERRORS",
        "SECRET_KEY",
        "SESSION_COOKIE_NAME",
        "SESSION_COOKIE_DOMAIN",
        "SESSION_COOKIE_PATH",
        "SESSION_COOKIE_HTTPONLY",
        "SESSION_COOKIE_SECURE",
        "SESSION_COOKIE_SAMESITE",
        "PERMANENT_SESSION_LIFETIME",
        "SESSION_REFRESH_EACH_REQUEST",
        "USE_X_SENDFILE",
        "SEND_FILE_MAX_AGE_DEFAULT",
        "ERROR_404_HELP",
        "SERVER_NAME",
        "APPLICATION_ROOT",
        "PREFERRED_URL_SCHEME",
        "MAX_CONTENT_LENGTH",
        "TEMPLATES_AUTO_RELOAD",
        "EXPLAIN_TEMPLATE_LOADING",
        "MAX_COOKIE_SIZE",
    }

    def __init__(
        self,
        debug: t.Optional[bool] = None,
        propagate_exceptions: t.Optional[bool] = None,
        trap_http_exceptions: t.Optional[bool] = None,
        trap_bad_request_errors: t.Optional[bool] = None,
        secret_key: t.Optional[str] = None,
        session_cookie_name: t.Optional[str] = None,
        session_cookie_domain: t.Optional[str] = None,
        session_cookie_path: t.Optional[str] = None,
        session_cookie_httponly: t.Optional[bool] = None,
        session_cookie_secure: t.Optional[bool] = None,
        session_cookie_samesite: t.Optional[t.Literal["Lax", "Strict"]] = None,
        permanent_session_lifetime: t.Optional[int] = None,
        session_refresh_each_request: t.Optional[bool] = None,
        use_x_sendfile: t.Optional[bool] = None,
        send_file_max_age_default: t.Optional[int] = None,
        error_404_help: t.Optional[bool] = None,
        server_name: t.Optional[str] = None,
        application_root: t.Optional[str] = None,
        preferred_url_scheme: t.Optional[str] = None,
        max_content_length: t.Optional[int] = None,
        templates_auto_reload: t.Optional[bool] = None,
        explain_template_loading: t.Optional[bool] = None,
        max_cookie_size: t.Optional[int] = None,
        app_instance: t.Optional["Flask"] = None,
    ):
        self.DEBUG = debug
        self.PROPAGATE_EXCEPTIONS = propagate_exceptions
        self.TRAP_HTTP_EXCEPTIONS = trap_http_exceptions
        self.TRAP_BAD_REQUEST_ERRORS = trap_bad_request_errors
        self.SECRET_KEY = secret_key
        self.SESSION_COOKIE_NAME = session_cookie_name
        self.SESSION_COOKIE_DOMAIN = session_cookie_domain
        self.SESSION_COOKIE_PATH = session_cookie_path
        self.SESSION_COOKIE_HTTPONLY = session_cookie_httponly
        self.SESSION_COOKIE_SECURE = session_cookie_secure
        self.SESSION_COOKIE_SAMESITE = session_cookie_samesite
        self.PERMANENT_SESSION_LIFETIME = permanent_session_lifetime
        self.SESSION_REFRESH_EACH_REQUEST = session_refresh_each_request
        self.USE_X_SENDFILE = use_x_sendfile
        self.SEND_FILE_MAX_AGE_DEFAULT = send_file_max_age_default
        self.ERROR_404_HELP = error_404_help
        self.SERVER_NAME = server_name
        self.APPLICATION_ROOT = application_root
        self.PREFERRED_URL_SCHEME = preferred_url_scheme
        self.MAX_CONTENT_LENGTH = max_content_length
        self.TEMPLATES_AUTO_RELOAD = templates_auto_reload
        self.EXPLAIN_TEMPLATE_LOADING = explain_template_loading
        self.MAX_COOKIE_SIZE = max_cookie_size

        if app_instance is not None:
            self.apply_config(app_instance)

    def apply_config(self, app):
        if not hasattr(app, "config"):
            raise ValueError("app must have a config attribute")

        for attr in self._flask_config_keys:
            value = getattr(self, attr)
            if value is not None:
                app.config[attr] = value

    def as_dict(self) -> dict:
        return {
            k: getattr(self, k) for k in self._flask_config_keys if getattr(self, k)
        }
