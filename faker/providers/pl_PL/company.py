# coding: utf-8
from __future__ import unicode_literals
from ..company import Provider as CompanyProvider
import random

class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}} i {{last_name}} {{company_suffix}}',
        '{{last_name}}, {{last_name}} i {{last_name}} {{company_suffix}}',
    )

    company_suffixes = (
        's.j.', 'sp. z o.o.',
    )
    
    def company(self):
        if random.randrange(5):
            pattern = self.random_element(self.formats)
            return self.generator.parse(pattern)
        else:
            return self.random_element([
                'Rad', 'Jan', 'Bart', 'Zdzich', 'Mar', 'Przem', 'Jar', 'Dan',
                'Tom', 'Bruk', 'Koszul', 'Śrub', 'Drut', 'Omer', 'Krzych',
                'Sław', 'Jak', 'Jac', 'Ant', 'Luc'
            ]) + self.random_element(['pol', 'ex'])
