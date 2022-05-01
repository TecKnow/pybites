import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
    _domain_regex = re.compile(r'.*\.[a-z]{2,3}$')

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if self._domain_regex.fullmatch(name) is None:
            raise DomainException()
        self.name = name

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively

    def __str__(self) -> str:
        return self.name

    @classmethod
    def parse_url(cls, url: str):
        protocol_separator_location = url.find("://")
        domain_and_resource = url[protocol_separator_location+3:]
        resource_separator_location = domain_and_resource.find("/")
        if resource_separator_location >= 0:
            domain_part = domain_and_resource[:resource_separator_location]
        else:
            domain_part = domain_and_resource
        return Domain(domain_part)

    @classmethod
    def parse_email(cls, email: str):
        separator_location = email.find("@")
        domain_part = email[separator_location+1:]
        return Domain(domain_part)


if __name__ == "__main__":
    url_str = "https://nu.nl-nu.nl"
    d = Domain.parse_url(url_str)
