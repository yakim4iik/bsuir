package com.example.demo.models;

import org.hibernate.annotations.Immutable;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity
@Immutable
public class CourseAndCurrentTeacher extends NamedEntity {

    @Column
    private String code;

    @ManyToOne
    @JoinColumn
    private Type type;

    @ManyToOne
    @JoinColumn
    private Organization organization;

    @Column
    private Integer days;

    @Column
    private Integer students;

    @Column
    private Integer price;

    @Column
    private Integer priceNds;

    @ManyToOne
    @JoinColumn
    private Teacher teacher;

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

    public Integer getDays() {
        return days;
    }

    public void setDays(Integer days) {
        this.days = days;
    }

    public Integer getStudents() {
        return students;
    }

    public void setStudents(Integer students) {
        this.students = students;
    }

    public Integer getPrice() {
        return price;
    }

    public void setPrice(Integer price) {
        this.price = price;
    }

    public Integer getPriceNds() {
        return priceNds;
    }

    public void setPriceNds(Integer priceNds) {
        this.priceNds = priceNds;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }

}
