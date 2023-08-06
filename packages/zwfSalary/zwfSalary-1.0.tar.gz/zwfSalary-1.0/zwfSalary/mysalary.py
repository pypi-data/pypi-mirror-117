"""
本模块用于计算公司员工的薪资
"""
company = "蒙发利"
def yearSalary(monthSalary):
    """根据传入的月薪，计算出年薪"""
    yearSalary = monthSalary*13
def daySalary(monthSalary):
    """根据传入的月薪，计算出每天的薪资,国家国定每月上班时长为22.5天"""
    daySalary = monthSalary/22.5

if __name__=="__main__":         #测试代码
    print(yearSalary(3000))
    print(daySalary(3000))