SELECT s.student_id, s.student_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 2
GROUP BY s.student_id, s.student_name
ORDER BY avg_grade DESC
LIMIT 1;
