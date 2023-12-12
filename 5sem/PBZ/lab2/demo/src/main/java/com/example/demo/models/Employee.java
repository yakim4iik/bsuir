package com.example.demo.models;

import jakarta.persistence.*;

@Entity
public class Employee extends Person {

    @ManyToOne
    @JoinColumn(name = "job_title_id")
    private JobTitle jobTitle;

    public JobTitle getJobTitle() {
        return jobTitle;
    }

    public void setJobTitle(JobTitle jobTitle) {
        this.jobTitle = jobTitle;
    }
}
