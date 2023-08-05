import datetime
import json
from typing import Dict

import asyncpg
import pandas as pd

from liualgotrader.common import config
from liualgotrader.common.database import fetch_as_dataframe
from liualgotrader.common.tlog import tlog


class Accounts:
    @classmethod
    async def create(
        cls,
        balance: float,
        allow_negative: bool = False,
        credit_line: float = 0.0,
        details: Dict = {},
        db_connection: asyncpg.Connection = None,
    ) -> int:
        q = """
                INSERT INTO 
                    accounts (balance, allow_negative, credit_line, details)
                VALUES
                    ($1, $2, $3, $4)
                RETURNING account_id;
            """
        params = [balance, allow_negative, credit_line, json.dumps(details)]
        if db_connection:
            return await db_connection.fetchval(q, *params)

        pool = config.db_conn_pool
        async with pool.acquire() as con:
            async with con.transaction():
                return await con.fetchval(q, *params)

    @classmethod
    async def get_balance(cls, account_id: int) -> float:
        pool = config.db_conn_pool

        async with pool.acquire() as con:
            return await con.fetchval(
                """
                    SELECT
                        balance
                    FROM 
                        accounts 
                    WHERE
                        account_id = $1
                """,
                account_id,
            )

    @classmethod
    async def add_transaction(
        cls,
        account_id: int,
        amount: float,
        tstamp: datetime.datetime = None,
        details: Dict = {},
    ):
        pool = config.db_conn_pool
        async with pool.acquire() as con:
            async with con.transaction():
                try:
                    if tstamp:
                        await con.execute(
                            """
                                INSERT INTO 
                                    account_transactions (account_id, amount, tstamp, details)
                                VALUES
                                    ($1, $2, $3, $4);
                            """,
                            account_id,
                            amount,
                            tstamp,
                            json.dumps(details),
                        )
                    else:
                        await con.execute(
                            """
                                INSERT INTO 
                                    account_transactions (account_id, amount, details)
                                VALUES
                                    ($1, $2, $3);
                            """,
                            account_id,
                            amount,
                            json.dumps(details),
                        )
                except Exception as e:
                    tlog(
                        f"[EXCEPTION] add_transaction({account_id}, {amount}, {tstamp} ) failed with {e} current balance={await cls.get_balance(account_id)}"
                    )
                    raise

    @classmethod
    async def get_transactions(cls, account_id: int) -> pd.DataFrame:
        q = """
            SELECT
                tstamp, amount
            FROM 
                account_transactions 
            WHERE
                account_id = $1
            """

        df = await fetch_as_dataframe(q, account_id)
        return (
            df.set_index("tstamp", drop=True).sort_index()
            if not df.empty
            else df
        )

    @classmethod
    async def clear_balance(cls, account_id: int, new_balance: float):
        pool = config.db_conn_pool
        async with pool.acquire() as con:
            async with con.transaction():
                try:
                    await con.execute(
                        """
                            UPDATE  
                                accounts
                            SET
                                balance = $2
                            WHERE
                                account_id = $1
                        """,
                        account_id,
                        new_balance,
                    )
                except Exception as e:
                    tlog(
                        f"[EXCEPTION] clear_balance() failed with {e} current balance={await cls.get_balance(account_id)}"
                    )
                    raise

    @classmethod
    async def clear_account_transactions(cls, account_id: int):
        pool = config.db_conn_pool
        async with pool.acquire() as con:
            async with con.transaction():
                try:
                    await con.execute(
                        """
                            DELETE FROM  
                                account_transactions
                            WHERE
                                account_id = $1
                        """,
                        account_id,
                    )
                except Exception as e:
                    tlog(
                        f"[EXCEPTION] clear_account_transactions() failed with {e} current balance={await cls.get_balance(account_id)}"
                    )
                    raise
