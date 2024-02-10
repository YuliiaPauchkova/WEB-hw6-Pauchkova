SELECT t.teacher_name, AVG(g.grade) AS avg_grade
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
JOIN grades g ON s.subject_id = g.subject_id
GROUP BY t.teacher_name;
