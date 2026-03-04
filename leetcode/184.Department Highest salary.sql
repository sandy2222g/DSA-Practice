select d.name department,e.name employee,e.salary salary 
from employee e join department d 
on e.departmentid=d.id 
where e.salary=(
    select max(salary) from employee where departmentid=e.departmentid
)
;
