import hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


def create_gravatar_url(email: str, size: int = 200) -> str:
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    email_bytestring = email.strip().lower().encode("utf-8")
    email_hash = hashlib.md5(email_bytestring).hexdigest()
    return GRAVATAR_URL.format(hashed_email=email_hash, size=size)
