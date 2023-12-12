package com.example.demo.models;

import java.util.Date;

import jakarta.persistence.*;

@Entity
public class Teacher extends Person {

    @ManyToOne
    @JoinColumn
    private Sex sex;

    @ManyToOne
    @JoinColumn
    private Education education;

    @Column
    private Date birthday;

    @ManyToOne
    @JoinColumn
    private Category category;

    public Sex getSex() {
        return sex;
    }

    public void setSex(Sex sex) {
        this.sex = sex;
    }

    public Education getEducation() {
        return education;
    }

    public void setEducation(Education education) {
        this.education = education;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
}
