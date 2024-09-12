# Desc: Common models for the application
class AppException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.code = status_code
        self.payload = payload

    def __json__(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        rv["code"] = self.code
        return rv

    def __str__(self):
        return self.message

    def __html__(self):
        return self.__json__()


ERROR_CODE = {
    "USER_NOT_FOUND": 1001,
    "USER_ALREADY_EXISTS": 1002,
    "USER_PASSWORD_ERROR": 1003,
    "USER_NOT_LOGIN": 1004,
    "USER_TOKEN_EXPIRED": 1005,
    "OLD_PASSWORD_ERROR": 1006,
    "RESET_PWD_CODE_EXPIRED": 1007,
    "RESET_PWD_CODE_ERROR": 1008,
    "CHECK_CODE_ERROR": 1009,
    "CHECK_CODE_EXPIRED": 1010,
    "SMS_SEND_ERROR": 1011,
    "SMS_SEND_FREQUENTLY": 1012,
    "SMS_SEND_EXPIRED": 1013,
    "SMS_CHECK_ERROR": 1014,
    "UNKNOWN_ERROR": 9999,
    # 订单相关
    "ORDER_NOT_FOUND": 3001,
    "ORDER_ALREADY_EXISTS": 3002,
    "ORDER_STATUS_ERROR": 3003,
    "ORDER_PAY_ERROR": 3004,
    "ORDER_REFUND_ERROR": 3005,
    "ORDER_PAY_EXPIRED": 3006,
    "ORDER_PAY_NOT_FOUND": 3007,
    "ORDER_HAS_PAID": 3008,
    # 折扣码相关
    "DISCOUNT_NOT_FOUND": 3101,
    "DISCOUNT_ALREADY_USED": 3102,
    "DISCOUNT_LIMIT": 3103,
    "DISCOUNT_NOT_START": 3104,
    "DISCOUNT_EXPIRED": 3105,
    "ORDER_DISCOUNT_ALREADY_USED": 3106,
    #  课程相关
    "COURSE_NOT_FOUND": 4001,
    "LESSON_CANNOT_BE_RESET": 4002,
    # 支付相关
    "PAY_CHANNEL_NOT_SUPPORT": 5001,
    # 文件上传相关
    "FILE_UPLOAD_ERROR": 6001,
    "FILE_TYPE_NOT_SUPPORT": 6002,
    "FILE_SIZE_EXCEED": 6003,
    # 参数错误
    "PARAMS_ERROR": 2001,
    # admin error
    "VIEW_NOT_FOUND": 7001,
}

ERROR_MESSAGE = {
    "USER_NOT_FOUND": "没有找到用户",
    "USER_ALREADY_EXISTS": "用户已经存在",
    "USER_PASSWORD_ERROR": "用户密码错误",
    "USER_NOT_LOGIN": "用户没有登录",
    "USER_TOKEN_EXPIRED": "用户token过期",
    "OLD_PASSWORD_ERROR": "旧密码错误",
    "RESET_PWD_CODE_EXPIRED": "重置密码验证码过期",
    "RESET_PWD_CODE_ERROR": "重置密码验证码错误",
    "UNKNOWN_ERROR": "未知错误",
    "CHECK_CODE_ERROR": "验证码错误",
    "CHECK_CODE_EXPIRED": "验证码过期",
    "SMS_SEND_ERROR": "短信发送失败",
    "SMS_SEND_FREQUENTLY": "短信发送过于频繁",
    "SMS_SEND_EXPIRED": "短信验证码过期",
    "SMS_CHECK_ERROR": "短信验证码错误",
    # 订单相关
    "ORDER_NOT_FOUND": "没有找到订单",
    "ORDER_ALREADY_EXISTS": "订单已经存在",
    "ORDER_STATUS_ERROR": "订单状态错误",
    "ORDER_PAY_ERROR": "订单支付失败",
    "ORDER_REFUND_ERROR": "订单退款失败",
    "ORDER_PAY_EXPIRED": "订单支付过期",
    "ORDER_PAY_NOT_FOUND": "没有找到支付订单",
    "ORDER_HAS_PAID": "订单已经支付",
    # 折扣码相关
    "DISCOUNT_NOT_FOUND": "没有找到折扣码",
    "DISCOUNT_ALREADY_USED": "折扣码已经使用",
    "DISCOUNT_LIMIT": "折扣码数量限制",
    "DISCOUNT_NOT_START": "折扣码未开始",
    "DISCOUNT_EXPIRED": "折扣码已过期",
    "ORDER_DISCOUNT_ALREADY_USED": "订单已使用折扣码",
    # 课程相关
    "COURSE_NOT_FOUND": "没有找到课程",
    "LESSON_CANNOT_BE_RESET": "课程不能重置",
    # 支付相关
    "PAY_CHANNEL_NOT_SUPPORT": "不支持的支付渠道",
    # 文件上传相关
    "FILE_UPLOAD_ERROR": "文件上传失败",
    "FILE_TYPE_NOT_SUPPORT": "不支持的文件类型",
    "FILE_SIZE_EXCEED": "文件大小超过限制",
    # admin error
    "VIEW_NOT_FOUND": "没有找到视图",
    # 参数错误
    "PARAMS_ERROR": "参数错误:{param_message}",
}

USER_NOT_FOUND = AppException(
    ERROR_MESSAGE["USER_NOT_FOUND"], ERROR_CODE["USER_NOT_FOUND"]
)
USER_ALREADY_EXISTS = AppException(
    ERROR_MESSAGE["USER_ALREADY_EXISTS"], ERROR_CODE["USER_ALREADY_EXISTS"]
)
USER_PASSWORD_ERROR = AppException(
    ERROR_MESSAGE["USER_PASSWORD_ERROR"], ERROR_CODE["USER_PASSWORD_ERROR"]
)
USER_NOT_LOGIN = AppException(
    ERROR_MESSAGE["USER_NOT_LOGIN"], ERROR_CODE["USER_NOT_LOGIN"]
)
USER_TOKEN_EXPIRED = AppException(
    ERROR_MESSAGE["USER_TOKEN_EXPIRED"], ERROR_CODE["USER_TOKEN_EXPIRED"]
)
OLD_PASSWORD_ERROR = AppException(
    ERROR_MESSAGE["OLD_PASSWORD_ERROR"], ERROR_CODE["OLD_PASSWORD_ERROR"]
)
RESET_PWD_CODE_EXPIRED = AppException(
    ERROR_MESSAGE["RESET_PWD_CODE_EXPIRED"], ERROR_CODE["RESET_PWD_CODE_EXPIRED"]
)
RESET_PWD_CODE_ERROR = AppException(
    ERROR_MESSAGE["RESET_PWD_CODE_ERROR"], ERROR_CODE["RESET_PWD_CODE_ERROR"]
)
UNKNOWN_ERROR = AppException(
    ERROR_MESSAGE["UNKNOWN_ERROR"], ERROR_CODE["UNKNOWN_ERROR"]
)
CHECK_CODE_ERROR = AppException(
    ERROR_MESSAGE["CHECK_CODE_ERROR"], ERROR_CODE["CHECK_CODE_ERROR"]
)
CHECK_CODE_EXPIRED = AppException(
    ERROR_MESSAGE["CHECK_CODE_EXPIRED"], ERROR_CODE["CHECK_CODE_EXPIRED"]
)
SMS_SEND_ERROR = AppException(
    ERROR_MESSAGE["SMS_SEND_ERROR"], ERROR_CODE["SMS_SEND_ERROR"]
)
SMS_SEND_FREQUENTLY = AppException(
    ERROR_MESSAGE["SMS_SEND_FREQUENTLY"], ERROR_CODE["SMS_SEND_FREQUENTLY"]
)
SMS_SEND_EXPIRED = AppException(
    ERROR_MESSAGE["SMS_SEND_EXPIRED"], ERROR_CODE["SMS_SEND_EXPIRED"]
)
SMS_CHECK_ERROR = AppException(
    ERROR_MESSAGE["SMS_CHECK_ERROR"], ERROR_CODE["SMS_CHECK_ERROR"]
)

ORDER_NOT_FOUND = AppException(
    ERROR_MESSAGE["ORDER_NOT_FOUND"], ERROR_CODE["ORDER_NOT_FOUND"]
)
ORDER_ALREADY_EXISTS = AppException(
    ERROR_MESSAGE["ORDER_ALREADY_EXISTS"], ERROR_CODE["ORDER_ALREADY_EXISTS"]
)
ORDER_STATUS_ERROR = AppException(
    ERROR_MESSAGE["ORDER_STATUS_ERROR"], ERROR_CODE["ORDER_STATUS_ERROR"]
)
ORDER_PAY_ERROR = AppException(
    ERROR_MESSAGE["ORDER_PAY_ERROR"], ERROR_CODE["ORDER_PAY_ERROR"]
)
ORDER_REFUND_ERROR = AppException(
    ERROR_MESSAGE["ORDER_REFUND_ERROR"], ERROR_CODE["ORDER_REFUND_ERROR"]
)
ORDER_PAY_EXPIRED = AppException(
    ERROR_MESSAGE["ORDER_PAY_EXPIRED"], ERROR_CODE["ORDER_PAY_EXPIRED"]
)
ORDER_PAY_NOT_FOUND = AppException(
    ERROR_MESSAGE["ORDER_PAY_NOT_FOUND"], ERROR_CODE["ORDER_PAY_NOT_FOUND"]
)
ORDER_HAS_PAID = AppException(
    ERROR_MESSAGE["ORDER_HAS_PAID"], ERROR_CODE["ORDER_HAS_PAID"]
)

COURSE_NOT_FOUND = AppException(
    ERROR_MESSAGE["COURSE_NOT_FOUND"], ERROR_CODE["COURSE_NOT_FOUND"]
)
LESSON_CANNOT_BE_RESET = AppException(
    ERROR_MESSAGE["LESSON_CANNOT_BE_RESET"], ERROR_CODE["LESSON_CANNOT_BE_RESET"]
)

PAY_CHANNEL_NOT_SUPPORT = AppException(
    ERROR_MESSAGE["PAY_CHANNEL_NOT_SUPPORT"], ERROR_CODE["PAY_CHANNEL_NOT_SUPPORT"]
)

FILE_UPLOAD_ERROR = AppException(
    ERROR_MESSAGE["FILE_UPLOAD_ERROR"], ERROR_CODE["FILE_UPLOAD_ERROR"]
)
FILE_TYPE_NOT_SUPPORT = AppException(
    ERROR_MESSAGE["FILE_TYPE_NOT_SUPPORT"], ERROR_CODE["FILE_TYPE_NOT_SUPPORT"]
)
FILE_SIZE_EXCEED = AppException(
    ERROR_MESSAGE["FILE_SIZE_EXCEED"], ERROR_CODE["FILE_SIZE_EXCEED"]
)

VIEW_NOT_FOUND = AppException(
    ERROR_MESSAGE["VIEW_NOT_FOUND"], ERROR_CODE["VIEW_NOT_FOUND"]
)

DISCOUNT_NOT_FOUND = AppException(
    ERROR_MESSAGE["DISCOUNT_NOT_FOUND"], ERROR_CODE["DISCOUNT_NOT_FOUND"]
)
DISCOUNT_ALREADY_USED = AppException(
    ERROR_MESSAGE["DISCOUNT_ALREADY_USED"], ERROR_CODE["DISCOUNT_ALREADY_USED"]
)
ORDER_DISCOUNT_ALREADY_USED = AppException(
    ERROR_MESSAGE["ORDER_DISCOUNT_ALREADY_USED"],
    ERROR_CODE["ORDER_DISCOUNT_ALREADY_USED"],
)
DISCOUNT_LIMIT = AppException(
    ERROR_MESSAGE["DISCOUNT_LIMIT"], ERROR_CODE["DISCOUNT_LIMIT"]
)
DISCOUNT_NOT_START = AppException(
    ERROR_MESSAGE["DISCOUNT_NOT_START"], ERROR_CODE["DISCOUNT_NOT_START"]
)
DISCOUNT_EXPIRED = AppException(
    ERROR_MESSAGE["DISCOUNT_EXPIRED"], ERROR_CODE["DISCOUNT_EXPIRED"]
)


def raise_param_error(param_message):
    raise AppException(
        ERROR_MESSAGE["PARAMS_ERROR"].format(param_message=param_message),
        ERROR_CODE["PARAMS_ERROR"],
    )
