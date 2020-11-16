"""#FIN NAMES OF EMPLOYEES STARTING WITH 'a'"""
SELECT FIRST_NAME FROM HR.EMPLOYEES WHERE FIRST_NAME LIKE 'A%';

"""Find number of employees with salary lower than 17000"""
SELECT COUNT(*) FROM HR.EMPLOYEES WHERE SALARY < 17000;

"""Find employees with the job id it prog"""
select * from hr.employees where JOB_ID ='IT_PROG';


"""Find employees with the manager id >100"""
select * from hr.employees where manager_id > 100;