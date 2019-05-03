# coding=gbk
import json
import time

import requests

session = requests.Session()
session.headers= {
    "Content-Type": "application/json"
}
timeGap = input("�������ʱ��(��)����Ҫ̫���б�����Աɾ�ķ��գ�\n")
opt = input('1.ע��ˢ��һ���� 2.��ע�ᣬ��ˢ��\n')

if opt == '1':
    stuId = input('������ѧ��\n')
    pwd = input('����������\n')
    name = input('����������\n')
    college = input('������ѧԺȫ��\n')
    clazz = input('������רҵ�༶\n')

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
    stuId = input('������ѧ��\n')


session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/startTest',
             data=json.dumps({
                "studentId": stuId, "testId": 3
             }))

print("�ȴ�" + timeGap + "s.......\n")
time.sleep(int(timeGap))


data = json.dumps(
    {"testrecord":{"studentId":stuId,"testId":3},"submitPaper":{"titleList":[{"titleId":25,"name":"���繥����������ڲ��Գ�״̬����Ϊ( )","diffId":1,"score":2,"options":[{"optionId":97,"titleId":25,"content":"����Ĵ�����","checked":0},{"optionId":98,"titleId":25,"content":"Ӧ�õĴ�����","checked":0},{"optionId":99,"titleId":25,"content":"������Ӳ���ĸ�����","checked":1},{"optionId":100,"titleId":25,"content":"����Ĵ�����","checked":0}]},{"titleId":26,"name":"���繥��������( )","diffId":1,"score":2,"options":[{"optionId":101,"titleId":26,"content":"���������﷨���������幥��","checked":1},{"optionId":102,"titleId":26,"content":"�ڿ͹�������������","checked":0},{"optionId":103,"titleId":26,"content":"Ӳ���������������","checked":0},{"optionId":104,"titleId":26,"content":"���������ڿ͹�������������","checked":0}]},{"titleId":28,"name":"1995��֮����Ϣ���簲ȫ�������( )","diffId":1,"score":2,"options":[{"optionId":109,"titleId":28,"content":"���չ���","checked":1},{"optionId":110,"titleId":28,"content":"���ʿ���","checked":0},{"optionId":111,"titleId":28,"content":"��������","checked":0},{"optionId":112,"titleId":28,"content":"�رܷ���","checked":0}]},{"titleId":49,"name":"��ͳ�Ƶ�����������Σ�����ĺڿ͹�����( )","diffId":1,"score":2,"options":[{"optionId":191,"titleId":49,"content":"©������","checked":0},{"optionId":192,"titleId":49,"content":"��湥��","checked":0},{"optionId":193,"titleId":49,"content":"��������","checked":1}]},{"titleId":52,"name":"ͨ������ʹ��ϰ�ߵ��鷢���д�Լ___%����ʹ�õĿ���ȵ���5���ַ���( )","diffId":1,"score":2,"options":[{"optionId":200,"titleId":52,"content":"50.5","checked":0},{"optionId":201,"titleId":52,"content":"51. 5","checked":1},{"optionId":202,"titleId":52,"content":"52.5","checked":0}]},{"titleId":69,"name":"��Ϣս�ľ������ȷ�Ͻϳ���ս���ľ������ȷ��( )","diffId":1,"score":2,"options":[{"optionId":251,"titleId":69,"content":"��","checked":1},{"optionId":252,"titleId":69,"content":"��","checked":0},{"optionId":253,"titleId":69,"content":"��˵","checked":0}]},{"titleId":94,"name":"Ŀǰ�û��������ڲ����򻮷�ͨ��ͨ��____ʵ��","diffId":1,"score":2,"options":[{"optionId":341,"titleId":94,"content":"�������","checked":0},{"optionId":342,"titleId":94,"content":"Vlan ����","checked":1},{"optionId":343,"titleId":94,"content":"����ǽ����","checked":0}]},{"titleId":109,"name":"ľ�����һ����ָǱ�����û������д��ж������ʵ�____���������������û���֪����������ȡ�û����������ϵ���Ҫ������Ϣ��","diffId":1,"score":2,"options":[{"optionId":393,"titleId":109,"content":".Զ�̿������","checked":1},{"optionId":394,"titleId":109,"content":".���������ϵͳ","checked":0},{"optionId":395,"titleId":109,"content":".ľͷ������","checked":0}]},{"titleId":117,"name":"ĳ��˾δ����Ȩ,�������侭Ӫ����վ�ṩĳ��Ӱ�����߹ۿ�,�ù�˾�ַ��������õ�Ӱ�ĵ�Ӱ��˾��___________","diffId":1,"score":2,"options":[{"optionId":421,"titleId":117,"content":"ר��Ȩ","checked":0},{"optionId":422,"titleId":117,"content":"�̱�Ȩ","checked":0},{"optionId":423,"titleId":117,"content":"��Ϣ���紫��Ȩ","checked":1},{"optionId":424,"titleId":117,"content":"����Ȩ","checked":0}]},{"titleId":148,"name":"��������ĺ�����__","diffId":1,"score":2,"options":[{"optionId":545,"titleId":148,"content":" �޸Ķ�ջ��¼�н��̵ķ��ص�ַ","checked":1},{"optionId":546,"titleId":148,"content":"����Shellcode","checked":0},{"optionId":547,"titleId":148,"content":" �����û�����Ȩ��","checked":0},{"optionId":548,"titleId":148,"content":" ��׽����©��","checked":0}]},{"titleId":159,"name":"����ؼ��豸�����簲ȫר�ò�ƷӦ��������ع��ұ�׼��ǿ����Ҫ���ɾ߱��ʸ�Ļ����� �����߰�ȫ������Ҫ��󣬷������ۻ����ṩ��","diffId":1,"score":2,"options":[{"optionId":589,"titleId":159,"content":"��֤�豸�ϸ�","checked":0},{"optionId":590,"titleId":159,"content":"��ȫ��֤�ϸ�","checked":1},{"optionId":591,"titleId":159,"content":"��֤���ٺϸ�","checked":0},{"optionId":592,"titleId":159,"content":"��֤��Ʒ�ϸ�","checked":0}]},{"titleId":172,"name":"��ץ���簲ȫ������ʵ�ͼ�Ч���ˡ�����λҪ�ι�����������ʶ�������ʶ�������񣬲��ǩ����  ����","diffId":1,"score":2,"options":[{"optionId":641,"titleId":172,"content":"���簲ȫ������","checked":1},{"optionId":642,"titleId":172,"content":"���簲ȫ������","checked":0},{"optionId":643,"titleId":172,"content":"���簲ȫ��ŵ��","checked":0},{"optionId":644,"titleId":172,"content":"���簲ȫ����״","checked":0}]},{"titleId":177,"name":"���ݣ���ҳ����۸ġ���ð��й¶����ȡ���Թ�˾��ȫ��������Ӫ��������������ر��ش�Ӱ�죬���ж�Ϊ��  ������Ϣϵͳ�¼���","diffId":1,"score":2,"options":[{"optionId":661,"titleId":177,"content":"5","checked":1},{"optionId":662,"titleId":177,"content":"6","checked":0},{"optionId":663,"titleId":177,"content":"7","checked":0},{"optionId":664,"titleId":177,"content":"8","checked":0}]},{"titleId":209,"name":"������ ������Ļ��ƣ�һ�ǵ�һʱ�䷢��������ͷ���ռ�������Ϣ�����ǽ�����Ϣ�ռ�ƽ̨������������Ϣ��","diffId":1,"score":2,"options":[{"optionId":789,"titleId":209,"content":"���ٷ���","checked":1},{"optionId":790,"titleId":209,"content":"����","checked":0},{"optionId":791,"titleId":209,"content":"����","checked":0},{"optionId":792,"titleId":209,"content":"�Ѽ�","checked":0}]},{"titleId":241,"name":"( )�����Ǽ�������ý�塢�Ǿ��ã������Ļ�������ʶ��̬���ǹ�����ʵ������Ҫ����?","diffId":1,"score":2,"options":[{"optionId":916,"titleId":241,"content":"����","checked":0},{"optionId":917,"titleId":241,"content":"ý��","checked":0},{"optionId":918,"titleId":241,"content":"����????????","checked":1},{"optionId":919,"titleId":241,"content":"����?????","checked":0}]},{"titleId":288,"name":"�ҹ����ֵ�һ�������������ʱ����(  )?��","diffId":1,"score":2,"options":[{"optionId":1104,"titleId":288,"content":"1968?��?","checked":0},{"optionId":1105,"titleId":288,"content":"1978?��  ?","checked":0},{"optionId":1106,"titleId":288,"content":"1988?��?","checked":1},{"optionId":1107,"titleId":288,"content":"1998?��?","checked":0}]}],"blanksList":[{"titleId":317,"name":"�����簲ȫ����һ�����������ֱ�����ճ�̨�壬�ڻ����ṹ���������ݷ���û�н��и����Ե��޸ġ�","type":1,"answer":"T","score":2},{"titleId":326,"name":"������Ϣ���ռ���ʹ���߲��������������Ը�����Ϣ���д���֮��ʹ���޷�ʶ����ض������Ҳ��ܸ�ԭ�ģ��������ṩ��Щ���������������뾭�����ռ��ߵ�ͬ�⡣","type":1,"answer":"T","score":2},{"titleId":332,"name":"������Ϣ�����ĺ���ԭ���Ǿ������ռ��ߵ�ͬ�⡣","type":1,"answer":"T","score":2},{"titleId":359,"name":"�����ָı䵼�����ì�ܺ͸����������վ���?��","type":1,"answer":"F","score":2},{"titleId":396,"name":"���ұ��ܹ������Ÿ���ȼ������������йر��ܹ����ļල����顢ָ����","type":1,"answer":"T","score":2},{"titleId":502,"name":"·��Э�����û����֤���ܣ��Ϳ���α��·����Ϣ������·�ɱ���ң��Ӷ�ʹ����̱����","type":1,"answer":"T","score":2},{"titleId":528,"name":"�����ҹ���ؼ�����׼�͹涨�������ʼ�����������ʹ������ת�����ܡ�","type":1,"answer":"F","score":2},{"titleId":976,"name":"�ڵ���ʮ�Ŵ󱨸��������������Ҫ��ǿ���������ݽ��裬���������ۺ�������ϵ��Ӫ�����ʵ�����ռ䡣","type":1,"answer":"T","score":2},{"titleId":984,"name":"ϰ��ƽ�����ָ����û�����簲ȫ��û�й��Ұ�ȫ����û�о�������ȶ����У��������Ⱥ������Ҳ���Եõ�����","type":1,"answer":"T","score":2},{"titleId":988,"name":"Ҫ�γ������������۷�Χ������˵ֻ����һ��������һ������","type":1,"answer":"T","score":2}],"judgeList":None,"shortList":[{"titleId":569,"name":"Windows NT�ġ��򡰿��ƻ��ƾ߱���Щ��ȫ���ԣ� (    )\n#A.�û������֤\n#B.���ʿ���\n#C.���(��־)\n#D.����ͨѶ�ļ���","type":3,"answer":"ABC","score":4},{"titleId":583,"name":"�����������_____������� (    )\n#A.��������\n#B.��Ⱦ����\n#C.���в���\n#D.���ֲ���","type":3,"answer":"ABD","score":4},{"titleId":604,"name":"��Ṥ��ѧ���õ��������������   ��\n#A.����Ȩ��\n#B.���ι�ͬ����\n#C.��������\n#D.��������Ͽ�","type":3,"answer":"ABCD","score":4},{"titleId":614,"name":"��־�����ص������   ��\n#A.ԴIP \n#B.���󷽷�\n#C.��������\n#D.״̬����","type":3,"answer":"ABCD","score":4},{"titleId":632,"name":"�����й���˽Ȩ�ı���,��ȷ���ǣ�   ��\n#A.����ʱ��,��˽Ȩ�ı����ܵ��ϴ���\n#B.��Ȼ�������粻ͬ����ʵ����,��Ҳ��Ҫ����������˽\n#C.������������������,���������ϲ���Ҫ�������˵���˽\n#D.���Խ�������������������˽Ȩ","type":3,"answer":"ABD","score":4},{"titleId":645,"name":"δ��Ȩ�������,���ý�����Ʒ��¼����Ʒ�ϴ������Ϻ������ϴ����������Ȩ���˰����� �� \n#A.��Ȩ������\n#B.������\n#C.¼����Ʒ������\n#D.��վ������","type":3,"answer":"ABC","score":4},{"titleId":657,"name":"���¶Ե����ʼ��ı���,��ȷ���ǣ� �� \n#A.ͨѶ˫�����붼�ڳ�\n#B.�ʼ����˹��ʼ�����Ѹ�١��ɿ��ҷ�Χ���� \n#C.�ʼ�����ͬʱ���͸�����û�\n#D.�����ʼ��п��Է������֡�ͼ����������Ϣ","type":3,"answer":"BCD","score":4},{"titleId":734,"name":"web��ȫ��һ��ϵͳ����,������������ȫ��webӦ�÷�������ȫ��webӦ�ó���ȫ�����ݴ��䰲ȫ��Ӧ�ÿͻ��˰�ȫ��Ȼ��,����Ĺ�ģ�͸�����ʹweb��ȫ�����ͨ�������ϵ�Internet��ȫ�����Ϊ���ӡ�Ŀǰ��web��ȫ��Ҫ��Ϊ���¼������棿��  ��\n#A�� �����������������ݵİ�ȫ��\n#B�� �������������û�֮�䴫�ݵ���Ϣ�İ�ȫ��\n#C�� ����webӦ�ÿͻ��˼��价����ȫ��\n#D�� ��֤���㹻�Ŀռ���ڴ棬��ȷ���û�������ʹ�á�","type":3,"answer":"ABC","score":4},{"titleId":745,"name":"���������ָ����������α�����վ����ƭ�Եĵ����ʼ����е�����թƭ�����������������㳣�������ֶε��ǣ�\n#A�� α��������������վ\n#B�� ��ʾ���IP��ַ��������\n#C�� ��������ƭ\n#D�� ����������ƭ","type":3,"answer":"ABCD","score":4},{"titleId":763,"name":"δ�����ĳ����ʱ���ŵ���һСŮ������,���ϴ������͡�������Ƭ��ĳ��־��������,����Ϊ��ĸŮ���,��ĳ�������š�������Щ˵������ȷ��?(  )\n#A.��־���ֺ�����ĳ��Ф��Ȩ\n#B.��־���ֺ�����ĳ������Ȩ\n#C.��־���ֺ�����ĳ����˽Ȩ\n#D.��ĳ��Ȩ����־��Ҫ�������⳥","type":3,"answer":"ACD","score":4},{"titleId":763,"name":"δ�����ĳ����ʱ���ŵ���һСŮ������,���ϴ������͡�������Ƭ��ĳ��־��������,����Ϊ��ĸŮ���,��ĳ�������š�������Щ˵������ȷ��?(  )\n#A.��־���ֺ�����ĳ��Ф��Ȩ\n#B.��־���ֺ�����ĳ������Ȩ\n#C.��־���ֺ�����ĳ����˽Ȩ\n#D.��ĳ��Ȩ����־��Ҫ�������⳥","type":3,"answer":"ACD","score":4},{"titleId":763,"name":"δ�����ĳ����ʱ���ŵ���һСŮ������,���ϴ������͡�������Ƭ��ĳ��־��������,����Ϊ��ĸŮ���,��ĳ�������š�������Щ˵������ȷ��?(  )\n#A.��־���ֺ�����ĳ��Ф��Ȩ\n#B.��־���ֺ�����ĳ������Ȩ\n#C.��־���ֺ�����ĳ����˽Ȩ\n#D.��ĳ��Ȩ����־��Ҫ�������⳥","type":3,"answer":"ACD","score":4}],"shortAnswer":None,"caseAnswer":None,"discussAnswer":None}}
)

session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/submitTest',
             data=data)

res = session.post(url='http://yiban.csu.edu.cn/java/nskc_2019/test/testRecordInfo',
             data=json.dumps({
                 "studentId": stuId, "testId": 3
             }))

print("���ķ���" + str(json.loads(res.text)['score']))
print("��ǰ��http://yiban.csu.edu.cn/java/nskc_2019/�鿴\n")
