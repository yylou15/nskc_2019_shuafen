# coding=gbk
import json
import time

import requests

session = requests.Session()
session.headers= {
    "Content-Type": "application/json"
}
timeGap = input("输入答题时间(秒)（不要太短有被管理员删的风险）\n")
opt = input('1.注册刷分一条龙 2.已注册，仅刷分\n')

if opt == '1':
    stuId = input('请输入学号\n')
    pwd = input('请输入密码\n')
    name = input('请输入姓名\n')
    college = input('请输入学院全称\n')
    clazz = input('请输入专业班级\n')

    session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/account/registerForInfo',
                 data=json.dumps({
                     "studentId": stuId,
                     "username": name,
                     "sex": 0,
                     "clazz": clazz,
                     "college": college,
                     "grade": 9999,
                     "major": ""
                 })
    )
    session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/account/registerForAccount',
                 data=json.dumps({
                     "studentId": stuId, "password": pwd
                 }))


else:
    stuId = input('请输入学号\n')


session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/startTest',
             data=json.dumps({
                "studentId": stuId, "testId": 3
             }))

print("等待" + timeGap + "s.......\n")
time.sleep(int(timeGap))


data = json.dumps(
    {"testrecord":{"studentId":stuId,"testId":3},"submitPaper":{"titleList":[{"titleId":25,"name":"网络攻击与防御处于不对称状态是因为( )","diffId":1,"score":2,"options":[{"optionId":97,"titleId":25,"content":"管理的脆弱性","checked":0},{"optionId":98,"titleId":25,"content":"应用的脆弱性","checked":0},{"optionId":99,"titleId":25,"content":"网络软，硬件的复杂性","checked":1},{"optionId":100,"titleId":25,"content":"软件的脆弱性","checked":0}]},{"titleId":26,"name":"网络攻击的种类( )","diffId":1,"score":2,"options":[{"optionId":101,"titleId":26,"content":"物理攻击，语法攻击，语义攻击","checked":1},{"optionId":102,"titleId":26,"content":"黑客攻击，病毒攻击","checked":0},{"optionId":103,"titleId":26,"content":"硬件攻击，软件攻击","checked":0},{"optionId":104,"titleId":26,"content":"物理攻击，黑客攻击，病毒攻击","checked":0}]},{"titleId":28,"name":"1995年之后信息网络安全问题就是( )","diffId":1,"score":2,"options":[{"optionId":109,"titleId":28,"content":"风险管理","checked":1},{"optionId":110,"titleId":28,"content":"访问控制","checked":0},{"optionId":111,"titleId":28,"content":"消除风险","checked":0},{"optionId":112,"titleId":28,"content":"回避风险","checked":0}]},{"titleId":49,"name":"从统计的情况看，造成危害最大的黑客攻击是( )","diffId":1,"score":2,"options":[{"optionId":191,"titleId":49,"content":"漏洞攻击","checked":0},{"optionId":192,"titleId":49,"content":"蠕虫攻击","checked":0},{"optionId":193,"titleId":49,"content":"病毒攻击","checked":1}]},{"titleId":52,"name":"通过口令使用习惯调查发现有大约___%的人使用的口令长度低于5个字符的( )","diffId":1,"score":2,"options":[{"optionId":200,"titleId":52,"content":"50.5","checked":0},{"optionId":201,"titleId":52,"content":"51. 5","checked":1},{"optionId":202,"titleId":52,"content":"52.5","checked":0}]},{"titleId":69,"name":"信息战的军人身份确认较常规战争的军人身份确认( )","diffId":1,"score":2,"options":[{"optionId":251,"titleId":69,"content":"难","checked":1},{"optionId":252,"titleId":69,"content":"易","checked":0},{"optionId":253,"titleId":69,"content":"难说","checked":0}]},{"titleId":94,"name":"目前用户局域网内部区域划分通常通过____实现","diffId":1,"score":2,"options":[{"optionId":341,"titleId":94,"content":"物理隔离","checked":0},{"optionId":342,"titleId":94,"content":"Vlan 划分","checked":1},{"optionId":343,"titleId":94,"content":"防火墙防范","checked":0}]},{"titleId":109,"name":"木马程序一般是指潜藏在用户电脑中带有恶意性质的____，利用它可以在用户不知情的情况下窃取用户联网电脑上的重要数据信息。","diffId":1,"score":2,"options":[{"optionId":393,"titleId":109,"content":".远程控制软件","checked":1},{"optionId":394,"titleId":109,"content":".计算机操作系统","checked":0},{"optionId":395,"titleId":109,"content":".木头做的马","checked":0}]},{"titleId":117,"name":"某公司未经授权,擅自在其经营的网站提供某电影供在线观看,该公司侵犯了制作该电影的电影公司的___________","diffId":1,"score":2,"options":[{"optionId":421,"titleId":117,"content":"专利权","checked":0},{"optionId":422,"titleId":117,"content":"商标权","checked":0},{"optionId":423,"titleId":117,"content":"信息网络传播权","checked":1},{"optionId":424,"titleId":117,"content":"发明权","checked":0}]},{"titleId":148,"name":"溢出攻击的核心是__","diffId":1,"score":2,"options":[{"optionId":545,"titleId":148,"content":" 修改堆栈记录中进程的返回地址","checked":1},{"optionId":546,"titleId":148,"content":"利用Shellcode","checked":0},{"optionId":547,"titleId":148,"content":" 提升用户进程权限","checked":0},{"optionId":548,"titleId":148,"content":" 捕捉程序漏洞","checked":0}]},{"titleId":159,"name":"网络关键设备和网络安全专用产品应当按照相关国家标准的强制性要求，由具备资格的机构（ ）或者安全检测符合要求后，方可销售或者提供。","diffId":1,"score":2,"options":[{"optionId":589,"titleId":159,"content":"认证设备合格","checked":0},{"optionId":590,"titleId":159,"content":"安全认证合格","checked":1},{"optionId":591,"titleId":159,"content":"认证网速合格","checked":0},{"optionId":592,"titleId":159,"content":"认证产品合格","checked":0}]},{"titleId":172,"name":"狠抓网络安全责任落实和绩效考核。各单位要牢固树立风险意识，充分认识责任义务，层层签订（  ）。","diffId":1,"score":2,"options":[{"optionId":641,"titleId":172,"content":"网络安全责任书","checked":1},{"optionId":642,"titleId":172,"content":"网络安全保障书","checked":0},{"optionId":643,"titleId":172,"content":"网络安全承诺书","checked":0},{"optionId":644,"titleId":172,"content":"网络安全责任状","checked":0}]},{"titleId":177,"name":"数据（网页）遭篡改、假冒、泄露或窃取，对公司安全生产、经营活动或社会形象产生特别重大影响，可判定为（  ）级信息系统事件。","diffId":1,"score":2,"options":[{"optionId":661,"titleId":177,"content":"5","checked":1},{"optionId":662,"titleId":177,"content":"6","checked":0},{"optionId":663,"titleId":177,"content":"7","checked":0},{"optionId":664,"titleId":177,"content":"8","checked":0}]},{"titleId":209,"name":"建立（ ）舆情的机制，一是第一时间发现舆情苗头，收集舆情信息，二是建立信息收集平台，整理舆情信息。","diffId":1,"score":2,"options":[{"optionId":789,"titleId":209,"content":"快速发现","checked":1},{"optionId":790,"titleId":209,"content":"分析","checked":0},{"optionId":791,"titleId":209,"content":"引导","checked":0},{"optionId":792,"titleId":209,"content":"搜集","checked":0}]},{"titleId":241,"name":"( )不仅是技术、是媒体、是经济，更是文化、是意识形态、是国家软实力的重要体现?","diffId":1,"score":2,"options":[{"optionId":916,"titleId":241,"content":"舆论","checked":0},{"optionId":917,"titleId":241,"content":"媒介","checked":0},{"optionId":918,"titleId":241,"content":"网络????????","checked":1},{"optionId":919,"titleId":241,"content":"电脑?????","checked":0}]},{"titleId":288,"name":"我国出现第一例计算机病毒的时间是(  )?。","diffId":1,"score":2,"options":[{"optionId":1104,"titleId":288,"content":"1968?年?","checked":0},{"optionId":1105,"titleId":288,"content":"1978?年  ?","checked":0},{"optionId":1106,"titleId":288,"content":"1988?年?","checked":1},{"optionId":1107,"titleId":288,"content":"1998?年?","checked":0}]}],"blanksList":[{"titleId":317,"name":"《网络安全法》一、二、三审稿直至最终出台稿，在基本结构、基本内容方面没有进行根本性的修改。","type":1,"answer":"T","score":2},{"titleId":326,"name":"个人信息的收集、使用者采用匿名化技术对个人信息进行处理之后，使其无法识别出特定个人且不能复原的，向他人提供这些匿名化的数据无须经过被收集者的同意。","type":1,"answer":"T","score":2},{"titleId":332,"name":"个人信息保护的核心原则是经过被收集者的同意。","type":1,"answer":"T","score":2},{"titleId":359,"name":"利益格局改变导致社会矛盾和各种诉求与日俱增?。","type":1,"answer":"F","score":2},{"titleId":396,"name":"国家保密工作部门负责等级保护工作中有关保密工作的监督、检查、指导。","type":1,"answer":"T","score":2},{"titleId":502,"name":"路由协议如果没有认证功能，就可以伪造路由信息，导致路由表混乱，从而使网络瘫痪。","type":1,"answer":"T","score":2},{"titleId":528,"name":"根据我国相关技术标准和规定，电子邮件服务器允许使用匿名转发功能。","type":1,"answer":"F","score":2},{"titleId":976,"name":"在党的十九大报告中提出，我们需要加强互联网内容建设，建立网络综合治理体系，营造清朗的网络空间。","type":1,"answer":"T","score":2},{"titleId":984,"name":"习近平总书记指出，没有网络安全就没有国家安全，就没有经济社会稳定运行，广大人民群众利益也难以得到保障","type":1,"answer":"T","score":2},{"titleId":988,"name":"要形成良好网上舆论氛围，就是说只能有一个声音、一个调子","type":1,"answer":"T","score":2}],"judgeList":None,"shortList":[{"titleId":569,"name":"Windows NT的“域“控制机制具备哪些安全特性？ (    )\n#A.用户身份验证\n#B.访问控制\n#C.审计(日志)\n#D.数据通讯的加密","type":3,"answer":"ABC","score":4},{"titleId":583,"name":"计算机病毒由_____部分组成 (    )\n#A.引导部分\n#B.传染部分\n#C.运行部分\n#D.表现部分","type":3,"answer":"ABD","score":4},{"titleId":604,"name":"社会工程学利用的人性弱点包括（   ）\n#A.信任权威\n#B.信任共同爱好\n#C.期望守信\n#D.期望社会认可","type":3,"answer":"ABCD","score":4},{"titleId":614,"name":"日志分析重点包括（   ）\n#A.源IP \n#B.请求方法\n#C.请求链接\n#D.状态代码","type":3,"answer":"ABCD","score":4},{"titleId":632,"name":"下列有关隐私权的表述,正确的是（   ）\n#A.网络时代,隐私权的保护受到较大冲击\n#B.虽然网络世界不同于现实世界,但也需要保护个人隐私\n#C.由于网络是虚拟世界,所以在网上不需要保护个人的隐私\n#D.可以借助法律来保护网络隐私权","type":3,"answer":"ABD","score":4},{"titleId":645,"name":"未经权利人许可,不得将其作品或录音制品上传到网上和在网上传播。这里的权利人包括（ ） \n#A.版权所有人\n#B.表演者\n#C.录音制品制作者\n#D.网站管理者","type":3,"answer":"ABC","score":4},{"titleId":657,"name":"以下对电子邮件的表述,正确的是（ ） \n#A.通讯双方必须都在场\n#B.邮件比人工邮件传送迅速、可靠且范围更广 \n#C.邮件可以同时发送给多个用户\n#D.电子邮件中可以发送文字、图像、语音等信息","type":3,"answer":"BCD","score":4},{"titleId":734,"name":"web安全是一个系统问题,包括服务器安全、web应用服务器安全、web应用程序安全、数据传输安全和应用客户端安全。然而,网络的规模和复杂性使web安全问题比通常意义上的Internet安全问题更为复杂。目前的web安全主要分为以下几个方面？（  ）\n#A、 保护服务器及其数据的安全；\n#B、 保护服务器和用户之间传递的信息的安全；\n#C、 保护web应用客户端及其环境安全；\n#D、 保证有足够的空间和内存，来确保用户的正常使用。","type":3,"answer":"ABC","score":4},{"titleId":745,"name":"网络钓鱼是指攻击者利用伪造的网站或欺骗性的电子邮件进行的网络诈骗活动。以下属于网络钓鱼常见攻击手段的是：\n#A、 伪造相似域名的网站\n#B、 显示虚假IP地址而非域名\n#C、 超链接欺骗\n#D、 弹出窗口欺骗","type":3,"answer":"ABCD","score":4},{"titleId":763,"name":"未婚的张某旅游时抱着当地一小女孩拍照,并上传到博客。后来照片被某杂志用作封面,标题为“母女情深”,张某深受困扰。下列哪些说法是正确的?(  )\n#A.杂志社侵害了张某的肖像权\n#B.杂志社侵害了张某的名誉权\n#C.杂志社侵害了张某的隐私权\n#D.张某有权向杂志社要求精神损害赔偿","type":3,"answer":"ACD","score":4},{"titleId":763,"name":"未婚的张某旅游时抱着当地一小女孩拍照,并上传到博客。后来照片被某杂志用作封面,标题为“母女情深”,张某深受困扰。下列哪些说法是正确的?(  )\n#A.杂志社侵害了张某的肖像权\n#B.杂志社侵害了张某的名誉权\n#C.杂志社侵害了张某的隐私权\n#D.张某有权向杂志社要求精神损害赔偿","type":3,"answer":"ACD","score":4},{"titleId":763,"name":"未婚的张某旅游时抱着当地一小女孩拍照,并上传到博客。后来照片被某杂志用作封面,标题为“母女情深”,张某深受困扰。下列哪些说法是正确的?(  )\n#A.杂志社侵害了张某的肖像权\n#B.杂志社侵害了张某的名誉权\n#C.杂志社侵害了张某的隐私权\n#D.张某有权向杂志社要求精神损害赔偿","type":3,"answer":"ACD","score":4}],"shortAnswer":None,"caseAnswer":None,"discussAnswer":None}}
)

session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/submitTest',
             data=data)

res = session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/testRecordInfo',
             data=json.dumps({
                 "studentId": stuId, "testId": 3
             }))

print("您的分数" + str(json.loads(res.text)['score']))
print("请前往http://yiban.csu.edu.cn/java/nskc_2019/查看\n")
