SELECT '2023-05-05'::DATE,
'123'::INT,
true::BOOLEAN,
'2.71'::REAL;

SELECT 
    COUNT(job_id),
    EXTRACT(MONTH FROM job_posted_date) AS month
FROM job_postings_fact
WHERE job_title_short = 'Data Engineer'
GROUP BY month
ORDER BY COUNT(job_id) DESC


