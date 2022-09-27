'''
        라이브러리 제공 => 벤더 -> 파이썬
파이썬 <-----------------> 벤더(Datebase)
        라이브러리로 접근(드라이버) => 파이썬 -> 벤더
'''
import cx_Oracle

user ="SCOTT"
pw = "TIGER"
dns = '192.168.90.71:1521/xe'

con = cx_Oracle.connect(user,pw,dns, encoding='utf-8')