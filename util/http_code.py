class Code():
    #: 没有消息就是好消息
    Ok = 0

    #: ----------------------- 1xxx 用户相关错误 -----------------
    unlogin = 1000

    #: 密码错误
    error_pwd = 1001

    #: 用户不存在
    not_user = 1002

    #: 该用户已存在
    exists_user = 1003

    #: 重复发送验证码
    repeat_code = 1004

    #: 邮箱格式错误
    error_mail = 1005

    #: ----------------------- 2xxx 权限相关错误 -----------------
    only_super = 2000
    not_permission = 2001

    #: ----------------------- 3xxx sql相关错误 -----------------
    sql_execute_error = 3000

    #: ----------------------- 4xxx 定时任务相关错误 -----------------
    params_error = 4000

    code_msg = {
        Ok: 'success',
        only_super: '需要超管权限',
        unlogin: '请先登陆',
        error_pwd: '密码错误',
        not_user: '用户不存在',
        repeat_code: '请不要重复发送验证码',
        error_mail: '邮箱格式错误',
        exists_user: '该用户已存在',
        not_permission: '没有该资源权限',
        sql_execute_error: '数据库执行错误',
        params_error: '参数错误'
    }

    code_unknow_msg = '未知错误'
