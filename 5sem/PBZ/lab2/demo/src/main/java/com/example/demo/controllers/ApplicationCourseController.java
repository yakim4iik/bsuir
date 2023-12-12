package com.example.demo.controllers;

import com.example.demo.dto.CoursePeriodDto;
import com.example.demo.models.ApplicationCourse;
import com.example.demo.models.Course;
import com.example.demo.models.TeacherDocument;
import com.example.demo.repositories.ApplicationCourseRepository;
import com.example.demo.repositories.CourseRepository;
import com.example.demo.repositories.TeacherDocumentRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/application-course")
public class ApplicationCourseController {
    private final ApplicationCourseRepository applicationCourseRepository;
    private final CourseRepository courseRepository;
    private final TeacherDocumentRepository teacherDocumentRepository;

    public ApplicationCourseController(ApplicationCourseRepository applicationCourseRepository,
            CourseRepository courseRepository,
            TeacherDocumentRepository teacherDocumentRepository) {
        this.applicationCourseRepository = applicationCourseRepository;
        this.courseRepository = courseRepository;
        this.teacherDocumentRepository = teacherDocumentRepository;
    }

    @GetMapping
    public Iterable<ApplicationCourse> getAll(@RequestParam Optional<Long> applicationId) {
        List<ApplicationCourse> applicationCourses = new ArrayList<>();
        for (ApplicationCourse applicationCourse : applicationCourseRepository.findAll()) {
            if (applicationId.isEmpty()) {
                applicationCourses.add(applicationCourse);
                continue;
            }
            if (applicationCourse.getApplicationCourseId() != null &&
                    applicationId.get().equals(applicationCourse.getApplicationCourseId().getApplication().getId())) {
                applicationCourses.add(applicationCourse);
            }
        }
        return applicationCourses;
    }

    @GetMapping("/number")
    public List<CoursePeriodDto> getActualStudentsNumber(@RequestParam Long courseId,
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) Date from,
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) Date to) {

        List<CoursePeriodDto> periodList = getPeriodList(courseId, from, to);
        countStudents(periodList, courseId);
        return periodList;
    }

    @PutMapping
    public void put(@RequestBody ApplicationCourse applicationCourse) {

        applicationCourseRepository.save(applicationCourse);
    }

    @PostMapping
    public void post(@RequestBody ApplicationCourse applicationCourse) {
        applicationCourseRepository.save(applicationCourse);
    }

    @DeleteMapping
    public void delete(@RequestBody ApplicationCourse applicationCourse) {
        applicationCourseRepository.delete(applicationCourse);
    }

    private List<CoursePeriodDto> getPeriodList(Long courseId, Date from, Date to) {
        Course course = courseRepository.findById(courseId).orElseThrow();
        long courseLengthMilliseconds = (long) course.getDays() * 24 * 60 * 60 * 1000;
        List<CoursePeriodDto> periodList = new ArrayList<>();

        for (TeacherDocument teacherDocument : teacherDocumentRepository.findAll()) {
            if (Objects.equals(teacherDocument.getCourse().getId(), courseId)
                    && teacherDocument.getStart() != null && teacherDocument.getEnd() != null
                    && Math.max(from.getTime(), teacherDocument.getStart().getTime()) < Math.min(to.getTime(),
                            teacherDocument.getEnd().getTime())) {

                Date periodStart = teacherDocument.getStart();
                while (periodStart.before(to)) {
                    Date periodEnd = new Date(periodStart.getTime() + courseLengthMilliseconds);
                    if (periodEnd.after(teacherDocument.getEnd())) {
                        break;
                    }
                    if (periodEnd.after(from)) {
                        periodList.add(new CoursePeriodDto(periodStart, periodEnd, 0));
                    }
                    periodStart = periodEnd;
                }
            }
        }
        return periodList;
    }

    private void countStudents(List<CoursePeriodDto> periodList, Long courseId) {
        for (ApplicationCourse applicationCourse : applicationCourseRepository.findAll()) {
            if (courseId.equals(applicationCourse.getApplicationCourseId().getCourse().getId())) {
                for (CoursePeriodDto period : periodList) {
                    if (applicationCourse.getDate() == null || !period.getStart().after(applicationCourse.getDate()) &&
                            !period.getEnd().before(applicationCourse.getDate())) {
                        period.setStudents(period.getStudents() + 1);
                    }
                }
            }
        }
    }
}
