# Copyright 2021 The Data Text Grid Reader Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
from typing import List, Optional

import sqlalchemy
from sqlalchemy.engine.cursor import CursorResult


class DBConnector:
    _db_connection = None

    def __init__(self, db_uri: str):
        """
        :param db_uri: Examples:
        sqlite://
        postgresql+psycopg2://postgres:@localhost/postgres
        snowflake://username:password@my_account_locator.us-east-1/DEMO_DB/PUBLIC?warehouse=COMPUTE_WH
        """
        self._db_uri = db_uri
        self._db_connection = None

    def __del__(self):
        self.close()

    def execute_as_cursor(self, sql: str) -> CursorResult:
        if not self._db_connection:
            db_engine = sqlalchemy.create_engine(self._db_uri)
            self._db_connection = db_engine.connect()
        return self._db_connection.execute(sql)

    def execute(self, sql: str) -> List[dict]:
        return [dict(row) for row in self.execute_as_cursor(sql)]

    @staticmethod
    def _get_calling_file_path() -> str:
        stack = inspect.stack()
        calling_file = next(context for context in stack if context.filename != __file__).filename
        return calling_file[0: calling_file.rfind('/') + 1]

    def execute_script_file_as_cursor(
            self,
            query_file: str,
            text_substitution_map: Optional[dict] = None
    ) -> CursorResult:
        """
        Open and execute a SQL script
        :param query_file: A relative or absolute path leading to the script to be executed.
        :param text_substitution_map: Allows for a sort of variable substitution
        by allowing the caller to replace substrings in the script (for example,
        database names) with substitute values that allow the script to run.
        :return: A SQLAlchemy Cursor Result
        """
        if not query_file.startswith('/'):
            query_file = self._get_calling_file_path() + query_file

        with open(query_file, 'r') as f:
            sql = f.read().strip()
            text_substitution_map = text_substitution_map or []
            for key in text_substitution_map:
                value = str(text_substitution_map[key])
                sql = sql.replace('{' + str(key) + '}', value)
                # TODO: Use regex to make sure key isn't a substring:
                sql = sql.replace(':' + str(key), value)
            return self.execute_as_cursor(sql)

    def execute_script_file(
            self,
            query_file: str,
            text_substitution_map: Optional[dict] = None
    ) -> List[dict]:
        """
        Open and execute a SQL script
        :param query_file: A relative or absolute path leading to the script to be executed.
        :param text_substitution_map: Allows for a sort of variable substitution
        by allowing the caller to replace substrings in the script (for example,
        database names) with substitute values that allow the script to run.
        :return: A list of dicts representing rows in the result set.
        """
        return [dict(row) for row in self.execute_script_file_as_cursor(query_file, text_substitution_map)]

    def close(self) -> None:
        if self._db_connection:
            self._db_connection.close()
            self._db_connection = None
