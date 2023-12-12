package com.example.demo.repositories;


import com.example.demo.models.TeacherDocument;

import org.springframework.data.repository.CrudRepository;

public interface TeacherDocumentRepository extends CrudRepository<TeacherDocument, Long> {
}
