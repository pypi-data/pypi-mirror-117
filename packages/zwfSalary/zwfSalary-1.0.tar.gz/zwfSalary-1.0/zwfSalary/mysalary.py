"""
��ģ�����ڼ��㹫˾Ա����н��
"""
company = "�ɷ���"
def yearSalary(monthSalary):
    """���ݴ������н���������н"""
    yearSalary = monthSalary*13
def daySalary(monthSalary):
    """���ݴ������н�������ÿ���н��,���ҹ���ÿ���ϰ�ʱ��Ϊ22.5��"""
    daySalary = monthSalary/22.5

if __name__=="__main__":         #���Դ���
    print(yearSalary(3000))
    print(daySalary(3000))