import hashlib
import hmac
import secrets


_ALGORITHM = "pbkdf2_sha256"
_ITERATIONS = 600_000
_MIN_ITERATIONS = 100_000
_MAX_ITERATIONS = 1_000_000
_SALT_BYTES = 16


def hash_password(password):
    salt = secrets.token_bytes(_SALT_BYTES)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, _ITERATIONS
    )
    return f"{_ALGORITHM}${_ITERATIONS}${salt.hex()}${digest.hex()}"


def _parse_hash(encoded):
    try:
        algorithm, iterations_text, salt_text, digest_text = encoded.split("$")
        iterations = int(iterations_text)
        salt = bytes.fromhex(salt_text)
        digest = bytes.fromhex(digest_text)
    except (AttributeError, TypeError, ValueError):
        return None

    if (
        algorithm != _ALGORITHM
        or not _MIN_ITERATIONS <= iterations <= _MAX_ITERATIONS
        or len(salt) != _SALT_BYTES
        or len(digest) != hashlib.sha256().digest_size
    ):
        return None
    return iterations, salt, digest


def is_password_hash(encoded):
    return _parse_hash(encoded) is not None


def verify_password(password, encoded):
    parsed = _parse_hash(encoded)
    if parsed is None:
        return False

    iterations, salt, expected_digest = parsed
    actual_digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    )
    return hmac.compare_digest(actual_digest, expected_digest)