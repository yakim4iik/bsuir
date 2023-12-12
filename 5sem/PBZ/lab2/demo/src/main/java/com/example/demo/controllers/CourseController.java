package com.example.demo.controllers;

import com.example.demo.models.Course;
import com.example.demo.models.CourseAndCurrentTeacher;
import com.example.demo.models.CoursePrice;
import com.example.demo.repositories.CourseAndCurrentTeacherRepository;
import com.example.demo.repositories.CourseRepository;
import com.example.demo.repositories.TypeRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/course")
public class CourseController {
    private final CourseRepository courseRepository;
    private final CourseAndCurrentTeacherRepository courseAndCurrentTeacherRepository;
    private final CoursePriceController coursePriceController;
    private final TypeRepository typeRepository;

    public CourseController(CourseRepository courseRepository,
            CourseAndCurrentTeacherRepository courseAndCurrentTeacherRepository,
            CoursePriceController coursePriceController, TypeRepository typeRepository) {
        this.courseRepository = courseRepository;
        this.courseAndCurrentTeacherRepository = courseAndCurrentTeacherRepository;
        this.coursePriceController = coursePriceController;
        this.typeRepository = typeRepository;
    }

    @GetMapping
    public Iterable<CourseAndCurrentTeacher> getCoures(Optional<Long> organizationId, @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) Optional<Date> historyDate) {
        List<CourseAndCurrentTeacher> courses = new ArrayList<>();
        for (CourseAndCurrentTeacher course : courseAndCurrentTeacherRepository.findAll()) {
            if (organizationId.isEmpty()) {
                courses.add(course);
                continue;
            }
            if (course.getOrganization() != null && organizationId.get().equals(course.getOrganization().getId())) {
                courses.add(course);
            }
        }
        if(historyDate.isPresent()) {
            List<CourseAndCurrentTeacher> historyCourses = new ArrayList<>();
            for( CourseAndCurrentTeacher course : courses) {
                Date closest = new Date(Long.MIN_VALUE);
                CoursePrice current = null;
                for (CoursePrice coursePrice : coursePriceController.getCoursePrices(Optional.of(course.getId()))) {
                    if (coursePrice.getDate().after(closest) && coursePrice.getDate().before(historyDate.get()))  {
                        closest = coursePrice.getDate();
                        current = coursePrice;
                    }
                }
                if (current != null) {
                    course.setPrice(current.getPrice());
                    course.setPriceNds((int) Math.round(current.getPrice() * 1.2));
                    historyCourses.add(course);
                }
            }
            return historyCourses;
        }
        return courses;
    }

    @PutMapping
    public void put(@RequestBody Course course) {
        if(course.getType() != null) {
            course.setType(typeRepository.findById(course.getType().getId()).get());
        }
        courseRepository.save(course);
    }

    @PostMapping
    public Long post(@RequestBody Course course) {
        if(course.getType() != null) {
            course.setType(typeRepository.findById(course.getType().getId()).get());
        }
        courseRepository.save(course);
        return course.getId();
    }

    @DeleteMapping
    public void delete(@RequestParam Long courseId) {
        courseRepository.deleteById(courseId);
    }
}
