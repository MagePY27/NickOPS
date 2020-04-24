# 脚本用来发送 celery 任务

from test_celery import *

# # 最基本推送一个任务，不支持任何选项
# ret = add.delay(3, 6)
# print(ret.get())
# # 错误的输入，触发重试
# add.delay(3, 'aaa')
#
# # 推送一个任务，第一个参数 (2,5) 为任务参数，必须为 tuple 或 list，
# # 如果任务只需要一个参数，必须添加逗号进行转换，格式 (var1,)
# # countdown=10，10 秒后开始执行
# add.apply_async((2, 5), countdown=10)
# # 参数的其他写法，
# add.apply_async(kwargs={'x': 4, 'y': 8})
# add.s(5, 6).apply_async()
#
# # 任务组
# from celery import group
#
# numbers = [(2, 2), (4, 4), (8, 8), (16, 16)]
# res = group(add.subtask(i) for i in numbers).apply_async()
# print(res.get())
#
# # 使用 link，将任务结果作为第一个参数传递到下一个任务
# add.apply_async((2, 3), link=add.s(16))
#
# # 同样，前一个任务结果作为下一个任务的第一个参数
# from celery import chain
#
# res = chain(add.s(2, 2), add.s(4), add.s(8))()
# print(res.get())
#
# # 使用管道符
# (add.s(2, 2) | add.s(4) | add.s(8))().get()

# 任务队列
add.apply_async(
    (10, 100),  # 任务参数
    queue='lst1'  # 任务队列
)

add.apply_async(
    (20, 200),  # 任务参数
    queue='lst2'  # 任务队列
)
