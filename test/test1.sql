select user_id, sum(amount) as total_sum
from transactions
where status = 'SUCCESS' 
group by user_id
having sum(amount) > 1000