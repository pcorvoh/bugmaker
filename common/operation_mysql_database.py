# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 18:21
# @Author   : 王俊
# @File     : operation_mysql_database.py
# @Software : PyCharm
import pymysql

from common.excute_log import com_log
from common.read_config import select_db
from configs.defalut_configs import config
from configs.config import environment_config
from common.exception_msg import DataBaseException


def prick_content(db_type):
    conn_db = select_db(db_type)
    if not conn_db:
        raise AssertionError("db db_type error")
    if isinstance(conn_db["password"], int):
        conn_db["password"] = str(conn_db["password"])
    connect = pymysql.connect(**conn_db)
    if connect:
        return connect
    else:
        raise DataBaseException("数据库连接失败，请检查您的网络！")


class OperationMysql(object):
    config.form_obj(environment_config.get("my_environment_config"))

    @classmethod
    def _escape_args(cls, args, conn_obj):
        if isinstance(args, (tuple, list)):
            return tuple(conn_obj.conn.escape(arg) for arg in args)
        elif isinstance(args, dict):
            return dict((key, conn_obj.conn.escape(val)) for (key, val) in args.items())
        else:
            return conn_obj.conn.escape(args)

    @classmethod
    def _log_sql(cls, query, args, conn):
        if args is not None:
            query = query % cls._escape_args(args, conn)
        com_log.info(query)
        print(query)

    @classmethod
    def get_conn_class(cls, sql):
        if config.get("DATABASE_NAME") in sql or config.get("TBALE_NAME") in sql:
            conn_class = MyMysqlConn
        elif 'installmentdb' in sql:
            conn_class = GMMysqlConn
        else:
            raise Exception('Not support db, sql: {}'.format(sql))
        return conn_class

    @classmethod
    def select_one(cls, sql, params=None, log_sql=False):
        conn_class = cls.get_conn_class(sql)
        with conn_class() as conn:
            if log_sql:
                cls._log_sql(sql, params, conn)
            result = conn.select_one(sql, params)
            return result

    @classmethod
    def select_one_value(cls, sql, params=None, log_sql=False):
        conn_class = cls.get_conn_class(sql)
        with conn_class() as conn:
            if log_sql:
                cls._log_sql(sql, params, conn)
            result = conn.select_one_value(sql, params)
            return result

    @classmethod
    def select_many(cls, sql, params=None, log_sql=False):
        conn_class = cls.get_conn_class(sql)
        with conn_class() as conn:
            if log_sql:
                cls._log_sql(sql, params, conn)
            result = conn.select_many(sql, params)
            return result

    @classmethod
    def exec(cls, sql, params=None, log_sql=True):
        conn_class = cls.get_conn_class(sql)
        with conn_class() as conn:
            if log_sql:
                cls._log_sql(sql, params, conn)
            result = conn.exec(sql, params)
            return result


class BaseMysql(object):
    def __init__(self, db_type="mydb"):
        self.conn = prick_content(db_type)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.cur.close()
        self.conn.close()

    def select_one(self, sql, param=None):
        count = self.cur.execute(sql, param)
        if count > 0:
            return self.cur.fetchone()
        return None

    def select_one_value(self, sql, param=None):
        count = self.cur.execute(sql, param)
        if count > 0:
            result = self.cur.fetchone()
            return list(result.values())[0]
        return None

    def select_many(self, sql, param=None):
        count = self.cur.execute(sql, param)
        if count > 0:
            return self.cur.fetchall()
        return None

    def insert(self, sql, param=None):
        try:
            self.cur.execute(sql, param)
            return self.cur.lastrowid
        except Exception as e:
            print(e)
            self.conn.rollback()

    def update(self, sql, param=None):
        try:
            self.cur.execute(sql, param)
        except Exception as e:
            print(e)
            self.conn.rollback()

    def exec(self, sql, param=None):
        if 'select' in sql or 'SELECT' in sql:
            result = self.select_many(sql, param)
            if result is not None:
                if len(result) == 1:
                    result = result[0]
            return result
        elif 'insert' in sql or 'INSERT' in sql:
            return self.insert(sql, param)
        else:
            self.update(sql, param)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_tb)
            print(exc_val)
        self.close()
        # if exceptions have been resolved, return true, else  exceptions  will be raised
        return False


class MyMysqlConn(BaseMysql):

    def __init__(self):
        super().__init__('mydb')


class GMMysqlConn(BaseMysql):

    def __init__(self):
        super().__init__('business')


db_conn = OperationMysql


def exec_sql(sql, params=None):
    """
    :param sql:
    :return  None or dict  or  list<dict>:
    """
    result = db_conn.exec(sql, params=params)
    if isinstance(result, int):
        return {'new_id': result}
    return result


if __name__ == '__main__':
    print(exec_sql("select * from db_school.tb_class where ClassNo=%s;", params="AC1302"))
