from multiprocessing import managers
from typing import Optional
from venv import logger
from pymysql import connect
from sqlalchemy import create_engine, inspect, table, text


class MySQLDatabaseManager():

    def __init__(self, connect_string: str):
        """
        初始化Mysql数据库连接
        
        Args:
            connect_string (str): 连接字符串，格式为 'mysql+pymysql://user:password@host:port/dbname'
        """
        self.engine = create_engine(connect_string,
                                    pool_size=10,
                                    pool_recycle=3600)

    def get_table_names(self) -> list[str]:
        try:
            inspector = inspect(self.engine)
            return inspector.get_table_names()
        except Exception as e:
            logger.exception(e)
            raise ValueError(f"获取数据库表名失败: {str(e)}")

    def get_table_with_comment(self) -> list[dict]:
        """
        获取数据库表名及注释
        
        Returns:
            list[dict]: 包含表名及注释的字典列表
        """
        try:
            query = text("""
                         SELECT TABLE_NAME,TABLE_COMMENT 
                         FROM information_schema.TABLES 
                         WHERE TABLE_SCHEMA = DATABASE()
                         AND TABLE_TYPE = 'BASE TABLE'
                         ORDER BY TABLE_NAME
                     """)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                tables = [{
                    'table_name': row[0],
                    'table_comment': row[1]
                } for row in result]
                return tables
        except Exception as e:
            logger.exception(e)
            raise ValueError(f"获取数据库表注释失败: {str(e)}")

    def get_table_schema(self, table_name: Optional[list[str]] = None) -> str:
        """
        获取数据库表结构
        
        Args:
            table_name : 表名
        Returns:
            list[dict]: 包含表结构的字典列表
        """
        try:
            inspector = inspect(self.engine)
            tables = table_name or inspector.get_table_names()
            schema_list = []
            for table in tables:
                columns = inspector.get_columns(table)
                column_info = [
                    f"{col['name']} {col['type']}" for col in columns
                ]
                schema = f"Table: {table}\n" + "\n".join(column_info)
                schema_list.append(schema)
            return "\n\n".join(schema_list)
        except Exception as e:
            logger.exception(e)
            raise ValueError(f"获取数据库表结构失败: {str(e)}")


if __name__ == '__main__':
    connect_string = 'mysql+pymysql://root:123456@localhost:3306/test'
    manager = MySQLDatabaseManager(connect_string)
    print(manager.get_table_names())
