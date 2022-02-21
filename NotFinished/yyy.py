age_limit = 18
query = f'''
SELECT users.id, users.name
From users
WHERE age > {age_limit}
'''

postgres = 'select 1;'
oracle = 'select 1 from dual;'