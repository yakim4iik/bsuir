package com.example.demo.controllers;


import com.example.demo.models.TeacherDocument;
import com.example.demo.repositories.CourseRepository;
import com.example.demo.repositories.TeacherDocumentRepository;
import com.example.demo.repositories.TeacherRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping("api/teacher-document")
public class TeacherDocumentController {
    private final TeacherDocumentRepository teacherDocumentRepository;
    private final TeacherRepository teacherRepository;
    private final CourseRepository courseRepository;

    public TeacherDocumentController(TeacherDocumentRepository teacherDocumentRepository,
            TeacherRepository teacherRepository, CourseRepository courseRepository) {
        this.teacherDocumentRepository = teacherDocumentRepository;
        this.teacherRepository = teacherRepository;
        this.courseRepository = courseRepository;
    }

    @GetMapping
    public Iterable<TeacherDocument> getAll(Optional<Long> teacherId) {
        List<TeacherDocument> teacherDocuments = new ArrayList<>();
        for (TeacherDocument teacherDocument : teacherDocumentRepository.findAll()) {
            if (teacherId.isEmpty()) {
                teacherDocuments.add(teacherDocument);
                continue;
            }
            if (teacherDocument.getTeacher() != null && teacherId.get().equals(teacherDocument.getTeacher().getId())) {
                teacherDocuments.add(teacherDocument);
            }
        }
        return teacherDocuments;
    }

    @PostMapping
    public TeacherDocument post(@RequestBody TeacherDocument teacherDocument) {
        
        teacherDocument.setStart(new Date());
        if( teacherDocument.getTeacher() != null && teacherDocument.getTeacher().getId() != null) {
            teacherDocument.setTeacher(teacherRepository.findById(teacherDocument.getTeacher().getId()).orElse(null));
        }
        if (teacherDocument.getCourse() != null && teacherDocument.getCourse().getId() != null) {
            teacherDocument.setCourse(courseRepository.findById(teacherDocument.getCourse().getId()).orElse(null));
        }
        long courseLengthDays = teacherDocument.getCourse() != null ? teacherDocument.getCourse().getDays() : 30;
        teacherDocument.setEnd(new Date(new Date().getTime() + courseLengthDays * 24 * 60 * 60 * 1000));
        return teacherDocumentRepository.save(teacherDocument);
    }
    
}
