package com.example.demo.controllers;


import com.example.demo.models.Teacher;
import com.example.demo.repositories.CategoryRepository;
import com.example.demo.repositories.EducationRepository;
import com.example.demo.repositories.SexRepository;
import com.example.demo.repositories.TeacherRepository;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/teacher")
public class TeacherController {
    private final SexRepository sexRepository;
    private final EducationRepository educationRepository;
    private final CategoryRepository categoryRepository;
    private final TeacherRepository teacherRepository;


    public TeacherController(SexRepository sexRepository, EducationRepository educationRepository,
            CategoryRepository categoryRepository, TeacherRepository teacherRepository) {
        this.sexRepository = sexRepository;
        this.educationRepository = educationRepository;
        this.categoryRepository = categoryRepository;
        this.teacherRepository = teacherRepository;
    }

    @GetMapping
    public Iterable<Teacher> getAll() {
        return teacherRepository.findAll();
    }

    @PutMapping
    public void put(@RequestBody Teacher teacher) {
        if(teacher.getSex() != null) {
            teacher.setSex(sexRepository.findById(teacher.getSex().getId()).get());
        }
        if(teacher.getEducation() != null) {
            teacher.setEducation(educationRepository.findById(teacher.getEducation().getId()).get());
        }
        if(teacher.getCategory() != null) {
            teacher.setCategory(categoryRepository.findById(teacher.getCategory().getId()).get());
        }
        teacherRepository.save(teacher);
    }

    @PostMapping 
    public Long post(@RequestBody Teacher teacher) {
        if(teacher.getSex() != null) {
            teacher.setSex(sexRepository.findById(teacher.getSex().getId()).get());
        }
        if(teacher.getEducation() != null) {
            teacher.setEducation(educationRepository.findById(teacher.getEducation().getId()).get());
        }
        if(teacher.getCategory() != null) {
            teacher.setCategory(categoryRepository.findById(teacher.getCategory().getId()).get());
        }
        teacherRepository.save(teacher);
        return teacher.getId();
    }

    @DeleteMapping
    public void delete(@RequestParam Long teacherId) {
        teacherRepository.deleteById(teacherId);
    }
}
