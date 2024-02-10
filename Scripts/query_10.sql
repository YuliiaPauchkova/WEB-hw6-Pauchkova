SELECT s.subject_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE st.student_id = 1 AND t.teacher_name = 'Jeffrey Ortega';
