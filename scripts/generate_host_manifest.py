"""从 portable manifest 生成宿主兼容元数据，不改变产品身份或宣称宿主已验收。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def generate():
    source=json.loads((ROOT/'plugin.json').read_text())
    base={k:v for k,v in source.items() if k not in {'$schema','extensions'}}
    interface=source.get('extensions',{}).get('com.openai',{}).get('interface',{})
    target={**base,'skills':'./skills/'}
    target.update(source.get('extensions',{}).get('com.openai',{}))
    zcode={**base,'displayName':interface.get('displayName',source['name']),'skills':'./skills/'}
    kimi={**base,'interface':interface,'skills':'./skills/'}
    for relative,data in (('.codex-plugin/plugin.json',target),('.zcode-plugin/plugin.json',zcode),('kimi.plugin.json',kimi)):
        path=ROOT/relative;path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return target
if __name__=='__main__':generate()
