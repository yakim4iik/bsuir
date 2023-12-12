package com.example.demo.controllers;

import com.example.demo.models.CoursePrice;
import com.example.demo.repositories.CoursePriceRepository;
import com.example.demo.repositories.CourseRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/course-price")
public class CoursePriceController {
    private final CoursePriceRepository coursePriceRepository;
    private final CourseRepository courseRepository;

    

    public CoursePriceController(CoursePriceRepository coursePriceRepository, CourseRepository courseRepository) {
        this.coursePriceRepository = coursePriceRepository;
        this.courseRepository = courseRepository;
    }

    @GetMapping
    public Iterable<CoursePrice> getCoursePrices(Optional<Long> courseId) {
        List<CoursePrice> coursePrices = new ArrayList<>();
        for (CoursePrice coursePrice : coursePriceRepository.findAll()) {
            if (courseId.isEmpty()) {
                coursePrices.add(coursePrice);
                continue;
            }
            if (coursePrice.getCourse() != null && courseId.get().equals(coursePrice.getCourse().getId())) {
                coursePrices.add(coursePrice);
            }
        }
        return coursePrices;
    }

    @PutMapping
    public void put(@RequestBody CoursePrice coursePrice) {
        
        coursePriceRepository.save(coursePrice);
    }

    @PostMapping
    public CoursePrice post(@RequestBody CoursePrice coursePrice) {
        coursePrice.setDate(new Date());
        coursePrice.setCourse(courseRepository.findById(coursePrice.getCourse().getId()).get());
        coursePriceRepository.save(coursePrice);
        return coursePrice;
    }

    @DeleteMapping
    public void delete(@RequestParam Long coursePriceId) {
        coursePriceRepository.deleteById(coursePriceId);
    }
}
