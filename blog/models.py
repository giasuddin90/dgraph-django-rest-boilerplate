from service.dgraph_base import DgraphBase
from service.log import *
import datetime
import json


class Blogs(DgraphBase):

    # Set schema.
    @classmethod
    def set_schema(cls):
        """
        This function will be used for
        """
        schema = """
        title: string @index(exact) .
        description: string .
        summery: string .
        category: string .
        created_at: datetime .
        type Blog {
            title
            description
            summery
            category
            created_at
        }
        """
        return cls.schema_alter(schema)

    @classmethod
    def create_blog(cls, post_data):
        # if type(post_data) is not dict:
        #     raise TypeError()

        post_data['uid'] = '_:newpost'
        post_data['dgraph.type'] = 'Blog'
        post_data['created_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()

        txn = cls.db_connection().txn()

        try:
            response = txn.mutate(set_obj=post_data)
            txn.commit()
        except Exception as ex:
            # logger
            error_data = str(ex) + str(post_data)
            Log.general_log(error_data, "blog_create_error")
            response = False
        finally:
            txn.discard()

        if response:
            return response.uids['newpost']
        else:
            return False

    @classmethod
    def blog_list(cls):
        txn = cls.db_connection().txn()
        query = """{
                posts(func: type(Blog))  {
                    uid
                    title
                    description
                    category
                    summery
                }
                }"""

        res = txn.query(query)
        data = json.loads(res.json)
        posts_data = data.get('posts', None)
        return posts_data

    @classmethod
    def get_blog(cls, uid):
        txn = cls.db_connection().txn()

        query_uid = f'{{ post(func: uid({uid})) @filter(type("Blog"))'
        query_fields = '''{ 
                                uid title description category summery

                           } }'''

        query = query_uid + query_fields

        res = txn.query(query)

        data = json.loads(res.json)

        if len(data['post']) == 0:
            return False

        data = data['post'][0]
        return data
