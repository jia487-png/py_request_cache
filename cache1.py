import requests_cache    # 导入requests_cache模块
import requests          # 导入网络请求模块
requests_cache.install_cache()    # 设置缓存
requests_cache.clear()            # 清理缓存
url = 'http://httpbin.org/get'    # 定义测试地址
r = requests.get(url)             # 第一次发送网络请求
print('是否存在缓存：',r.from_cache)  # False表示不存在缓存
r = requests.get(url)             # 第二次发送网络请求
print('是否存在缓存：',r.from_cache)  # True表示存在缓存
