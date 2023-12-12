package com.example.demo.repositories;


import com.example.demo.models.CourseAndCurrentTeacher;

import org.springframework.data.repository.Repository;

public interface CourseAndCurrentTeacherRepository extends Repository<CourseAndCurrentTeacher, Long> {
    Iterable<CourseAndCurrentTeacher> findAll();
}
