from django.http import JsonResponse


class ErrorResponse(JsonResponse):
    status = 'error'

    def __init__(self, message=''):
        jsend = {
            'status': self.status,
            'message': message
        }

        super().__init__(data=jsend, status=400)


class FailResponse(JsonResponse):
    status = 'fail'

    def __init__(self, message='', details=None):
        jsend = {
            'status': self.status,
            'data': {
                'message': message,
                'details': details or []
            }
        }

        super().__init__(data=jsend, status=404)


class SuccessResponse(JsonResponse):
    status = 'success'

    def __init__(self, object, status_code=200):
        jsend = {
            'status': self.status,
            'data': {
                'object': object,
            }
        }

        super().__init__(data=jsend, status=status_code)


class SuccessListResponse(JsonResponse):
    status = 'success'

    def __init__(self, objects, pagination):
        jsend = {
            'status': self.status,
            'data': {
                'objects': objects,
                'pagination': pagination,
            }
        }

        super().__init__(data=jsend)
