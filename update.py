import json
import os
import sys
import requests

commit = sys.argv[1]

def 获取npm包最新版本(pkgname):
    return(json.loads(requests.get('https://registry.npmjs.org/'+pkgname+'/latest').text)['version'])


with open('_config.yun.yml', encoding='utf-8') as f:
    oriconfig = f.read()
print('开始检测npm仓库最新版本\r--------\r')
latest = 获取npm包最新版本('tnxg-blog')
oriconfig = oriconfig.replace('[TNXG-Static-CDN]', 'https://npm.elemecdn.com/tnxg-blog@' + latest + ' #[TNXG-Static-CDN]')
print('当前npm库最新版本：' + latest + '\r--------\r')
with open('_config.yun.yml', 'w', encoding='utf-8') as f:
    f.write(oriconfig)
print('开始上传github仓库\r--------\r')
os.system('git add .')
os.system('git commit -m "' + commit + '"')
os.system('git push https://github.com/TNXG/blog.git')
print('OK')