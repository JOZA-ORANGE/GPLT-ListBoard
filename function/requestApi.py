from requests import get, post
import config

qheader = {
    "x-exam-type-id": config.x_exam_type_id,
    "accept": "application/json; q=1.0, text/*; q=0.8, */*; q=0.1"
}

# 请求cached/board接口
def getBoard(select=''):
    res = get(config.BASEURL + '/cached/board')
    if select == 'score':
        return res.json()['data']['rawData']['score']
    if select == 'teams':
        return res.json()['data']['rawData']['score']['teams']
    if select == 'schools':
        return res.json()['data']['rawData']['score']['schools']
    if select == 'top':
        return res.json()['data']['rawData']['top']
    return res.json()

# 队伍详细信息
def getTeamDetail(_id):
    res = get(config.BASEURL + '/cached/board/team/' + str(_id))
    return res.json()

# 学生基础信息(个人做题情况+宣言等)
def getStudentBase(_id):
    res = get(config.BASEURL + '/cached/board/student/' + str(_id))
    return res.json()

# 获取examGroupId
def getExamGroupId():
    res = get(config.BASEURL + '/cached/examGroupId')
    return res.json()['data']['examGroupId']

# 参赛队伍查询
def getTeamList(keyword='', page=0, limit=50):
    # keyword为空则输出所有学校
    filter = '{"examGroupId":"' + getExamGroupId() + '","keyword":"' + keyword + '"}'
    url = config.qURL + '/teams/visible?filter=' + filter + '&page=' + str(page) + '&limit=' + str(limit) + '&asc=true'
    res = get(url,headers=qheader)
    return res.json()