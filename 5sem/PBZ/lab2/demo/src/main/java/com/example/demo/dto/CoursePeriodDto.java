package com.example.demo.dto;

import java.util.Date;

public class CoursePeriodDto {
    private Date start;
    
    private Date end;

    private Integer students;

    public CoursePeriodDto(Date start, Date end, Integer students) {
        this.start = start;
        this.end = end;
        this.students = students;
    }

    public Date getStart() {
        return start;
    }

    public void setStart(Date start) {
        this.start = start;
    }

    public Date getEnd() {
        return end;
    }

    public void setEnd(Date end) {
        this.end = end;
    }

    public Integer getStudents() {
        return students;
    }

    public void setStudents(Integer students) {
        this.students = students;
    }

    
}
