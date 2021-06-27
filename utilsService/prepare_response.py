
def prepare_success_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': 'success',
        'message': 'Data successfully returned',
        'data': serializer_data
    }
    return response


def prepare_error_response(details):
    '''
    get error message and return error response
    :param details:
    :return:
    '''
    response = {
        'status': 'error',
        'message': details,
        "data": None
    }
    return response

