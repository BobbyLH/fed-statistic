ret_list = {
  '成功': 0,
  '服务器错误': -1,
  '参数错误': 40000,
  '项目未注册': 40100,
  '项目删除失败': 400101,
  '未能成功入库，请重试': 40102,
  '未找到工具信息': 40103,
  '不允许直接添加日志信息': 40104,
  '未找到日志信息': 40105,
  '暂不支持该服务': 40106,
  '请传入正确的数据格式': 40200,
  '缺少关键参数': 40201,
  '请求方法不匹配': 40202
}

def make_res(msg = '成功', data = None):
  res = {}
  res['msg'] = msg
  for key in ret_list.keys():
    if msg == key:
      res['ret'] = ret_list[key]
      break
  if not 'ret' in res:
    res['ret'] = 50000
  if data:
    res['data'] = data
  return res