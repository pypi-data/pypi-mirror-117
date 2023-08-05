# -*- coding=utf-8 -*-

from enum import Enum
import sys
import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor

from x_py_libs.db import BaseDBHelper

class PgDBHelper(BaseDBHelper):

    def connect(self):
        try:
            conn = psycopg2.connect(self.connect_string, cursor_factory=DictCursor)
            conn.set_client_encoding('UTF8')
            # print(conn)
            return conn
        except psycopg2.Error as e:
            print('psycopg2 error:', e.pgerror)
            return None

    
    # def get_one(self, table_name, fields, sc=None, conditions=None):
    #     rst, cnt = self.get_list(table_name, fields, sc=sc, conditions=conditions, order_field=None, order_type=None, count=False, pagination=False)
    #     return rst[0] if len(rst) > 0 else None


    def get_list_base(self, table_name, fields, condition='', params=None, order_field='id', order_type='DESC', page_index=0, page_size=10, pagination=True):
        cnt = 0
        if pagination:
            cnt_sql = """SELECT COUNT(1) AS cnt FROM """ + table_name + ' WHERE 1 = 1 ' + condition + """;"""
            rst = self.fetch_one(cnt_sql, params)
            cnt = rst['cnt']

        sql = """SELECT """ + fields + """ FROM """ + table_name
        sql += """ WHERE 1 = 1 """
        sql += condition

        if order_field is not None and order_type is not None:
            order_field = [order_field] if type(order_field) is str else order_field
            order_type = [order_type] if type(order_type) is str else order_type

            if len(order_type) != len(order_field):
                order_type = list(map(lambda x: order_type[0], range(len(order_field))))

            sort_list = list(map(lambda f, t: """ %s %s """ % (f, t), order_field, order_type))

            sql += """ ORDER BY """ + ','.join(sort_list)

        if pagination:
            if page_size > 0:
                sql += """ LIMIT %s OFFSET %s """
                params.append(page_size)
                params.append(page_size*page_index)

            # __page_size = 10
            # __page_index = 0

            # if sc is not None:
            #     __page_size = int(sc['pageSize'] if sc['pageSize'] is not None else 10)
            #     __page_index = int(sc['pageIndex'] if sc['pageIndex'] is not None else 1)-1
            # else:
            #     __page_size = page_size
            #     __page_index = page_index

            # if __page_size > 0:
            #     sql += """ LIMIT %s OFFSET %s """
            #     params.append(__page_size)
            #     params.append(__page_size*__page_index)

        sql += """;"""

        # print(sql, params)

        rst = self.fetch_all(sql, params)
        return rst, cnt

    def fetch_returning_id(self, sql, *params, **kw):
        sql = sql + """ RETURNING id;"""

        def callback(cur):
            rst = cur.fetchone()
            id = rst.get('id')
            return 0 if id is None else id

        return self.execute_sql(sql, callback, *params, **kw)

    # def fetch_rowcount(self, sql, *params, **kw):
    #     def callback(cur):
    #         # print('cur:',cur)
    #         return cur.rowcount

    #     return self.execute_sql(sql, callback, *params, **kw)

    # def fetch_one(self, sql, *params, **kw):
    #     def callback(cur):
    #         return cur.fetchone()

    #     return self.execute_sql(sql, callback, *params, **kw)

    # def fetch_all(self, sql, *params, **kw):
    #     def callback(cur):
    #         return cur.fetchall()

    #     return self.execute_sql(sql, callback, *params, **kw)

    def execute_sql(self, sql, callback, *params, **kw):
        conn = self.connect()

        if conn == None:
            return None

        # print(sql, *params, type(params), len(params), **kw)
        is_multiple = False if kw.get('is_multiple') == None else kw['is_multiple']
        # print('--kw--:', kw, kw.get('is_multiple'), is_multiple)

        cur = conn.cursor(cursor_factory=RealDictCursor)
        # cur = conn.cursor()
        rst = None

        if is_multiple:
            psycopg2.extras.execute_values(cur, sql, params, page_size=9999)
        else:
            if params is not None:
                # print('sql:', cur.mogrify(sql, *params))
                cur.execute(sql, *params)
            else:
                cur.execute(sql)

        # rst = cur.fetchone()

        rst = callback(cur)
        conn.commit()
        conn.close()
        # print('rst:',rst)
        return rst

    def callproc(self, proc_name, *params):
        conn = self.connect()

        if conn == None:
            return None

        cur = conn.cursor()
        cur.callproc(proc_name, *params)
        rst = cur.fetchall()

        conn.commit()
        conn.close()
        return rst


"""
    # def execute_values(self, sql, *params):
    #     conn = db_helper.connect()

    #     if conn == None:
    #         return None

    #     print(params, type(params), list(params))

    #     cur = conn.cursor()
    #     psycopg2.extras.execute_values(cur, sql, params)
    #     rst = cur.rowcount
    #     conn.commit()
    #     conn.close()
    #     return rst
"""
