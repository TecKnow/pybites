import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envlist = self.config["tox"]["envlist"]
        envlist = envlist.replace('\n', ',')
        envlist = envlist.split(',')
        envlist = [y for x in envlist if (y := x.strip())]
        return envlist

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return list({section_proxy.get(property_name) for (section_name, section_proxy) in self.config.items() for property_name in section_proxy if property_name == "basepython"})
