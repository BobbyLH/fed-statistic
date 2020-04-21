ret_list = {
  '成功': 0,
  '服务器错误': -1,
  '参数错误': 40000,
  '项目未注册': 40100,
  '未能成功入库，请重试': 40101,
  '未找到工具信息': 40102,
  '不允许直接添加日志信息': 40103,
  '未找到日志信息': 40104,
  '请传入正确的数据格式': 40200,
  '缺少关键参数': 40201,
  '请求方法不匹配': 40202
}

def make_res(msg = '成功', data = None):
  res = {}
  res['msg'] = msg
  res['ret'] = ret_list[msg] if not ret_list[msg] == None else 50000
  if data:
    res['data'] = data
  return res