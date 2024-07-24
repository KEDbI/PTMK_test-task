from dataclasses import dataclass
import logging
from datetime import date, datetime


logger = logging.getLogger(__name__)
logging.basicConfig(level='ERROR',
                    format='#%(levelname)-8s [%(asctime)s] %(filename)s: %(lineno)d - %(name)s - %(message)s')


@dataclass
class UserData:
    full_name: str
    birth_date: str
    sex: str

    def check_data_format(self):
        check_birthdate = self._validate_date()
        if self.full_name.isdigit():
            return False
        elif self.sex.lower() not in ['male', 'female']:
            return False
        elif not check_birthdate:
            return False
        return True

    def _validate_date(self):
        try:
            datetime.strptime(self.birth_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_age(self) -> int:
        logger.info('Getting age')
        try:
            birthdate = f'{self.birth_date}'
            birthdate = date(year=int(self.birth_date.split('-')[0]),
                             month=int(self.birth_date.split('-')[1]),
                             day=int(self.birth_date.split('-')[2]))
            today = date.today()
            return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month,
                                                                              birthdate.day))
        except:
            logger.exception('Failed')