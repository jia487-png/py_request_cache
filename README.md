# py_request_cache

#CACHE1源代码
~~~~
import requests_cache    # 导入requests_cache模块
import requests          # 导入网络请求模块
requests_cache.install_cache()    # 设置缓存
requests_cache.clear()            # 清理缓存
url = 'http://httpbin.org/get'    # 定义测试地址
r = requests.get(url)             # 第一次发送网络请求
print('是否存在缓存：',r.from_cache)  # False表示不存在缓存
r = requests.get(url)             # 第二次发送网络请求
print('是否存在缓存：',r.from_cache)  # True表示存在缓存
~~~~
#输出结果
是否存在缓存： False
是否存在缓存： True

#CACHE2源代码
~~~~
import requests_cache    # 导入requests_cache模块
import time              # 导入时间模块
requests_cache.install_cache()    # 设置缓存
requests_cache.clear()            # 清理缓存
# 定义钩子函数
def make_throttle_hook(timeout=0.1):
    def hook(response, *args, **kwargs):
        print(response.text)       #  打印请求结果
        # 判断没有缓存时就添加延时
        if not getattr(response, 'from_cache', False):
            print('等待',timeout,'秒！')
            time.sleep(timeout)     # 等待指定时间
        else:
            print('是否存在请求缓存！',response.from_cache)  # 存在缓存输出True
        return response
    return hook

if __name__ == '__main__':
    requests_cache.install_cache()              # 创建缓存
    requests_cache.clear()                      # 清理缓存
    s = requests_cache.CachedSession()          # 创建缓存会话
    s.hooks = {'response': make_throttle_hook(2)}  # 配置钩子函数
    s.get('http://httpbin.org/get')            # 模拟发送第一次网络请求
    s.get('http://httpbin.org/get')            # 模拟发送第二次网络请求
~~~~
#输出结果

{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.5", 
    "X-Amzn-Trace-Id": "Root=1-6ab5c5d1-4fe68faf48cdf55649d4c7fa"
  }, 
  "origin": "111.60.88.247", 
  "url": "http://httpbin.org/get"
}

等待 2 秒！
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.5", 
    "X-Amzn-Trace-Id": "Root=1-6ab5c5d1-4fe68faf48cdf55649d4c7fa"
  }, 
  "origin": "111.60.88.247", 
  "url": "http://httpbin.org/get"
}

等待 2 秒！
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.5", 
    "X-Amzn-Trace-Id": "Root=1-6ab5c5d1-4fe68faf48cdf55649d4c7fa"
  }, 
  "origin": "111.60.88.247", 
  "url": "http://httpbin.org/get"
}

是否存在请求缓存！ True
