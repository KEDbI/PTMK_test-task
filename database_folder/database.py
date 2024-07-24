import mysql
from mysql import connector
from database_folder.db_config import DatabaseConfig, load_database_config
import logging
from database_folder.user_data import UserData

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO',
                    format='#%(levelname)-8s [%(asctime)s] %(filename)s: %(lineno)d - %(name)s - %(message)s')

config: DatabaseConfig = load_database_config()


class Database:
    table_name: str = 'test1'

    def create_table(self, **columns_with_data_type: {str: str}) -> None:
        logger.info('Starting creating a table')
        temp_str = ''
        result = ''
        for key in columns_with_data_type.items():
            temp_str += key[0] + ' ' + key[1] + ', '
            result += temp_str
            temp_str = ''
        else:
            result = result.rstrip(', ')
        try:
            logger.info('Connecting to db')
            with connector.connect(database=config.db.database_name,
                                   user=config.db.user,
                                   password=config.db.password,
                                   host=config.db.host,
                                   port=config.db.port) as conn:
                cursor = conn.cursor()
                cursor.execute(f"CREATE TABLE {self.table_name} "
                               f"{result})")
                logger.info('Query executed')
                print('Query executed.')
        except mysql.connector.errors.ProgrammingError:
            print(f'Table "{self.table_name}" already exists')
        except:
            logger.exception('Query or connection failed')
            return None

    def insert_row(self, columns_with_values: dict) -> None:
        logger.info('Starting inserting a row')
        columns = ''
        values = []
        for key, value in columns_with_values.items():
            columns += f'{key}, '
            values.append(f'{value}')
        else:
            columns = columns.rstrip(', ')
        try:
            logger.info('Connecting to db')
            with connector.connect(database=config.db.database_name,
                                   user=config.db.user,
                                   password=config.db.password,
                                   host=config.db.host,
                                   port=config.db.port) as conn:
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO {self.table_name} ({columns}) "
                               f"VALUES ({str('%s, ' * len(values)).rstrip(', ')})", tuple(values))
                # При работе с Postgres и psycopg2 контекстный менеджер with сохранял изменения в бд и закрывал соединение
                # Mysql.connector видимо, так не умеет. Хотя в методе с созданием таблицы все работает норм
                conn.commit()
                conn.close()
                logger.info('Query executed')
                print('Query executed.')
        except:
            logger.exception('Query or connection failed')
            return None

    def insert_rows(self, *columns, values: list[tuple | list]) -> None:
        logger.info('Starting inserting rows')
        col = ', '.join(columns)
        try:
            logger.info('Connecting to db')
            with connector.connect(database=config.db.database_name,
                                   user=config.db.user,
                                   password=config.db.password,
                                   host=config.db.host,
                                   port=config.db.port) as conn:
                cursor = conn.cursor()
                cursor.executemany(f"INSERT INTO {self.table_name} ({col}) "
                                   f"VALUES ({str('%s, ' * len(columns)).rstrip(', ')})", values)
                conn.commit()
                conn.close()
                logger.info('Query executed')
                print(f'Query executed. Inserted {len(values)} rows.')
        except:
            logger.exception('Query or connection failed')
            return None

    @staticmethod
    def convert_obj_list_into_values_list(obj_list: list[UserData]) -> list:
        values = []
        for i in obj_list:
            values.append([str(f'{i.full_name}'), str(f'{i.birth_date}'), str(f'{i.sex}'), str(f'{i.get_age()}')])
        return values

    def select_distinct_and_sort_rows(self, *columns: str, order_by: str) -> None:
        logger.info('Starting getting sorted rows')
        col = ', '.join(columns)
        try:
            logger.info('Connecting to db')
            with connector.connect(database=config.db.database_name,
                                   user=config.db.user,
                                   password=config.db.password,
                                   host=config.db.host,
                                   port=config.db.port) as conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(f"SELECT DISTINCT {col} "
                               f"FROM {self.table_name} "
                               f"ORDER BY {order_by}")
                for i in cursor.fetchall():
                    temp_str = ''
                    for key, value in i.items():
                        temp_str += f'{key}: {value}, '
                    print(temp_str.rstrip(', '))
                logger.info('Query executed')
                print('Query executed.')
        except:
            logger.exception('Query or connection failed')
            return None

    def task5(self):
        # Уже не было времени на выполнение задания, поэтому быстро накидал
        logger.info('Starting executing query for task 5')
        try:
            logger.info('Connecting to db')
            with connector.connect(database=config.db.database_name,
                                   user=config.db.user,
                                   password=config.db.password,
                                   host=config.db.host,
                                   port=config.db.port) as conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(f"SELECT * FROM {self.table_name} "
                               "WHERE sex = 'Male' "
                               "AND full_name LIKE 'F%'")
                for i in cursor.fetchall():
                    temp_str = ''
                    for key, value in i.items():
                        temp_str += f'{key}: {value}, '
                    print(temp_str.rstrip(', '))
                logger.info('Query executed')
                print('Query executed.')
        except:
            logger.exception('Query or connection failed')
            return None