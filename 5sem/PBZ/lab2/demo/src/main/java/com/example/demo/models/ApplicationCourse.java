package com.example.demo.models;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.EmbeddedId;
import jakarta.persistence.Entity;

@Entity
public class ApplicationCourse {

    @EmbeddedId
    private ApplicationCourseId applicationCourseId;

    @Column
    private Date date;

    public ApplicationCourseId getApplicationCourseId() {
        return applicationCourseId;
    }

    public void setApplicationCourseId(ApplicationCourseId applicationCourseId) {
        this.applicationCourseId = applicationCourseId;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    
}
