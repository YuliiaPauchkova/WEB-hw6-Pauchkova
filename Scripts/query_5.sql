SELECT t.teacher_name, s.subject_name
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
WHERE t.teacher_name = 'Jeffrey Ortega';
