import codecs
import re

from dateutil import parser

from peewee import IntegrityError

import models


class WhatsAppParser:
    regex = re.compile(
        '(?P<datetime>\d{2}:\d{2},\s\D{3}\s\d{1,2})\s-\s(?P<name>\w+(?::\s*\w+)*|[\w\s]+?):\s(?P<message>(?:.+|\n))')

    def parse_file(self):
        f = codecs.open('path-to-file', 'r', 'utf_8')
        errors = []
        for line in f:
            result = self.regex.match(line)
            if result is not None:
                print(result.groupdict())
                try:
                    with models.database.transaction():
                        models.Message.create(datetime=parser.parse(result.group('datetime')),
                                              text=result.group('message'),
                                              sender=result.group('name'), messenger='whatsapp')
                except IntegrityError:
                    pass
            else:
                errors.append(line)