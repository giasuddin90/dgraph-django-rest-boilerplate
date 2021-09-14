from decouple import config
import pydgraph
from service.log import *
import json


class DgraphBase(object):
    dgraph_key = config('DGRAPH_API_KEY')
    dgraph_url = config('DGRAPH_URL')

    @classmethod
    def db_connection(cls):
        """
        connect with dgraph server
        """
        try:
            # this line will be used for cloud connection
            # client_stub = pydgraph.DgraphClientStub.from_slash_endpoint(cls.dgraph_url, cls.dgraph_key)
            client_stub = pydgraph.DgraphClientStub(cls.dgraph_url)
            client = pydgraph.DgraphClient(client_stub)
            return client
        except Exception as ex:
            # logger
            Log.general_log(ex, "dgraph_connection_error")
            client = None
            return client

    @classmethod
    def cloud_db_connection(cls):
        """
        connect with dgraph server
        """
        try:
            # This function will connect dgraph clould db
            client_stub = pydgraph.DgraphClientStub.from_slash_endpoint(cls.dgraph_url, cls.dgraph_key)
            client = pydgraph.DgraphClient(client_stub)
            return client
        except Exception as ex:
            # logger
            Log.general_log(ex, "dgraph_connection_error")
            client = None
            return client

    @classmethod
    def schema_alter(cls, schema):
        client = cls.db_connection()
        try:
            sync_schema = client.alter(pydgraph.Operation(schema=schema))
            return sync_schema
        except Exception as ex:
            # logger
            Log.general_log(ex, "dgraph_schema_sync_error")
            return None

    @classmethod
    def drop_all(cls):
        """
        Drop All - discard all data and start from a clean slate.
        """
        client = cls.db_connection()
        return client.alter(pydgraph.Operation(drop_all=True))

    @classmethod
    def query(cls, query_string, variables=None):
        # self._app.logger.debug(f"Sending dgraph query.")
        client = cls.db_connection()
        if variables is None:
            res = client.txn(read_only=True).query(query_string)
        else:
            res = client.txn(read_only=True).query(query_string, variables=variables)
        # self._app.logger.debug(f"Received response for dgraph query.")
        data = json.loads(res.json)
        return data

    @classmethod
    def update(cls, uid, input_data):
        """
        Dgraph update query
        """
        if type(input_data) is not dict:
            raise TypeError()

        input_data['uid'] = uid

        txn = cls.db_connection().txn()

        try:
            response = txn.mutate(set_obj=input_data)
            txn.commit()
        except Exception as ex:
            # logger
            error_data = str(ex) + str(input_data)
            Log.general_log(error_data, "update_query_error")
            response = False
        finally:
            txn.discard()

        if response:
            return str(uid)
        else:
            return False

    @classmethod
    def delete(cls, uid):
        """
        This function will be used for delete any dgraph node
        """

        mutation = {'uid': uid}
        txn = cls.db_connection().txn()

        try:
            response = txn.mutate(del_obj=mutation)
            txn.commit()
        except Exception as ex:
            # logger
            error_data = str(ex) + str(uid)
            Log.general_log(error_data, "delete_query_error")
            response = False
        finally:
            txn.discard()

        if response:
            return True
        else:
            return False

